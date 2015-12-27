---
layout: post 
title:  "C语言进阶：整型提升"
date:   2015-08-25 18:51:30 +0800
categories: 编程语言
tags: [C, 整型提升, 翻译]
---

原文链接：http://www.idryman.org/blog/2012/11/21/integer-promotion/

几乎每个程序员都学过C，而且大多数在他们的工作中使用C。很显然C是TIOBE（2012年11月时排榜首）上最流程的编程语言之一。然而，有时，C的行为会让人意外和困惑。其中一个例子就是**整型提升**。请看下面这个例子：

```c
#include <stdio.h>

int main(void)
{
    unsigned char a = 0xff;
    char b = 0xff;
    int c = a==b; // true, or false?
    printf("C: %d\n",c);
}
```
你可能认为输出是`1`.其实是`0`。噢！

<!-- more -->

#### C99标准

在K&R和C89的早期实现中，基于`short`和`char`的算术运算陷入两难的困境，因为可能会产生两种不同的结果。因此，在C99中很明确地定义了整型提升的规则（6.3.1.1）：

> 如果int能够表示原始类型中的所有数值，那么这个数值就被转成int型，否则，它被转成unsigned int型。这种规则被称为整型提升。所有其它类型都不会被整型提升改变。

让我们回忆一下整型的范围：

 - signed char: -127 -> 127
 - unsigned char: 0 -> 255
 - signed short: -32767 -> 32767
 - unsigned short: 0 -> 65535
 - signed int: -2147483647 -> 2147483647

可以看出有符号或者无符号的char、short都可以被signed int表示，所以当它们作算术运算时，都会被转成signed int。
在前面的例子中， `unsigned char a = 0xff` 的值是255。但是， `char b = 0xff` 的值是-1。当它们都被转为int类型时，`a` 仍然是255，即 `0x000000ff`， 而`b`却变成`0xffffffff` ，代表整型中的-1。以下代码可以证明：

```c
#include <stdio.h>

int main(void)
{
    unsigned char a = 0xff;
    char b = 0xff;
    printf("A: %08x, B: %08x\n", a, b);
    return 0;
}
```
输出结果是：

```
A: 000000ff, B: ffffffff
```
这就是为什么表示是`a==b`的结果是`0`。

#### 从汇编层面理解

当我第一次听说整型提升时，我更加困惑：为什么会有这么奇怪的规则？想要知道为什么这样设计，你必须从汇编代码中挖掘原因。

从一个简单的例子开始：

```c
int main(void)
{
    unsigned char a = 0xff;
    char b = 0xff;
    int c = a + b;
    return 0;
}
```
反汇编结果是：

```asm
movl    $0, -4(%rbp)        # The return value of main is 0
movb    $-1, -5(%rbp)       # unsigned char a = 0xff;
movb    $-1, -6(%rbp)       # char b = 0xff;
movzbl  -5(%rbp), %eax
movsbl  -6(%rbp), %ecx
addl    %eax, %ecx          # int c = a + b
movl    %ecx, -12(%rbp)     # store c onto the stack
movl    -4(%rbp), %eax
popq    %rbp
ret                         # return value 0 from eax
```
如果你的GAS语法不熟悉，可以查看X86 Assembly/GAS Syntax。GAS语法指令通常以“b”, “s”, “w”, “l”, “q” 和“t” 为后缀，以区分操作数在大小。

 - b = byte (8 bit)
 - s = short (16 bit integer) or single (32-bit floating point)
 - w = word (16 bit)
 - l = long (32 bit integer or 64-bit floating point)
 - q = quad (64 bit)
 - t = 10 bytes (80-bit floating point)

GAS语法中的mov是把参数从左边移到右边。例如： `movl $0, -4(%rbp)`的意思是把 `0x00000000` 移到地址 `-4(%rbp)`处。

指令 `movzbl` 表示把一个byte变成long并将空位**零填充** 。`movzbl -5(%rbp), %eax` 把 `0xff` 移到寄存器 `%eax` 上，并把空位补0。寄存器 `%eax` 的值变成了 `0x000000ff`。

指令 `movsbl` 表示把一个byte变成long并将空位**符号填充**。`movsbl -6(%rbp), %ecx` 把 `0xff` 移到寄存器 `%eax` ，然后把空位补成有符号的数值，这使得寄存器 `%ecx` 值变为 `0xffffffff`。最后， `addl %eax, %ecx` 执行加法操作， `movl %ecx, -12(%rbp)` 把结果存到栈上。

现在，你可以把整型提升理解为把C语言类型直接映射到机器指令的一种机制了。所有算术操作的操作数被转成有符号或无符号int后，都会被当作一个小的int的计算。你可以这么想：尽管short和char只占一两个字节，当它们在进行算术运算时，都是当作int的。这种转成int规则被称为整型提升。

#### 总结

通常情况下，在对int类型的数值作运算时，CPU的运算速度是最快的。在x86上，32位算术运算的速度比16位算术运算的速度快一倍。C语言是一个注重效率的语言，所以它会作整型提升，使得程序的运行速度尽可能地快。因此，你必须记住整型提升规则，以免发生一些整型溢出的问题。

作者：dryman (Felix Ren-Chyan Chern)
时间：11/21/2012
