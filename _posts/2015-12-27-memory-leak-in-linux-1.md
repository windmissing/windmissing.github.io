---
layout: post
title: "linux中内存泄漏的检测（一）最简单的方法"
category: linux
tags: [linux, memory leak]
---

#### 什么是内存泄漏

内存泄漏是指程序动态申请的内存在使用完后没有释放，导致这段内存不能被操作系统回收再利用。
例如这段程序，申请了4个字节的空间但没有释放，有4个字节的内存泄漏。

```c++
#include <iostream>
using namespace std;

int main()
{
     int *p = new int(1);
     cout <<*p<<endl;
     return 0
}
```
<!-- more -->

随着时间的推移，泄漏的内存越来越多，可用的内存越来越少，轻则性能受损，重则系统崩溃。

一般情况下，发生内存泄漏时，重启就可以回收泄漏的内存。但是对于linux，通常跑的是服务器程序，不可以随意重启，在内存泄漏问题上就要格外小心。

#### 内存泄漏特点

1. 难复现 — 要运行到足够长的时间才会暴露。

2. 难定位 — 出错位置是随机的，看不出与内存泄漏的代码有什么联系。

#### 最简单的方法

为了避免写出内存泄漏的程序，通常会有这样的编程规范，要求我们在写程序时申请和释放成对出现的。因为每一次申请都意味着必须有一次释放与它相对应。

基于这个特点，一种简单的方法就是在代码中统计申请和释放的次数，如果申请和释放的数量不同，就认为是内存泄漏了。

```c
#include "stdio.h"
#include "stdlib.h"

int malloc_count, free_count;

void * my_malloc(int size)
{
     malloc_count++;
     return malloc(size);
}
void my_free(void *p)
{
     free_count++;
     free(p);
}
int main()
{
     count = 0;
     int *p1 = (int *)my_malloc(sizeif(int))
     int *p2 = (int *)my_malloc(sizeif(int))
     printf("%d, %d", p1, p2);
     my_free(p1);
     if(malloc_count != free_count)
         printf("memory leak!\n");
     return 0
}
```

#### 方法分析

 - 优点：

直观，容易理解，容易实现

 - 缺点：

1.该方法要求运行结束时对运行中产生的打印分析才能知道结果。

2.该方法要求封装所有申请和释放空间的函数，并在调用的地方修改成调用封装后的函数。虽然C中申请/释放内存接口并不多，但是对于一个大型的项目，调用这些接口的地方却是很多的，要全部替换是一个比较大的工作量。

3.只对C语言适用，不能应用于C++

4.对于所调用的库不适用。如果希望应用于库，则要修改库代码

5.只能检测是否泄漏，却没有具体信息，比如泄漏了多少空间

6.不能说明是哪一行代码引起了泄漏

#### 改进

这种方法虽然简单的，却有许多的不足，无法真正应用于项目中。欲知怎样改进，且看下回分解。

[linux中内存泄漏的检测（一）最简单的方法](memory-leak-in-linux-1.html)

[linux中内存泄漏的检测（二）定制化的malloc/free](memory-leak-in-linux-2.html)

[linux中内存泄漏的检测（三）定制化的new/delete](memory-leak-in-linux-3.html)

[linux中内存泄漏的检测（四）记录泄漏的大小](memory-leak-in-linux-4.html)

[linux中内存泄漏的检测（五）定制内存泄漏的代码](memory-leak-in-linux-5.html)