---
layout: post
title:  "valgrind memcheck使用方法及效果"
category: linux
tags: [valgrind, memcheck]
---

#### 一、valgrind

##### 1. Valgrind是什么

Valgrind是运行在Linux上一套基于仿真技术的程序调试和分析工具，它包含一个内核──一个软件合成的CPU，和一系列的小工具，每个工具都可以完成一项任务──调试，分析，或测试等。Valgrind可以检测内存泄漏和内存违例，还可以分析cache的使用等

不管是使用哪个工具，valgrind在开始之前总会先取得对你的程序的控制权，从可执行关联库里读取调试信息。然后在valgrind核心提供的虚拟CPU上运行程序，valgrind会根据选择的工具来处理代码，该工具会向代码中加入检测代码，并把这些代码作为最终代码返回给valgrind核心，最后valgrind核心运行这些代码。

valgrind是高度模块化的，所以开发人员或者用户可以给它添加新的工具而不会损坏己有的结构。

<!-- more -->

##### 2. valgrind tool是什么

valgrind提供多种内存检测方法，用于检测不同的数据，满足不同的使用需求

可使用的工具如下：

（1）cachegrind是一个缓冲模拟器。它可以用来标出你的程序每一行执行的指令数和导致的缓冲不命中数。

（2）callgrind在cachegrind基础上添加调用追踪。它可以用来得到调用的次数以及每次函数调用的开销。作为对cachegrind的补充，callgrind可以分别标注各个线程，以及程序反汇编输出的每条指令的执行次数以及缓存未命中数。

（3）helgrind能够发现程序中潜在的条件竞争。

（4）lackey是一个示例程序，以其为模版可以创建你自己的工具。在程序结束后，它打印出一些基本的关于程序执行统计数据。

（5）massif是一个堆剖析器，它测量你的程序使用了多少堆内存。

（6）memcheck是一个细粒度的的内存检查器。

（7）none没有任何功能。它一般用于Valgrind的调试和基准测试。

##### 3. Valgrind怎么用

###### (1)安装

```
yum install valgrind
```

###### (2)运行

```
valgrind --tool=toolname args-val program args-pro
```
例如

```
valgrind --tool=memcheck ls -l
```

`--tool`选项，用于选择valgrind tool中的一种，后面接tool的名字。可以不加这个参考，则默认使用memcheck。

`args-val`选项，这是指valgrind可以添加的参数，用于配置单次运行时的特殊需求。

可以通过valgrind -h查看参数的各类的作用。

`program`选项，用于指定检测程序对象。valgrind对目标program的编译过程有些要求：

（1）打开调试模式（gcc编译器的-g选项）。如果没有调试信息，即使最好的valgrind工具也将中能够猜测特定的代码是属于哪一个函数。打开调试选项进行编译后再用valgrind检查，valgrind将会给出具体到某一行的详细报告。

（2）关闭编译优化选项(比如-O2或者更高的优化选项)。这些优化选项可能会使得memcheck提交错误的未初始化报告，因此，为了使得valgrind的报告更精确，在编译的时候最好不要使用优化选项。

`args-pro`选项，运行program所需要的参数。

#### memcheck

##### 1.valgrind memcheck是什么

memcheck是valgrind tool的一种，是一个细粒度的的内存检查器。它可以检测以下问题：

1）使用未初始化的内存

2）读/写已经被释放的内存

3）读/写内存越界

4）读/写不恰当的内存栈空间

5）内存泄漏

6）使用malloc/new/new[]和free/delete/delete[]不匹配。

7）src和dst的重叠

##### 2.运行

```
valgrind --tool=memcheck program args-pro
```
或

```
valgrind  program args-pro
```

##### 3.输出信息

（1）版本信息，其中`==`中间的数字（31549）是valgrind的进程ID，也是program的进程ID，它们是同一个进程。

```
==31549== Memcheck, a memory error detector
==31549== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==31549== Using Valgrind-3.10.0 and LibVEX; rerun with -h for copyright info
==31549== Command: ./uninit1
==31549==
```

后面的内容需要等程序运行结束才会出现。

（2）错误信息，不同的错误将出现不同的内容，下方将详细解说。

（3）总结

```
==31549== HEAP SUMMARY:
==31549==     in use at exit: 0 bytes in 0 blocks
==31549==   total heap usage: 0 allocs, 0 frees, 0 bytes allocated
==31549== 
==31549== All heap blocks were freed -- no leaks are possible
==31549== 
==31549== For counts of detected and suppressed errors, rerun with: -v
==31549== ERROR SUMMARY: 4 errors from 4 contexts (suppressed: 2 from 2)
```

##### 使用举例

##### 1.使用未初始化的内存

[《valgrind memcheck 使用未初始化的内存》](/linux/2016-02/valgrind-memcheck-uninitialized.html)

##### 2.读/写已经被释放的内存

[《valgrind memcheck 读/写已经被释放的内存》](/linux/2016-02/valgrind-memcheck-deleted.html)

##### 3.读/写内存越界

[《valgrind memcheck 读/写内存越界》](/linux/2016-02/valgrind-memcheck-outrange.html)

##### 4.读/写不恰当的内存栈空间

其它几篇都有读/写不恰当内存栈空间的例子

##### 5.内存泄漏

[《valgrind memcheck 内存泄漏》](/linux/2016-02/valgrind-memcheck-memleak.html)

##### 6.使用malloc/new/new[]和free/delete/delete[]不匹配

[《valgrind memcheck 使用malloc/new/new[]和free/delete/delete[]不匹配》](/linux/2016-02/valgrind-memcheck-mismatch.html)

##### 7.src和dst的重叠

###### 测试代码

```c++
#include <iostream>
using namespace std;

#include "string.h"

void test1()
{
    char ch[10] = "abcdefghi";
    char *p1 = ch;
    char *p2 = ch + 3;
    memcmp(p1, p2, 5);
}

int main()
{
    test1();
    return 0;
}
```

###### 编译及运行

```
g++ -g -o overlap val-overlap.cpp
valgrind --leak-check=full /home/vagrant/git_hub/windmissing.github.io/_posts/code/overlap
```
###### 检测结果

```
==29405== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 2 from 2)
```

###### 检测结果解读

对于不涉及到写的情况，src和dst重叠不算是问题

#### 四、Valgrind的特点

##### 1.优点

（1）检测对象程序在编译时无须指定特别的选项，也不需要连接特别的函数库

（2）valgrind被设计成非侵入式的，它直接工作于可执行文件上，因此在检查前不需要重新编译、连接和修改你的程序。要检查一个程序很简单，只需要执行下面的命令就可以了

（3）valgrind模拟程序中的每一条指令执行，因此，检查工具和剖析工具不仅仅是对你的应用程序，还有对共享库，GNU C库，X的客户端库都起作用。

（4）能打印堆栈信息，具体到某一行

（5）合并重复的信息
 
##### 2.缺点
（1）不同工具间加入的代码变化非常的大。在每个作用域的末尾，memcheck加入代码检查每一片内存的访问和进行值计算，代码大小至少增加12倍，运行速度要比平时慢25到50倍。 

（2）程序运行结束后才会显示结果
