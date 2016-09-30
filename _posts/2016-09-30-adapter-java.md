---
layout: post
title:  "JAVA设计模式之适配器"
category: [设计模式]
tags: []
---

#### 一、适配器模式

> 将一个类的接口转换成客户希望的另外一个接口，从而使得原本由于接口不兼容而不能一起工作的类可以一起工作。  
>                                          ———— 阎宏博士 《JAVA与模式》  

这句话摘自阎宏博士的《JAVA与模式》，为什么会需要把不能一起工作的类放一起呢？  

 - 场景一：  
 
项目决定使用第三方库A，因此在项目的代码中调用了A的接口。  
但考虑到以后有可能改用类似功能的第三库B，项目中调用A接口的代码全部改成调用B接口。  
这样做很不合理，而应该在项目与第三库之间增加适配器，当需要换第三方库时，只需要修改适配器的代码即可。  

 - 场景二：
 
lib提供了一套接口A，但随着时间的推移和业务的调整，客户希望以接口B的方式使用lib。  
为了满足客户的需求又不要影响到lib，在A和客户之间增加适配器。  

<!-- more -->

#### 二、要解决的问题

##### 1、先作以下定义

target：客户希望使用的接口称为target，target可以是接口类、抽象类或具体类。  
adapter：适配器。  
adaptee：需要被转换的类  

```
|--------       -------------|         |------------|
|        \       \           |---      |---         |
| target  >       > adapter     |         | adaptee |
|        /       /           |---      |---         |
|--------       -------------|         |------------|
```

##### 2、提出问题

期待增加adapter以后的效果：  
（1）像使用target一样地使用adapter（接口相同）。  
（2）adapter的使用效果与adaptee一样（功能相同）。  

##### 3、分析问题

（1）像使用target一样地使用adapter  
要使用target与adapter的接口相同，方法是继承。  
继承的作用就是统一接口。  
（2）adapter的使用效果与adaptee一样  
要使adapter具有adaptee相同的功能，就是要让adapter在target的接口的实现中调用adaptee提供的功能。  
做到这一点，有两种方法：  

 - 继承：adatper继承adaptee  
 - 组合：adatper引用adaptee

##### 4、解决问题

可以有两种方法解决2中提出的问题：  
方法一：类适配器模式  
adapter同时继承target和adaptee  
方法二：对象适配器模式  
adapter继承target。  
在adapter的实现中引用adaptee的对象。  

#### 三、类适配器模式

```
|--------|      |---------|
| target |      | adaptee |
|--------|      |---------|
    A                A
    |                | 
    ------------------
            |
       |---------|
       | adapter |
       |---------|
```

adapter继承了target，因此提供和target一样的接口。  
adapter继承了adaptee，所以adapter能够提供和adaptee一样的功能。  

```java
public interface Target {
    public void targetOperation(); 
}

public class Adaptee {
    public void originOperation(){}
}

public class Adapter extends Adaptee implements Target {
    @Override
    public void targetOperation {
        super.originOperation();
    }
}
```

#### 四、对象适配器模式

```
|--------| 
| target |
|--------|
    A     
    |     
|---------|                 |---------|
| adapter | ------------->  | adaptee |
|---------|                 |---------|
```

adapter继承了target，因此提供和target一样的接口。  
adapter引用了adaptee，所以adapter能够提供通过adaptee的对象使用adaptee的功能。  

```java
public interface Target {
    public void targetOperation(); 
}

public class Adaptee {
    public void originOperation(){}
}

public class Adapter implements Target{
    private Adaptee adaptee;
    
    public Adapter(Adaptee adaptee){
        this.adaptee = adaptee;
    }

    public void targetOperation(){
        this.adaptee.originOperation();
    }
}
```

#### 五、两种解决方案的比较

类适配器模式和对象适配器模式的区别在于adapter与adaptee的关系是继承还是组合。所以它们之前的比较也就是继承与组合的比较。  
继承关系既可以继承接口，又可以继承功能。但这种关系是静态的。因此继承主要用于统一接口而不是继承功能。  
组合关系不能继承接口，但可以使用它的功能，而且这种关系是可以在运行中动态组合的。  
在这里，adapter并不需要adaptee的接口，只需要它的功能。如果能够动态地使用它的功能会增加系统的灵活性。  
因此常见建议使用对象适配器模式。  
