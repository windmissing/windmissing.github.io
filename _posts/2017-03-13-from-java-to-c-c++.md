---
layout: post
title:  "从JAVA到C++ --- 快速上手篇"
category: [从JAVA到C++]
tags: []
---

一直觉得同为面向对象语言的JAVA和`C++`除了语法方面的不同之外，并没有什么本质的区别。从一个语言转换到另一个语言只是熟练程度的问题。直到现在授命给JAVA基础的人介绍`C/C++`才发现，C++只能算是半OOP的语言，和纯OOP的JAVA之间差别还是挺大的。于是把`C++`培训内容整理了一下，希望对读者有所帮助。   

<!-- more -->

#### 适合对象  
1.有JAVA基础，想了解C++  
2.已工作人士，通常没有时间和耐心去仔细学习另一门语言  
3.对C++所知不多，或写过一些类似hello world这样的小程序  

#### 目标
1.快速上手C++  
2.目前不需要使用C++，作为知识储备，希望在需要用到时能够知道怎么开始  

#### 大纲
##### 一、介绍
1.语言学习的困境  
[PPT]()
[MD]()
#### 语法方面的差别

JAVA相对于C++来说是后起之秀，在很多方面（比如OOP、丰富的库、垃圾回收、javadoc等）都更加完善。使JAVA开发者可以更加轻松地将注意力放到要实现的代码逻辑上。相对而言，C++的开发要同时关注的东西更多，束手束脚。  
从JAVA到C++，并不是一件容易的事。  

##### OO无关部分

[内存管理：内存、堆、栈、地址、指针、引用、值](http://windmissing.github.io/%E4%BB%8Ejava%E5%88%B0c++/2017-03/java-to-cpp-on-memory.html)  
参考链接：[地址、内存、堆、栈总结](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2012-01/address-memory-heap-stack.html)  
  
[字节对齐]()  
内存泄漏  
[指针和引用](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2012-01/porinter-and-reference-in-cpp.html)  
异常处理  
typedef和#define  
类型转换  
头文件（哪些放头文件，头文件包含导致的重定义，头文件包含导致的符号冲突）  
生命周期
关键字：const, static

##### OO相关部分

权限管理
类的大小  
[复制控制成员](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2012-01/copy-control-members-summerize.html)  
[操作符重载](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2012-01/operator-overloading-in-cpp.html)  
[接口与多重继承](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2015-12/supperclass-inheritance.html)  
virtual：默认非动态捆绑，需要加该关键字  

##### C与C++

class与struct  
string与char  
iostream与print

##### 函数式编程部分

C11/14
匿名函数

##### 库

stl  
网络库  
线程库  

#### 编程思想方面的差别

原以为JAVA和C++的区别主要在于功能的完善度和内存管理。  
仔细阅读thinking in JAVA后发现，JAVA和C++最本质的区别在于它们的设计的初衷不同。  
C++追求的是速度，而JAVA追求的是安全。  
JAVA在借鉴C++时，抛弃了那些不安全的内容（比如指针操作），对于不能抛弃的内容则采取了以较为安全的方法实现

1.内存管理  
[C++内存管理](http://windmissing.github.io/%E4%BB%8Ejava%E5%88%B0c++/2017-03/java-to-cpp-on-memory.html)  
[JAVA内存管理]()

#### 参考文章

http://blog.csdn.net/acosoft/article/details/4351549  
http://www.2cto.com/kf/201406/312122.html