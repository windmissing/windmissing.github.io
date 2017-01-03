---
layout: post
title:  "java中易混淆的关键字"
category: [编程语言]
tags: [JAVA, ]
---

#### extends与implement

```java
class A extends B implement C, D
```

在这段代码中，A**继承**B，同时**实现**C和D。  
JAVA只支持单继承，但有时也使用上面这样的语法来实现多重继承，那么继承和实现到底是什么关系？  
先来说说相同点（先约定称A下级类，BCD为上级类）：  
继承和实现都能起到统一接口的作用，A中同时包含了BCD和接口  
可以通过上级类使用下级类（多态）

||extends|implement|
|---|---|---|
|术语|继承|实现|
|对上一级类的要求|不能继承final类和abstract类|interface类|
|上一级的数量|只能继承一个类|可以实现多个接口，可以用于实现多重继承|
|下一级类的要求|派生类可以什么都不做就直接使用|必须要实现interface定义的接口才能使用|

#### abstract与interface

