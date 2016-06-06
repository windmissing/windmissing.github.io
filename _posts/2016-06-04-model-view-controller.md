---
layout: post
title:  "ios开发中的MVC模型"
category: ios
tags: [ios, MVC]
---

#### general description  
MVC广泛应用于UIKit中，它包括Ｍ、Ｖ、Ｃ这三个主要组件以及它们之间的关系。  
![](/image/mvc_general_description.jpg)  

<!-- more -->

主要组件：  
M(odel):一个或多个Model对象  
V(iew):通常是view hierarchic，包括buttons、sliders、textboxes等  
C(ontroller):  
关系：  
图中的实线表示强引用，虚线表示弱引用。这里强引用和弱引用的概念类似于C++中强关联和弱关联的概念  
M对象和V对象是C的成员  
M和V的部分实现需要用到C对象  

#### MVC的设计目的：  
##### 1.集中化管理  
1.1 变化与更新  
当V发生了变化，它会与C通信，然后C去更新M  
M发生变化时同理  
1.2 生命周期  
通常情况下，C首先被创建  
然后C（实际上是C的父类）创建M和V  
#### 2.avoid replication of data  

#### 强引用与弱引用  
##### 强引用
string reference implies ownership  
Ｃ对象强用引Ｍ对象和Ｖ对象  
当一个对象被一个或多个对象强引用时，它会停留在内存中  
当Ｃ对象不再Ｍ、Ｖ对象时，可以解除引用关系  
当一个对象不被任何对象强引用时，它会自动地deallocate  
##### 弱引用  
week reference does not imply ownership  
Ｍ对象和Ｖ对象弱引用Ｃ对象，它们只是需要与Ｃ通信，但不占有Ｃ  
当被引用的对象deallocated，对它的引用自动变成nil。  

#### View  
##### 所有View类都UIView子类  
每个View类可以包括一组子类，称为View Hierarchic  
View类还可以包括一系列contraints  
##### 怎样创建View类  
1.通过storyborad/nib file，这种方式最常用  
（1）编辑storyboard，然后build  
（2）所有的对象都创建到内存中  
（3）对象呗保存到nib file中  
（4）创建controller  
（5）controller尝试读取view对象  
（6）被引用的对象读到内存中  
2.通过代码  
##### 什么时候创建view对象  
第一次尝试引用View对象的对象  
##### 谁创建View对象  
UIViewController  

#### Controller
Controller是UIViewController的子类  
UIViewController中包含“从storyboard/nib file中加载View对象”的代码，所以controller能够加载View对象  
##### Controller与View之间的关系  
Controller的父类UIViewController强引用View  
View的子类subview弱引用Controller，称为action  
Controller弱引用View的子类subview，称为outlet  
##### Controller与Model之间的关系  
Controller强引用Model  
Model弱引用Controller  
![](/image/reference_relationship_between_MVC.jpg)
