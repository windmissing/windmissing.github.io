---
layout: post
title:  "C++虚函数易错题"
category: [编程语言]
tags: [C++, virtual]
---

本文不介绍C++虚函数的用法，也不分析虚函数的原理。只是针对自己在工作中由于虚函数使用不当遇到的问题做个总结。

问题1：virtual关键字涉及到两个类（基类和派生类）对同一个函数（函数名、参数、返回值类型都相同）的声明和实现。

既然两个类都声明了同一个函数，那么virtual关键字是放在基类还是放在派生类？可以两个类里都加上virtual?virtual关键字的位置对运行结果有什么影响呢？

[virtual关键字在父类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-1.html)

[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)

问题2：如果问题1中提到的函数正好是类的析构函数，结果又会怎样呢？

[析构函数的virtual在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-3.html)

问题3：问题1的测量场景中，虚函数都是被直接调用的。如果虚函数又是被另一个函数调用的，另一个函数是虚函数/非虚函数/基类函数/重写函数，会对虚函数的结果有什么影响呢？

[间接调用虚函数](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-4.html)

<!-- more -->
