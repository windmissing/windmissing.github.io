---
layout: post
title: "linux中内存泄漏的检测（三）定制化的new/delete"
category: linux
tags: [linux, memory leak]
---

[《linux中内存泄漏的检测（二）定制化的malloc/free》](/linux/2015-12/memory-leak-in-linux-2.html)中的__wrap方法只解决了C的问题，这一节介绍怎么让C++中的new/delete也能方便地插入计数代码。

#### wrap方法尝试

可不可以使用`__wrap_new/__wrap_delete`?我们试试看。

<!-- more -->

我写了这样的测试代码

```c++
#include <iostream>
using namespace std;

int count = 0;

void * __wrap_new(size_t size)
{
    count++;
    return __real_new(size);
}

void __wrap_delete(void *ptr)
{
    count--;
    __real_delete(ptr);
}

int main()
{
    count = 0;
    int *p1 = new int;
    int *p2 = new int;
    delete p1;
    if(count != 0)
        cout<<"memory leak!"<<endl;
        return 0;
}

```
然后这样编译，`g++ -o test test.cpp -Wl,--wrap,new -Wl,--wrap,delete`，结果

```
cpptest.cpp: In function ‘void* __wrap_new(size_t)’:
cpptest.cpp:9:27: error: ‘__real_new’ was not declared in this scope
     return __real_new(size);
                           ^
cpptest.cpp: In function ‘void __wrap_delete(void*)’:
cpptest.cpp:15:22: error: ‘__real_delete’ was not declared in this scope
     __real_delete(ptr);
     ^
```
     
看来这种方法不可行，这要从new和malloc的区别说起。

#### new VS. malloc

malloc很好理解，它的作用就是分配一段指定大小的内存空间。

而new的工作分为两步：

第一步也是分配一段指定大小的内存空间，这一步与malloc相同，它有一个专用的名字，叫operator new

第二步是将分配到的内存以指定的方式初始化化，这是malloc所没有的，它也有一个专用的名字，叫placement new

|步骤|作用|与malloc的关系|是否可以重载|怎样使用
|:---:|:---:|:---:|:---:|:---:|
|operator new|分配一段指定大小的空间|相当于malloc|可以重载|可以单独调用，如`class *pA = operator new(100)`，相当于`class *pA = malloc(100);`|
|placement new|将一段空间以指定的方式初始化|malloc不能提供这样的功能|不能重载|可以把空间的指针作为参数传入，单独调用这一行为执行初始化操作，如`class *pA = new(buf) class();`，相当于使用class::class()初始化buf这段内存

关于operator new和placement new和更多细节，可以参考更多文章，但显然new的功能非常复杂，并不是一个`__wrap_new(size_t size)`能解决的。

#### operator new 重载

new的功能虽然复杂，但我们所关心的只是其中与分配内存相关的部分，也就是operator new。幸好，它可以重载。

C++支持重载，我们可以重载new中的operater new，在其中加入计数功能，并通过malloc实现内存申请。

```c++
#include <iostream>
using namespace std;

#include <stdio.h>
#include <stdlib.h>

int count = 0;

void * operator new(size_t size)
{
    count++;
    return malloc(size);
}

void operator delete(void *ptr)
{
    count--;
    free(ptr);
}

int main()
{
    count = 0;
    int *p1 = new int;
    int *p2 = new int;
    delete p1;
    if(count != 0)
        cout<<"memory leak!"<<endl;
        return 0;
}
```

既然new也是通过调用malloc实现的，那么也不用operator new和malloc分别统计了，只需要统计malloc就行了。因为`__wrap_symbol`和`__real_symbol`都是C函数，所有要使用`extern "C"`。

```c++
#include <iostream>
using namespace std;

#include <stdio.h>
#include <stdlib.h>

int count = 0;

extern "C"
{
void* __real_malloc(int c); 
void * __wrap_malloc(int size)
{
    count++;
    return __real_malloc(size);
}

void __real_free(void *ptr);
void __wrap_free(void *ptr)
{
    count--;
    __real_free(ptr);
}
}

void * operator new(size_t size)
{
    return malloc(size);
}

void operator delete(void *ptr)
{
    free(ptr);
}

int main()
{
    count = 0;
    int *p1 = new int(3);
    int *p2 = new int(4);
    cout<<*p1<<' '<<*p2<<endl;
    delete p1;
    if(count != 0)
        cout<<"memory leak!"<<endl;
        return 0;
}
```

#### 分析

 - 优点

（1）不需要改产品代码，只需要修改编译选项即可完成。

（2）wrap是个链接选项，对所有通过`__wrap_malloc`和`__wrap_free`链接到一起的文件都起作用，不论是静态库还是动态库。

（3） c 的检测与c++的检测无缝兼容

 - 缺点

（1）该方法要求运行结束时对运行中产生的打印分析才能知道结果。

（2）只能检测是否泄漏，却没有具体信息，比如泄漏了多少空间

（3）不能说明是哪一行代码引起了泄漏

（4）这一方法虽然解决了C++的替换问题，却引入了新的问题。因为在C++中对于同一指针申请和释放，申请和释放的大小却有可能不相等，导致有些情况的内存泄漏检测不到。比如

(a)申请子类而析构父类

(b)申请数组而释放数组第一项

#### 改进

欲知如何解决，且看下回分解

[linux中内存泄漏的检测（一）最简单的方法](memory-leak-in-linux-1.html)

[linux中内存泄漏的检测（二）定制化的malloc/free](memory-leak-in-linux-2.html)

[linux中内存泄漏的检测（三）定制化的new/delete](memory-leak-in-linux-3.html)

[linux中内存泄漏的检测（四）记录泄漏的大小](memory-leak-in-linux-4.html)

[linux中内存泄漏的检测（五）定制内存泄漏的代码](memory-leak-in-linux-5.html)
