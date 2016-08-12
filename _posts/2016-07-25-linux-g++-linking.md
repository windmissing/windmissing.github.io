---
layout: post
title:  "linux g++ 链接"
category: [compile]
tags: [g++, linking, linux]
---

我们都知道，要把源代码变成可以运行的程序，需要经过编译、链接等步骤。  
其中编译步骤很好理解，就是把我们写的高级语言程序变成机器能够理解的机器指令的过程。  
那么既然已经机器指令了，为什么还需要链接才能运行呢？链接究竟做了什么？怎么做的？  
这就是我们今天的主题。  
![](http://img.my.csdn.net/uploads/201607/25/1469431311_9533.jpg)

<!-- more -->

#### 基础概念

[ linux g++ 链接器（一）基础概念](http://windmissing.github.io/compile/2016-07/linux-g++-basic-conception.html)

#### 一个实验

请看这样四个文件：

 - head.h

```c++
#include <iostream>
using namespace std;
void myfun(); 
```

 - main.cpp

```c++
#include "head.h“
int main()
{
    myfun();
    return 0;
} 
```

 - a.cpp

```c++
#include "head.h“
void myfun()
{
    cout<<"myfun in a.cpp"<<endl; 
} 
```

 - b.cpp

```c++
#include "head.h“
void myfun()
{
    cout<<"myfun in b.cpp"<<endl; 
}
```

把这四个文件生成目标文件并链接到一起会怎样呢？为什么？  
A. 链接错误  
B. 打印“myfun in a.cpp”  
C. 打印“myfun in b.cpp”  
D. 看情况
  
源代码可以编译成三种目标文件，不同目标文件之间的链接方法不同，结果也不同。读完后面的内容，就能明白其中的道理。  

完整实验请阅读[link](http://windmissing.github.io/compile/2015-04/symbol-redifine-in-g++-ld.html)

#### 可重定位目标文件的链接
[可重定位目标文件的链接](http://windmissing.github.io/compile/2016-07/static-linking-g++.html)

#### 静态库的链接  

静态库可以简单看作是一组可重定位文件的打包。  
虽然链接命令中是把所有文件打包拿来的，但不是每个文件都真的用得到。  
链接静态库和链接可执行文件相比，只是多了一步筛选文件的动作。  

![](http://img.my.csdn.net/uploads/201607/26/1469514066_2980.jpg)
在链接开始之前，链接器会维持两份表，一份记录已定义的符号，另一份记录未定义的符号。
链接器会先把静态链接器拆包，然后一一筛选。只有当前未定义符号的表中符号且能被那个文件能提供，文件才会被留下来。其它的文件都会被扔掉。

筛选剩下的文件与其它的可重定位文件一起，进入后面的静态链接过程。  
静态链接过程与可重定位文件的静态链接过程完全一致。分为文件合并、地址分配和重定位三个步骤，以及happy endding、one-on-one和符号缺失三种链接结果。

上文的例子中，如果先链接a.o生成的liba.a，那么libb.a中的b.o就会被扔掉。  
只有main.o和a.o链接，所以链接器不会报错而链接a.o中的符号。

#### 共享目标文件的链接

[共享目标文件的链接](http://windmissing.github.io/compile/2016-07/dynamic-linking-g++.html)
