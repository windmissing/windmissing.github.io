---
layout: post
title: "linux中内存泄漏的检测（五）记录内存泄漏的代码"
category: linux
tags: [linux, memory leak]
---

到目前为止，先后通过wrap malloc、new函数重载和计算指针内存大小的方法，基本上满足了对内存泄漏检测的需要。

如果发现了内存泄漏，那么就要找到内存泄漏的地方并且修正它了。

茫茫代码，如何去找？如果能根据未释放的内存找到申请它的地方就好了。

我们今天就是要做这个事情。

<!-- more -->

想要根据内存地址查出申请者的信息，那么在一开始申请的时候就要建立地址与申请者之间的映射。

1.内存地址

内存地址，是一个unsigned long型的数值，用`void *`来存储也可以。为了避免类型转换，我使用了`void *`。

2.申请者信息

申请者的信息比较复杂，不是一个类型可以搞定的。它包括哪些内容呢？

在C情况下，主要是需要知道谁调用了`__wrap_malloc`。但在C++情况下，调用`__wrap_malloc`的一定是new，这没有什么意义，还需要知道是谁调用了new。再进一步说，new有可能是在构造函数中被调用的，那么很有可能我们真正需要知道的是谁调用了构造函数。

由此可见，仅仅知道是谁调用了`__wrap_malloc`不够的，我们需要的是整个栈信息。

整个栈包含了很多内容，在这里，我们只记录栈的深度（int）和每一层的符号名（char **）。符号名在整个程序中是唯一的（不管C还是C++）且相对位置是确定的（动态库除外），当程序结束时再根据符号名反推出调用者的文件名和行号。

为什么不直接获取文件名和行号？
因为求符号名的实现比较简单。

3.映射方式

说到映射，首先想到的是map、hash这样的东西。

但需要说明的是，这里是`__wrap_malloc`函数，是每次程序动态分配空间时必然会走到的地方。

这有什么关系呢？想象一下，在由于某个动态申请内存的操作来到了这个函数，而在这个函数里又不小心申请了一次内存，会怎样呢？在`-Wl,--wrap,malloc`的作用下又来到了这里，于是开启了“鸡生蛋、蛋生鸡”的死循环中，直到——stack overflow。

所以，在这个函数里能使用的，只能使用栈空间或者全局空间，如果一定要使用堆空间，也必须显示地使用`__real_malloc`代替new或者malloc。由于在map、hash中会不可避免地使用动态内存空间的情况，还是放弃吧。

怎么办呢？为了避免节外生枝，我这里使用了最简单但是有点笨的方法——数组。

```c++
struct memory_record
{
    void * addr;
    size_t count;
    int depth;
    char **symbols;
}mc[1000];
```

4.怎样获取栈中的符号？

gcc给我们提相应的函数，按照要求调用就行。

```c++
char* stack[20] = {0};
mc[i].depth = backtrace(reinterpret_cast<void ** >(stack), sizeof(stack)/sizeof(stack[0])); 
if (mc[i].depth){ 
    mc[i].symbols = backtrace_symbols(reinterpret_cast<void**>(stack), mc[i].depth); 
}
```
 backtrace函数用于获取栈的深度（`depth`），以及每一层栈地址（`stack`）。
`backtrace_symbols`函数根据栈地址返回符号名（`symbols`）。
需要注意的是，backtrace_symbols返回的是符号的数组，这个数组的空间是由`backtrace_symbols`分配的，但需要调用者释放。

为什么这里`backtrace_symbols`分配了内存却没有引起stack overflow呢？以下是我的猜测：
`backtrace_symbols`函数和wrap机制都是GNU提供的，属性亲戚关系。既然是亲戚，那么大家通融一下，让`backtrace_symbols`绕过wrap机制直接使用内存也是有可能的。

源代码：

```c++
#include <iostream>
using namespace std;

#include "string.h"
#include <stdio.h>
#include <malloc.h>
#include <execinfo.h>

#if(defined(_X86_) && !defined(__x86_64))
#define _ALLOCA_S_MARKER_SIZE 4
#elif defined(__ia64__) || defined(__x86_64)
#define _ALLOCA_S_MARKER_SIZE 8
#endif

size_t count = 0;

int backtrace(void **buffer, int size);

struct memory_record
{
    void * addr;
    size_t count;
    int depth;
    char **symbols;
}mc[1000];

extern "C"
{
void* __real_malloc(int c); 
void * __wrap_malloc(size_t size)
{
    void *p =  __real_malloc(size);
    size_t w = *((size_t*)((char*)p -  _ALLOCA_S_MARKER_SIZE));
    cout<<"malloc "<<p<<endl;
    for(int i = 0; i < 1000; i++)
    {
        if(mc[i].count == 0)
        {
            count += w;
            mc[i].addr = p;
            mc[i].count = w;
            char* stack[20] = {0};
            mc[i].depth = backtrace(reinterpret_cast<void**>(stack), sizeof(stack)/sizeof(stack[0])); 
            if (mc[i].depth){ 
                mc[i].symbols = backtrace_symbols(reinterpret_cast<void**>(stack), mc[i].depth); 
            } 
            break;
        }
    }
    return p;
}

void __real_free(void *ptr);
void __wrap_free(void *ptr)
{
    cout<<"free "<<ptr<<endl;
    size_t w = *((size_t*)((char*)ptr -  _ALLOCA_S_MARKER_SIZE));
    for(int i = 0; i < 1000; i++)
    {
        if(mc[i].addr == ptr)
        {
            mc[i].count -= w;
            count -= w;
            if(mc[i].symbols)
                 __real_free(mc[i].symbols); 
            break;
        }
    }
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

void print_leaked_memory()
{
     if(count != 0)
        cout<<"memory leak!"<<endl;
     for(int i = 0; i < 1000; i++)
     {
         if(mc[i].count != 0)
         {
             cout<<mc[i].addr<<' '<<mc[i].count<<endl;
             if (mc[i].symbols){ 
                 for(size_t j = 0; j < mc[i].depth; j++){ 
                     printf("===[%d]:%s\n", (j+1), mc[i].symbols[j]); 
                 } 
             } 
             __real_free(mc[i].symbols);
         }
     }
}

class A
{
    int *p1;
public:
    A(){p1 = new int;}
    ~A(){delete p1;}
};

int main(void)
{
    memset(mc, 0, sizeof(mc));
    count = 0;
    int *p1 = new int(4);
    int *p2 = new int(5);
    delete p1;
    print_leaked_memory();
	return 0;
}
```

编译命令：

```
g++ -o test test.cpp -g -Wl,--wrap,malloc -Wl,--wrap,free
```

运行：

```
./test | grep "===" | cut -d"[" -f3 | tr -d "]" | addr2line -e test
```

方法分析：

优点：

（1）在程序运行结束时，打印程序内存泄漏情况以及导致泄漏发生的代码所在的文件及行号

（2）C/C++都适用

（3）需要修改产品源代码即可实现功能

（4）对一起链接的所有.o和静态库都有效

缺点：

（1）对动态库不适用

（2）求堆栈信息和求文件名行号是两个操作，不能一次性解决问题


#### 改进

[linux中内存泄漏的检测（一）最简单的方法](memory-leak-in-linux-1.html)

[linux中内存泄漏的检测（二）定制化的malloc/free](memory-leak-in-linux-2.html)

[linux中内存泄漏的检测（三）定制化的new/delete](memory-leak-in-linux-3.html)

[linux中内存泄漏的检测（四）记录泄漏的大小](memory-leak-in-linux-4.html)

[linux中内存泄漏的检测（五）定制内存泄漏的代码](memory-leak-in-linux-5.html)