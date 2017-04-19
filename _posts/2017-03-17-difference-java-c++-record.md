---
layout: post
title:  "JAVA C++ 语法区别记录"
category: [从JAVA到C++]
tags: []
---

读<thinking in jAVA>时发现了一些C++与JAVA在语法上的差别，记录一下，以备使用。  

<!-- more -->

**JAVA中的引用更像是C++里指针的概念**

||JAVA|C++|
|---|---|---|
||动态绑定（多态）是默认行为|使用virtual关键字来实现|
||单根继承，终极基类是Object|无终极基类|
|容器|持有其它对象的引用（指针）|可以持有指针、或者值，不能持有引用|
|变量名|对于内置类型，变量名代表值，对于类类型，变量名代表引用（指针）|与类型无关，变量名代表值，*变量名代表指针，&变量名代表引用|
|对象的生命周期|完全动态管理|自由选择动态或静态|
|销毁对象|GC|由编程决定|
|异常处理|一开始就内置了异常处理，且强制使用|无强制|
|并发编程|内置|无|
||引用可以独立于对象存在|指针可以独立于对象存在，但引用不可以|
||某些数据存于栈中（如引用），对外存于堆中|存于哪里与类型无关，与创建方式有关|
||内置类型不用new创建，而是创建一个非引用的“自动”变量，直接储值，存于堆中|同上，内置类型无特殊，指针引用或值取决于创建方式。|
|基本类型所占空间大小|不变|部分类型与机器有关|
||所有数值类型有正负号|unsigned表示无符号类型，有符号与无符号之间的转换容易出错|
|boolean大小|没有明确规定|8bit|
|包装器类|用于在堆上创建基本类型|无|
|数组|安全。默认初始化，未分配空间或越界会报错|危险，未初始化或越界|
|隐藏较大作用域的变量|不允许|有|
||对象可以存活于作用域之外|与创建方式有关|
|方法创建|必须在类中|类成员方法，或者全局方法|
|方法参数传递|对象传引用，内置类型传值|指针引用或值都可以|
|前身引用限制|无|有|
|文件名与类名|必须相同|无限制|
|文档|javadoc|无|
|操作符重载|无|有|
|数字自动转为字符串|有P54|无|
|while(x=y)|报错|相当于x=y,while(y)|
|类类型转换|不可以，或子类到父类|可以，实现一个转换函数|
|sizeof()|无|有|



#### 其它

单根继承的好处是什么？  
为什么说JAVA的并发是内置于语言中的？  