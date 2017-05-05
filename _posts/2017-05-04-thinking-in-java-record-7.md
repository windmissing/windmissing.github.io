---
layout: post
title:  "《thinking in JAVA》片断记录 (七)"
category: [读书笔记]
tags: []
---

#### main()方法

可以为每个类都创建一个main()方法。  
可使每个类的单元测试都变得简单易行。  
只有命令行所调用的那个类的main()方法会被调用。  

<!-- more -->

---

#### super

JAVA用super表示超类的意思。  
*C++用`父类的类名::`表示父类，在多重继承或多继承层级的情况下，可以明确的知道使用的是哪个超类。  
JAVA只有supuer，它是怎么区分的呢？*  

---

#### 代理

**代理是继承与组合之间的中庸之道，因为我们将一个成员对象置于所要构造的类中（就像组合），但与此同时我们在新类中暴露了该成员对象的所有方法（就像继承）。**
*不理解*

---

#### 确保正确的清理

如果你想要某个类清理一些东西，就必须显式地编写一个特殊的方法（如dispose）来做这件事，并要确保客户端程序员知晓他们必须要调用的这一方法。  
必须将这一清理动作置于finally子句之中，以预防异常的出现。  

```java
public stativ void main(String[] args)
{
    CADSystem x = new CADSystem(47);
    try {
        ... 
    } finally {
        x.dispose();
    }
}
```

子类清理时，先清理自己，再调用基类的dispose()，顺序与生成相反。  

---

#### 重写与重载

重写：子类方法的名称与参数与父类完全一样  
重载：子类方法的名称与与父类的相同，参数不同  
@Override表示只能重写不能重载。  

```java
class Lisa extends Homer {
    @Override void doh(Milhouse m) {
        ...
    }
}
```

若父类中没有doh(Milhouse m)，就会报错。  

---

#### 组合与继承

组合技术通常用于想在新类中使用现有类的功能而非它的接口。

---

#### protected

对类用户来说是private的。  
对类的导出类**或**位于同一个包的类，是可以访问的。  

---

#### final

##### final作用于基本类型

相当于常量。  
但可以这样写：  

```java
final int j; //空白final
...
j = 1; //用的时候再初始化
j = 2; //不能再次赋值
```

##### final作用于引用

相当于 * const，即指针的内容不能变，指向的内容的内容可以变。  
适用于空白final用法。  

##### final作用于方法

1.防止继承类覆盖它（pivate都默认是final的）  
2.相当于inline，效率优化

##### finaly作用于类

这个类不能被继承

---

#### 类static成员的加载

在C++中，如果某个static期望另一个static在被初始化之前就能有效地使用它，那么就会出现问题。  
*怎么说？*

**JAVA中的所有事物都是对象。  
每个类的编译代码都存在于它自己的独立的文件中。
该文件只在需要使用程序代码时才会被加载，即类的代码在初次使用时会加载。  
这通常是指加载发生于创建类的第一个对象之时。  
但是当访问static域可static方法时，也会发生加载。**
*没发现有什么区别？*  

---

#### 包含继承的初始化

1. 加载子类  
2. 加载基类  
3. 基类的static初始化  
4. 子类的static初始化  
5. 对象创建  
6. 内存清零  
7. 基类构造器  
 - 7.1基类实例变量初始化  
 - 7.2基类构造器调用
8. 子类构造器
 - 8.1子类实例变量初始化
 - 8.2子类构造器调用
 
```java
public class Insect {  
    private int i = 9;  
    protected int j;  
  
    public Insect() {  
        System.out.println("i = " + i + ", j = " + j);  
        j=39;  
    }  
  
    private static int x1 = printInit("static Insect.x1 initialized");  
  
    static int printInit(String s) {  
        System.out.println(s);  
        return 47;  
    }  
}  
package com.mufeng.theseventhchapter;  
  
public class Beetle extends Insect {  
    private int k = printInit("Beetle.k initialized");  
  
    public Beetle() {  
        System.out.println("k = " + k + ", j = " + j);  
    }  
  
    private static int x2 = printInit("static Beetle.x2 initialized");  
  
    public static void main(String[] args) {  
        System.out.println("Beetle constructor");  
        Beetle b = new Beetle();  
    }  
}  
```
输出：  

```
static Insect.x1 initialized   // 3
static Beetle.x2 initialized   // 4
Beetle constructor 
i = 9, j = 0                   // 7.2
Beetle.k initialized           // 8.1
k = 47, j = 39                 // 8.2
```