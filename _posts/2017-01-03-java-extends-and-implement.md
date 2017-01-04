---
layout: post
title:  "extends与implement"
category: [编程语言]
tags: [JAVA]
---

```java
class A extends B implement C, D
```

在这段代码中，A**继承**B，同时**实现**C和D。  
JAVA只支持单继承，但有时也使用上面这样的语法来实现多重继承，那么继承和实现到底是什么关系？  

<!-- more -->

#### 先来说说相同点

##### 都能起到统一接口的作用

A中同时包含了BCD和接口  

```java
public class A extends B implements C
{
    public void printA()
    {
        System.out.println( "this is A" );
    }

    public void printC()
    {
        System.out.println( "this is C" );
    }
}
public class B
{
    public void printB()
    {
        System.out.println( "this is B" );
    }
}
public interface C
{
    public void printC();
}
public class Main
{
    public static void main( String[] args )
    {
        A a = new A();
        a.printA();
        a.printB();
        a.printC();
    }
}
```

##### 可以实现多态

```java
public class A extends B implements C
{
    public void printB()
    {
        System.out.println( "this is A and B" );
    }

    public void printC()
    {
        System.out.println( "this is A and C" );
    }
}
public class A2 extends B implements C
{
    public void printB()
    {
        System.out.println( "this is A2 and B" );
    }

    public void printC()
    {
        System.out.println( "this is A2 and C" );
    }
}
public class B
{
    public void printB()
    {
        System.out.println( "this is B" );
    }
}
public interface C
{
    public void printC();
}
public class Main
{
    public static void main( String[] args )
    {
        B a = new A();
        a.printB();
        B a2 = new A2();
        a2.printB();

        C c = new A();
        c.printC();
        C c2 = new A2();
        c2.printC();
    }
}
```

#### 语法上的区别

||extends|implement|
|---|---|---|
|术语|继承|实现|
|对父类的要求|不能继承final类|interface类|
|父类的数量|只能继承一个类|可以实现多个接口|
|子类的要求|派生类可以什么都不做就直接使用|必须要实现interface定义的接口才能使用|

```java
public class B
{
    public void printB()
    {
        System.out.println( "this is B" );
    }
}
public class A extends B
{
}
public interface C
{
    public void printC();
}
public class A2 implements C
{
    public void printC()
    {
        System.out.println( "this is A2 and C" );
    }
}
public class Main
{
    public static void main( String[] args )
    {
        A a = new A();
        a.printB();

        A2 a2 = new A2();
        a2.printC();
    }
}
```

#### 用法上的区别

继承与实现在意义上就是不同的，不限于JAVA。  
extends中的父类，是把多个子类的相同点抽象出来。继承是子类是父类的功能扩展。扩展的功能是必定是子类特有的功能，是属于这个子类的功能。  
```
public class 鸡
{
    public void eat(){}
    public void sleep(){}
}
public class 乌鸡 extends 鸡
{
    public static color = black;
}
public class 潜水鸡 extends 鸡
{
    public void swim(){}
}
```
implements提供的是另一种抽象，对接口的抽象，强制要求子类实现某些接口。实现是要求子类增加一些父类的接口。增加的接口不一定是属于这个子类的功能。是为了让子类能够被别的系统使用，必须要实现的接口。  

```
interface 飞
{
    public void 飞行();
}
class 鸟 implements 飞
{
    public void 飞行(){用翅膀飞}
}
class 孙悟空 implements 飞
{
    public void 飞行(){踩着筋斗云飞}
}
```