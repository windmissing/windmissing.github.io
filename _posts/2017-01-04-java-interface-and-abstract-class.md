---
layout: post
title:  "interface与abstract class"
category: [编程语言]
tags: [JAVA]
---

java中有两种特殊的类，它们都代表抽象，不能实例化，因此常常让人傻傻分不清，它们就是interface与abstract class。  
abstract class是指类中包含了抽象方法的类，abstract class的派生类实现了其中所有的抽象方法，就变成了普通的可以实例化的类，否则仍然是abstract class。  
interface则抽象程度更高，所有的方法都是抽象的。interface可以被继承，但继承的类也是interface。interface可以被实现，但实现的类必须把interface中所有的接口都实现。  

<!-- more -->

#### 语法上的区别

abstract class本质上还是个类，具有类的特征，而interface本质上是个接口。  
结合普通的class来对比它们之间的差别  

||class|abstract class| interface|
|---|---|---|---|
|翻译|类|抽象类|接口|
|普通成员变量|可以有|可以有|无|
|静态成员变量|可以有|可以有|必须是public static final|
|普通成员方法|可以有|可以有|无|
|抽象成员方法|无|可以有，public或protected|必须全部是抽象方法，public abstract|
|静态方法|可以有|可以有|无|
|构造函数|不能是抽象的或者静态的|不能是抽象的或者静态的|无|
|派生类|class|class或者abstract class|interface|
|实现类|不能被实现|不能被实现|能，但需要实现其中全部的接口|

#### 用法上的区别

##### extends与implement

abstract class被用来extends，interface主要用来implement，因此它们之间的区别类似于[extends与implement]()之间的区别。  
interface可以被extends，用于扩展接口。  

##### 产生常量群

interface中的变量默认为public static final，可以把一类常量放到一起管理，例如：  

```java
public interface Months{
    int JANURAUY = 1;
    int FEBRUARY = 2;                   
    int MARCH =3;
}
```

使用的时候`import Months.JANURAUY`