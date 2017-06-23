---
layout: post
title:  "《thinking in JAVA》片断记录 (十)"
category: [读书笔记]
tags: []
---

内部类的对象能访问其外围类对象的所有成员，而不需要任何特殊条件。  
这点与C++的嵌套类的设计非常不同，在C++中只是单纯的名字隐藏机制，与外围对象没有联系，也没有隐含的访问权。  

---

当外围类的对象创建一个内部类的对象时，内部类对象会秘密地捕获一个指向外围类对象的指针。   
当内部类对象需要访问外围类对象的成员时，是通过这个指针访问的。  

---

必须使用外部类的对象来创建内部类的对象。 

```java
public class outter
{
    public class inner{}
    public static void main(String[] args)
    {
        outter o = new outter();
        outter.inner i = dn.new inner();
    }
}
```

---

嵌套类 ！= 内部类
内部类：非静态的内部类
嵌套类：静态的内部类

---

在Outter类的内部创建一个实现Destination接口的内部类Inner，且把它说明为private。  

```java
public interface Destination {
    String readLabel();
}

class Outter {
    private class Inner implements Destination {
        private String label;
        private Inner(String l) {label = l;}
        public String readLabel() {return label;}
    }
    public Destination createInner(String s) {
        return new Inner(s);
    }
}

public class test {
    public static void main(String[] args)
    {
        Outter o = new Outter();
        Destination d = o.createInner("Tasmania");
        d.readLabel();
    }
}
```

效果：  
Inner类只能被Outter类访问，客户端的访问是受到限制的。  
客户端无法知道关于Inner的细节，仅知道它实现了Destination接口。  
客户端只能以接口Destination接口的方法来使用Inner，阻止任何依赖于类型的编码。  

---

1.虽然代码写在b条件下，但类的创建不是有条件。它和其它的类一起编译过了。  
2.在b条件的作用域下才可以使用这个类。  

```java
public class Outter {
    public void func(boolean b){
        if(b) {
            class Inner {}              //1
            Inner i = new Inner();
        }
        Inner i = new Inner();          //2
    }
}
```

---

#### 创建匿名内部类

```java
public class Outter {
    public Inner inner() {
        return new Inner () {   // 1
            private int i = 11;
            public int value() {return i;}
        };                      // 2
    }
}
```

 - 1.不是创建Inner类的对象，而是**创建一个继承自Inner的匿名子类的对象。**  
 - 2.分号不要漏掉了

---

#### 匿名类中使用外部对象

##### 在匿名类的基类中使用

```java
public class Outter {
    public Inner inner(int x) {     // 2
        return new Inner (x) {      // 1
            public int value() {return super.value;}
        }; 
    }
}
```

 - 1.此处调用了基类的构造函数Inner(int x);
 - 2.x给了基类的构造器，没有被匿名类内部直接使用，因为不要求为final  

##### 在匿名类中使用

```java
public class Outter {
    public Inner inner(final String dest) {
        return new Inner () {
            private String label = dest;    // 1
            public String value() {return label;}
        }; 
    }
}
```

 - 1.匿名类使用外部对象dest，外部对象必须为final
 
 ---
 
#### 匿名内部类的构造器

匿名内部类没有名字，所以不可能有构造器。  
但可以通过**实例初始化**达到为匿名内部类创建一个构造器的效果。  

```java
public class Outter {
    public Inner inner() {
        return new Inner (final String dest) {
            private String label;
            {                           // 1
                System.out.println("inside instance initializer");
                label = dest;           // 2
            }
            public String value() {return label;}
        }; 
    }
}
```

 - 1.这段区间的代码相当于构造器
 - 2.此处使用了外部的dest，dest必须为final

---

匿名内部类既可以实现接口，也可以扩展类。  
但是匿名内部类只能实现**一个**接口**或**扩展**一个**类。  

---

优先使用类而不是接口。  
如果你的设计中需要某个接口，你必须了解它。  
否则，不到迫不得已，不要将其放到你的设计中。

---

声明为static的内部类被称为嵌套类。  
普通内部类不能有static数据、static字段和嵌套类。  
嵌套类则无此限制。  

---

#### 嵌套类的应用1
通常情况下，接口内部不能放代码。  
但接口内可以有嵌套类。  
接口内的嵌套类可以实现其外围接口。  
如果想要创建某些公共代码，使得它们可以被某个接口的所有不同实现共用，那么使用接口内部的嵌套类会很方便。  

---

#### 嵌套类的应用2

可以通过在每个类中加main()方法的方法来测试这个类，但缺点是发布时会带着这些额外的代码。  
也可以把测试代码放在类的嵌套类中，发布是把对应的.class文件删掉即可。  

```java
public class TestBed {
    public void f() { //... }
    public static class Tester {                    //发布时删掉TestBed$Tester.class
        public static void main(String[] args) {
            TestBed t = new TestBed();
            t.f();                                  //测试代码
        }
    }
}
```

---

#### 为什么需要内部类

内部类继承自某个类或实现某个接口，又可以访问创建它的外围类的对象。因此，内部类提供了某种进入其外围类的窗口。  

通过内部类实现接口与外围类直接实现接口有什么区别？  
1.每个内部类能独立地继承自一个（接口的）实现。所以，无论外围类是否已经继承了某个（接口的）实现，对于内部类都没有影响。  
2.如果继承一个抽象类，只能用内部类

---

通过内部类实现闭包的功能，比指针更灵活、安全  

---

#### 控制框架

控制框架被设计用以解决某类特定的问题，调用一个或多个可覆盖的方法。  
模板方法包含基本的算法结构，提供一套通用的解决问题方案。  
可覆盖的方法是变化的事物。  

内部类能够很容易地访问外围类的任意成员，所以可以避免这种实现变得笨拙。

---

继承一个内部类，构造器必须这么写：

```java
class WithInner {
    class Inner{}
}

public class InheritInner extends WithInner.Inner {
    InheritInner() {}   // compile error
    InheritInner(WithInner wi) {    //这个参数必须要
        wi.supper();                //这一句必须要
    }
}
```

---

一个外围类中定义了一个内部类。  
然后继承此外围类，并重写一个同名的内部类，  
那么继承类的内部类会覆盖基类的内部类吗？  
答：不会。这两个内部类是完全独立的两个实体，各自在自己的命名空间。  

```java
class Outer
{
    protected inner{}
}
class Outer2 extends Outer
{
    public inner{}
}
```

---

|| 函数中的局部内部类 | 函数中的匿名内部类|
|---|---|---|
|构造器|可以重载构造器|只能用于实例初始化|
|对象|可以创建多个对象|只能创建一个对象|

---

内部类的标识：外围类名$内部类名
匿名内部类的标识：外围类名$数字