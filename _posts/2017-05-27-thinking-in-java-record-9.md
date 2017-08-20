---
layout: post
title:  "《thinking in JAVA》片断记录 (九)"
category: [读书笔记]
tags: []
---

接口和内部类为我们提供了一种将**接口与实现分离**的更加结构化的方法。  
创建抽象类是希望通过这个通用接口操纵一系列类。  

---

包含抽象方法的类叫做抽象类。  
也可以创建一个不包含抽象方法的抽象类，仅仅是为了阻止该类产生对象。  

---

创建抽象类和抽象方法非常有用，因为它们可以使类的抽象性明确起来，并告诉用户和编译器打算怎样来使用它们。  
抽象类还是很有用的重用工具，因为它们使得我们可以很容易地将公共方法沿着继承层次结构向上移动。

---

任何使用某特定接口的代码都知道可以调用该接口的哪些方法，而且仅需要知道这些。  
接口被用来建立类与类之间的协议。  

---

在接口中定义的方法必须被定义成public。  
默认声明为public，而不是包访问权限。（与普通类不同）  

---

创建一个能够根据所传递的参数对象的不同而具有不同行为的方法，被称为**策略模式**。  
这类方法包含所要执行的算法中固定不变的部分，而“策略包含”变化的部分。  
策略就是传递进去的参数对象，它包含要执行的代码。  

![](/image/thinking-in-java-9-0.png)  

---

策略模式的基础是继承，因此有一定的局限性，当它遇到这样一种新的操作Filter：    
1.它做的工作和Processor类似  
2.它不适合继承Processor  
3.这个操作的参数和返回的类型与process不同  
![](/image/thinking-in-java-9-1.png) 

解决方法是把Process变成一个interface
让Filter和StringProcessor都实现这个interface

---

这种解决方法仍有一个问题，如果Filter是一第三方类，无法改变它让它实现某个接口，那么就要用到**适配器模式**。

![](/image/thinking-in-java-9-2.png) 

---

当需要表示“一个x是一个a和一个b以及一个c”时。  
C++使用多重继承，它可能会使你背负很沉重的包袱，因为每个类都有一个具体的实现。  
JAVA中，接口没有任何具体的实现。一个类只能继承一个父类，可以实现多个接口。因此一个类只有一个具体的实现，不会出现JAVA的问题。  

---

#### 接口的使用举例

一个接受接口类型的方法，而该接口的实现和向该方法传递的对象则取决于方法的使用者。  

```java
interface CanFight{
    void fight();
}
interface CanSwim{
    void swim();
}
interface CanFly{
    void fly();
}
class ActionCharacter{
    public void fight(){
        System.out.println("I can fight!");
    }
}
class Hero extends ActionCharacter implements CanFight,CanSwim,CanFly{
    public void swim(){
        System.out.println("I can swim!");
    }
    public void fly(){
        System.out.println("I can fly!");
    }
}
public class Adventure {
    public static void t(CanFight x){x.fight();}
    public static void u(CanSwim x){x.swim();}
    public static void v(CanFly x){x.fly();}
    public static void w(ActionCharacter x){x.fight();}
    public static void main(String[] args){
        Hero h=new Hero();
        t(h); //Treat it as a CanFight
        u(h);
        v(h);
        w(h);
    }
}
```

---

interface可以多重继承

```java
interface A extends B, C {
    //...
}
```

---

打算组合的不同接口中使用相同的方法名通常会造成代码可读性的混乱，应尽量避免这种情况。  

```java
interface I1{void f();}
interface I2{int f(int i);}
class C2 implements I1, I2{
    //...
}
```

---

接口中的域自动是static和final的，因此成为创建常量组的工具。  

---

# 嵌套接口

---

生成遵循某个接口的对象的典型方式就是**工厂方法**设计模式。  
这与直接调用构造器不同，我们在工厂对象上调用的是创建方法，而该工厂对象将生成接口的某个实现的对象。  
理论上，通过这种方式，我们的代码将完全与接口的实现分离。  

![](/image/thinking-in-java-9-3.png)  

---

应该重构接口而不是到处添加额外级别的间接性，并由此带来额外的复杂性。  
优先选择类而不是接口。
