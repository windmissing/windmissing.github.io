---
layout: post
title:  "g++/ld中的符号重定义"
category: [compile]
tags: [g++, ld]
---

#### O、什么是符号

符号是指代码中的变量与函数。  
[链接中的符号](http://windmissing.github.io/compile/2015-04/symbols-in-linking.html)

#### 一、分析

在外部符号和可引出符号的解析过程中，都有可能遇到符号重定义的问题。  
当链接器发现符号重定义时会怎么处理吗？它会报错吗？ 
不要这么急着下结论。  
本着“实践是检验真理的唯一标准”的原则，我们一起做几个实验。  

#### 二、实验材料

##### 文件准备

head.h

```c++
#include <iostream>
using namespace std;

void myfun();
```

a.cpp

```c++
#include "head.h"
void myfun()
{
	cout<<"myfun in a.cpp"<<endl;
}
```
b.cpp

```c++
#include "head.h"
void myfun()
{
	cout<<"myfun in b.cpp"<<endl;
}
```
main.cpp

```c++
#include <iostream>
using namespace std;

#include "head.h"
int main()
{
	myfun();
	return 0;
}
```

##### 文件加工

gcc/ld可以链接三种类型的可重定位目标文件，分别是目标文件（.oxx）、静态链接库（.a）和动态链接库（.so）。因此把a.c和b.c分别编译成不同的文件类型，来观察不同文件类型造成的符号重定义的链接结果。

（1）把a.cpp和b.cpp分别编译成a.oxx和b.oxx

```
```
（2）把a.cpp和b.cpp分别编译成liba.a和libb.a

```
```
（3）把a.cpp和b.cpp分别编译成liba.so和libb.so

```
```

#### 三、实验过程及结果

|实验序号|a.cpp编译生成的文件类型|b.cpp编译生成的文件类型|操作语句|链接结果（成功、失败）|若成功，链接进去的是哪个文件，若失败，先链接进去的是哪个文件|
|---|---|---|---|---|---|
|1|a.oxx|b.oxx|g++ -o main main.cpp a.oxx b.oxx|失败||
|2|a.oxx|libb.a|g++ -o main main.cpp a.oxx libb.a|成功|a.oxx|
|3|a.oxx|libb.so|g++ -o main main.cpp a.oxx -L. -lb|成功|a.oxx|
|4|liba.a|b.oxx|g++ -o main main.cpp liba.a b.oxx|失败|liba.a|
|5|liba.a|libb.a|g++ -o main main.cpp liba.a libb.a|成功|liba.a|
|6|liba.a|libb.so|g++ -o main main.cpp liba.a -L. -lb|成功|liba.a|
|7|liba.so|b.oxx|g++ -o main main.cpp -L. -la b.oxx|成功|b.oxx|
|8|liba.so|libb.a|g++ -o main main.cpp -L. -la libb.a|成功|liba.so|
|9|liba.so|libb.so|g++ -o main main.cpp -L. -la lb|成功|liba.so|

#### 四、分析结果
（1）1 => 当一个符号在多个目标文件(.o)里同时出现时, LD报错. 提示符号多重定义.  
[普通目标文件的符号解析与重定义处理策略](http://windmissing.github.io/compile/2015-04/symbol-confliction-in-normal-target-file.html)  
（2）5， 6， 8， 9 => 当一个符号在多个静态库(.a)或者动态库(.so)里同时出现时, LD不报错, 以第一个遇到的为准.   
（3）3， 7 => 当一个符号在目标文件(.o)和动态库(.so)里同时出现时，取目标文件(.o)里的符号  
（4）2 =>  
[静态库的符号解析和重定义处理策略](http://blog.csdn.net/mishifangxiangdefeng/article/details/45127863)  

有些情况下，链接器发现重定义后会提示链接错误，让我们及时地发现问题。可有些情况，链接器会悄悄地选择其中一个定义而忽略其它定义，这样就产生了难以定义的BUG。 
