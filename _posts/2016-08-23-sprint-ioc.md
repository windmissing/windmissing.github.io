---
layout: post
title:  "spring framework中的IOC技术"
category: [back-end]
tags: [sprint, java, IOC]
---

> spring是一个基于IOC和AOP的构架多层J2EE系统的框架。  
使用IOC技术使得它可以很容易实现bean的装配。  

也许这些官方介绍过于抽象让你不知所云。但实际上IOC技术并不是spring framework所特有的，它是一种架构设计的思想。  
本文简单说一说IOC是怎么回事。

<!-- more -->

#### 一、IOC

IOC即Inversion of Control，翻译为控制反转。  
正常情况下，A类的对象a想要使用B类的对象，那么a应该创建一个对象并使用它。就是“A依赖B”。  
B类的对象可以是b，也可以是b1，甚至可以是BB类的对象bb。a究竟要创建哪一个，完全由a说了算。这就是a的控制。  
这时候出现了IOC容器。当a需要使用B类的对象时，它并不直接创建，而是向IOC申请。IOC决定创建怎样的对象，而a只能被动地接受IOC创建的B类对象。这就是控制反转。  

#### 二、DI

常常与IOC伴随出现的是DI。DI即Dependency Injection，翻译为依赖注入。  
依赖，在上文中已经讲过。  
既然a要使用B的对象（A依赖B），而IOC代替a创建了B的对象，那么IOC还要把它创建的对象交给a，这就是依赖注入。  

#### 三、依赖注入的方法

依赖注入的方法有两种，  
 - （1）构造器注入是指在生成对象时的构造函数中注入。  
 - （2）setter注入是指每次调用setter函数时注入。    
两种方法的原理基本上类似，就是IoC容器根据xml配置文件生成依赖对象，然后调用构造函数或setter函数把对象传给使用者。  
因此代码主要分为两部分，  
 - （1）包含构造函数或者setter函数的使用者类  
 - （2）xml配置文件。  
本文只是一个栗子，更详细的说明在别的文章中介绍。

##### 1.构造器注入

使用构造器参数来注入依赖关系

```java
package examples;

public class ExampleBean  {

    // the SimpleMovieLister has a dependency on a MovieFinder
     private int years;
     private String ultimateAnswer;

    // a constructor so that the Spring container can 'inject' a MovieFinder
    public ExampleBean(int years, String ultimateAnswer) {
        this.years = years;
        this.ultimateAnswer = ultimateAnswer;
    }
    
    // business logic that actually 'uses' the injected elements is omitted...
}
```

通过使用'type'属性来显式指定那些简单类型的构造参数的类型

```
<bean id="exampleBean" class="examples.ExampleBean">
  <constructor-arg type="int" value="7500000"/>
  <constructor-arg type="java.lang.String" value="42"/>
</bean>
```

##### 2.Setter注入

通过调用无参构造器或无参static工厂方法实例化bean之后，调用该bean的setter方法，即可实现基于setter的DI。  

```java
public class ExampleBean {

    private AnotherBean beanOne;
    private YetAnotherBean beanTwo;
    private int i;

    public void setBeanOne(AnotherBean beanOne) {
        this.beanOne = beanOne;
    }

    public void setBeanTwo(YetAnotherBean beanTwo) {
        this.beanTwo = beanTwo;
    }

    public void setIntegerProperty(int i) {
        this.i = i;
    }    
}
```

相关的XML配置如下：

```
<bean id="exampleBean" class="examples.ExampleBean">

  <!-- setter injection using the nested <ref/> element -->
  <property name="beanOne"><ref bean="anotherExampleBean"/></property>

  <!-- setter injection using the neater 'ref' attribute -->
  <property name="beanTwo" ref="yetAnotherBean"/>
  <property name="integerProperty" value="1"/>
</bean>

<bean id="anotherExampleBean" class="examples.AnotherBean"/>
<bean id="yetAnotherBean" class="examples.YetAnotherBean"/>
```
