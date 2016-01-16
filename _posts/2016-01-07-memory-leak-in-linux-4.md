---
layout: post
title: "linux中内存泄漏的检测（四）记录泄漏的大小"
category: linux
tags: [linux, memory leak]
---

[《linux中内存泄漏的检测（三）定制化的new/delete》](memory-leak-in-linux-3.html)讲到，利用C++的函数重载的特性，使C++的代码，也能方便地为new/delete加上用于检测内存泄漏的统计代码。然而，也因此引入的新的问题。

目前的统计方式仅仅统计申请/释放内存的次数，并没有统计每次申请/释放内存的大小。
这种方法对于C来说是够用了，因为在C中申请和释放的大小是相同的，而在C++中就不一定了。
考虑以下两种情况：

<!-- more -->

（1）申请了子类的空间却只释放了父类的空间

```c++
father *pF = new son;
delete pF;
```
构造子类的时候申请的是子类所需大小的空间，然后先初始化父类的成员，再初始化子类的成员。

析构的时候，由于是父类的指针，只调用父类的析构函数并释放父类所占的空间。
不是说多态吗？既然pF指针子类，为什么不调用子类的析构函数？
因为多态的前提是虚函数。

正常情况下类的析构函数都应该写成虚函数，如果忘了，就有可能造成内存泄漏。

（2）申请了一个数组的空间却只释放第一项元素的空间

```c++
class A *pA = new class[5];
delete pA;
```
也不是所有这样的情况都会导致内存泄漏，如果class是一个内置类型，像int, char这种，就没有问题。对于内置类型，只能说没有内存泄漏方面，但有可能会有其它未知的潜在问题，所以仍不建议这么写。
在C++中，class就不限于内置类型了，如果是自己定义的类，delete pA只是释放pA所指向的数组的第一项，这样就产生了内存泄漏。

由于以上原因，仅仅统计申请/释放的次数，还不能准确地检测内存泄漏的情况，因此，在申请/释放的同时，还要记录大小。

大家在写代码的时候，有没有产生过这样的疑问，为什么申请内存时要传入所需要申请的内存大小，而释放时不需要说明释放多大的内存？

那是因为在申请时，把所申请的大小记在了某个地方，释放时从对应的对方查出大小。那么记在什么地方呢？

 > 一般有两种方式： 

 > 1 非入侵式，内存分配器自行先申请内存（和栈配合使用），用作记录用户层的申请记录（地址，大小）。 用户释放空间时会查找该表，除了知道释放空间大小外还能判断该指针是合法。

 > 2 入侵式，例如用户要申请1byte的内存，而内存分配器会分配5byte的空间（32位），前面4byte用于申请的大小。释放内存时会先向前偏移4个byte找到申请大小，再进行释放。

 > 两种方法各有优缺点，第一种安全，但慢。第二种快但对程序员的指针控制能力要求更高，稍有不慎越界了会对空间信息做成破坏。

我们linux上的gcc/g++编译器默认使用入侵式，为了验证我们找到的地址是否存储了我们想要的数据，我写了这样的测试代码：

```c++
#include <iostream>
using namespace std;

#if(defined(_X86_) && !defined(__x86_64))
#define _ALLOCA_S_MARKER_SIZE 4
#elif defined(__ia64__) || defined(__x86_64)
#define _ALLOCA_S_MARKER_SIZE 8
#endif

int main(void)
{
	void * p = NULL;
	int a = 5, n = 1;
	while (a--)
	{
		p = new char[n];
		size_t w = *((size_t*)((char*)p -  _ALLOCA_S_MARKER_SIZE));
        cout<<"w = "<< w <<" n = "<<n<<endl;
        n = n * 10;
	}
	return 0;
}
```
这是运行结果：

w = 33 n = 1

w = 33 n = 10

w = 113 n = 100

w = 1009 n = 1000

w = 10017 n = 10000

当我们读取申请到的内存的前面几个字节时，查到的数据与真实申请的数据好像有关系，但是又总是略大一点。这是不是我们要找的数据呢？它和真实申请的大小有什么关系呢？这要从gcc的内存分配策略说起。

假设现在要申请空间大小为n，实际分配的大小为m，我们读取到的值为k

（1）当调用malloc申请n个大小的空间，编译器还会多分配_ALLOCA_S_MARKER_SIZE个字节用于存储这片空间的管理信息。在我所测试的centos 64上这个管理信息一共8个字节，上文提到的申请空间的大小的信息就在其中。那么m=n+_ALLOCA_S_MARKER_SIZE

（2）为了减少内存碎片，实现申请的大小为一个数的整数倍，在我所测试的centos 64上测得这个数为16，即实际申请的大小为16的倍数。那么m=(n+8-1)&0xFFFFFFF0 + 0x10

（3）为了避免申请过小的内存，有这样一个限定，最小的实际分配空间大小为0x20
m = (n+8-1)&0xFFFFFFF0 + 0x10 if m < 0x20 m = 0x20

（4）因为m一定为16的倍数，所以在二进制中m的最后四位始终为0，并不起作用。因此这4位用于做标准位。于是有k = m + 1

总结m = (n+7)&0xFFFFFFF0 + 0x11  ， k = m + 1

为了证明这个结论是正确的，我写了这样的代码：

```c++
#include <iostream>
using namespace std;

#include<assert.h>
#include<ctime>
#include <stdlib.h>

#if(defined(_X86_) && !defined(__x86_64))
#define _ALLOCA_S_MARKER_SIZE 4
#elif defined(__ia64__) || defined(__x86_64)
#define _ALLOCA_S_MARKER_SIZE 8
#endif

int main(void)
{
	void * p = NULL;
	srand(time(0));
	int a = 100000;
	while (a--)
	{
		int n = rand() % 10000;
		p = new char[n];
		size_t w = *((size_t*)((char*)p -  _ALLOCA_S_MARKER_SIZE));
        if ( n <= 8) n = 9;
        int n2 = ((n+7) & 0xFFFFFFF0) + 0x11;
        assert(n2 == w);
	}
	return 0;
}
```
实际上我们在统计的时候并不关心调用者申请的大小，而是编译器真正申请和释放的大小，即，代码如下：

```c++
#include <iostream>
using namespace std;

#include <stdio.h>
#include <malloc.h>

#if(defined(_X86_) && !defined(__x86_64))
#define _ALLOCA_S_MARKER_SIZE 4
#elif defined(__ia64__) || defined(__x86_64)
#define _ALLOCA_S_MARKER_SIZE 8
#endif

size_t count = 0;

extern "C"
{
void* __real_malloc(int c); 
void * __wrap_malloc(int size)
{
    void *p =  __real_malloc(size);
    size_t w = *((size_t*)((char*)p -  _ALLOCA_S_MARKER_SIZE)) - 1;
    count += w;
    cout<<"malloc "<<w<<endl;
    return p;
}

void __real_free(void *ptr);
void __wrap_free(void *ptr)
{
    size_t w = *((size_t*)((char*)ptr -  _ALLOCA_S_MARKER_SIZE)) - 1;
    count -= w;
    cout<<"free "<<w<<endl;
    __real_free(ptr);
}
}

void *operator new(size_t size)
{
    return malloc(size);
}

void operator delete(void *ptr)
{
    free(ptr);
}

int main(void)
{
    count = 0;
    int *p1 = new int(3);
    int *p2 = new int(4);
    cout <<*p1<<' '<<*p2<<endl;
    delete p1;
    if(count != 0)
        cout<<"memory leak!"<<endl;
	return 0;
}
```

现在我们分别针对以上提到的两种情况测试：

（1）申请了子类的空间却只释放了父类的空间

```c++
class father
{
    int *p1;
public:
    father(){p1 = new int;}
    ~father(){delete p1;}
};
class son : public father
{
    int *p2;
public:
    son(){p2 = new int;}
    ~son(){delete p2;}
};

int main(void)
{
    count = 0;
    father *p = new son;
    delete p;
    if(count != 0)
        cout<<"memory leak!"<<endl;
	return 0;
}
```
（2）申请了一个数组的空间却只释放第一项元素的空间

```c++
class A
{
    int *p1;
public:
    A(){p1 = new int;}
    ~A(){delete p1;}
};

int main(void)
{
    count = 0;
    A *p = new A[5];
    delete p;
    if(count != 0)
        cout<<"memory leak!"<<endl;
	return 0;
}
```

分析：

- 方便性：

|功能|是否支持|说明
|:---:|:---:|:---:| 
|运行时检查|否|该方法要求运行结束时对运行中产生的打印分析才能知道结果。
|修改是否方便|是|wrap函数实现非常简单，且只需要实现一次，对所有参与链接的文件都有效
|使用是否方便|是|要关掉这一功能，只需要将这个链接选项去掉即可

 - 全面性：

|功能|是否支持|说明
|:---:|:---:|:---:| 
|C接口是否可以统一处理|否|C的每个接口都需要分别写包装函数
|C++接口是否可以统一处理|是|
|动态库与静态库的内存泄漏是否可以检测到|是|wrap是个链接选项，对所有通过wrap与`__wrap_malloc`和`__wrap_free`链接到一起的文件都起作用，不管是.o、.a或者.so

- 准确性：

|功能|是否支持|说明
|:---:|:---:|:---:| 
|是否会有检测不到的情况|否|
|是否可以定位到行|否|
|是否可以确定泄漏空间的大小|是|

#### 改进

[linux中内存泄漏的检测（一）最简单的方法](memory-leak-in-linux-1.html)

[linux中内存泄漏的检测（二）定制化的malloc/free](memory-leak-in-linux-2.html)

[linux中内存泄漏的检测（三）定制化的new/delete](memory-leak-in-linux-3.html)

[linux中内存泄漏的检测（四）记录泄漏的大小](memory-leak-in-linux-4.html)

[linux中内存泄漏的检测（五）定制内存泄漏的代码](memory-leak-in-linux-5.html)
