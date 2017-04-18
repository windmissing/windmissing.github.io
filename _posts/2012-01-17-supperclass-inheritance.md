---
layout: post
title:  "基类与派生类、继承关系总结"
category: 编程语言
tags: [C++, 继承, 基类, 派生类]
---

#### 基类与派生类

##### 类型相互转换

派生类的对象可以赋给基类，反之不行

基类的指针可以指向派生类，反之不行

基类的引用可以初始化为派生类的对象，反之不行

派生类指针必须强制转换为基类指针后才可以指向基类

基类指针转换为派生类指针容易导致崩溃性错误

虚基类的引用或派生不能转换为派生类

<!-- more -->

```c++
class father{};
class son:public father{}; 
int main()
{
    father f; 
    son s;
    f = s;//正确 
    s = f;//错误 
  
    father *pf = new son;//正确 
    son *ps = new father;//错误 
  
    father &rf = s;//正确
    son &rs = f;//错误 
    return 0; 
} 
```

##### 继承方式对基类成员被继承后的访问属性的影响

|      | 公有成员 | 保护成员 | 私有成员 |
| ---- | :--: | :--: | :--: |
| 公有继承 |  公有  |  保护  | 不可访问 |
| 保护继承 |  保护  |  保护  | 不可访问 |
| 私有继承 |  私有  |  私有  | 不可访问 |

##### 基类成员的访问属性对被访问权限的影响

|         | 公有成员 | 保护成员 | 私有成员 |
| ------- | :--: | :--: | :--: |
| 基类成员函数  | 可以访问 | 可以访问 | 可以访问 |
| 基类对象    | 可以访问 | 不可访问 | 不可访问 |
| 派生类成员函数 | 可以访问 | 可以访问 | 不可访问 |
| 派生类对象   | 可以访问 | 不可访问 | 不可访问 |

当所有成员都变成不可访问时，再往下派生就没有意义了

#### 派生类的构造函数与析构函数调用顺序
##### 单一继承
构造派生类对象时，先执行基类的构造函数，再执行派生类的构造函数，析构反之

```c++
class father
{
public: 
    father(){cout<<"father construct"<<endl;}
    ~father(){cout<<"father delete"<<endl;}
};
class son : public father
{
public:
    son(){cout<<"son construct"<<endl;}
    ~son(){cout<<"son delete"<<endl;}
};
int main()
{
    son s;
    return 0;
}
```
输出：

father construct

son construct

son delete

father delete

##### 多重继承
如果是多重继承，仍然是先执行基类的构造函数，再执行派生类的构造函数

调用基类构造函数的顺序与定义基类的顺序相同，

析构反之

```c++
class father
{
public:
    father(){cout<<"father construct"<<endl;}
    ~father(){cout<<"father delete"<<endl;}
};
class mother
{
public:
    mother(){cout<<"mother construct"<<endl;}
    ~mother(){cout<<"mother delete"<<endl;}
};
class son : public father, public mother
{
public:
    son(){cout<<"son construct"<<endl;}
    ~son(){cout<<"son delete"<<endl;}
};
int main()
{
    son s;
    return 0;
}
```
输出：

father construct

mother construct

son construct

son delete

mother delete

father delete

##### 构造函数的执行效率
利用基类的构造函数构造派生类，执行效率更高

```c++
class father
{
    int x;
public:
    father(int a):x(a){cout<<"father construct:"<<x<<endl;}
};
class son : public father
{
    int y;
public:
    son(int a, int b):father(a), y(b){cout<<"son construct:"<<y<<endl;}
};
int main()
{
    son s(1, 2);
    return 0;
}
```

输出：

father construct:1

son construct:2


#### 多重继承

##### 多重继续的二义性
多重继承的二义性是指派生类的多个基类具有相同名字的成员，编译器无法确定派生类所要使用的是哪一个。

造成这种情况出现通常的原因是：派生类的两个基类都继承于同一个祖先，那么祖先所拥有的成员这两个基类都有，这样就出现了上述的情况。如图
![](http://hi.csdn.net/attachment/201201/17/0_1326786263XRpI.gif)
假如A有Test()，则B和C都有Test()，于是D产生了二义性

##### 编译器的策略
编译器通常都是从离自己最近的目录树向上搜索的

假如把派生类的继承关系看作是一棵树，派生类是树的根结点，派生类的基类是根结点的孩子结点，依此类推

那么当派生类遇到多重继承的二义性问题时，编译器会从根结点向下搜索。遇到了离根结点最近的结点的成员作为派生的默认继承的成员。如果有多个结点都实现了这一成员且离根结点距离相同，编译器就会报错，这时需要通过显式的方式来指定。

```c++
class A
{
public:
    void Test(){cout<<"A"<<endl;}  
};
class B : public A
{
public:
    void Test(){cout<<"B"<<endl;}
};
class C : public A
{
public:
    void Test(){cout<<"C"<<endl;}
};
class D : public B, public C
{
};
int main()
{
    D d;
    d.Test();      //错误
    d.A::Test();   //正确，输出：A
    d.B::Test();   //正确，输出：B
    d.C::Test();   //正确，输出：C
    return 0;
}
```
##### 访问基类的成员
派生类的成员覆盖了基类的同名成员，并不代表基类的成员消失了，只是不能直接访问

```c++
class A  
{  
public:  
    void Test(){cout<<"A"<<endl;}  
};  
class B  
{  
public:  
    void Test(){cout<<"B"<<endl;}  
};  
class C : public A, public B  
{  
    void Test(){cout<<"C"<<endl;}  
};  
int main()  
{  
    C c;             
    c.Test();      //正确，输出：C  
    c.A::Test();   //正确，输出：A  
    c.B::Test();   //正确，输出：B  
    return 0;  
}  
```
##### 多重继承与单一继承在派生类访问基类方式上的区别
 - 对于单一继承，子类能否访问父类的父类，只与继承的方式有关

 - 对于多重继承，子类不能直接访问父类的父类。
 
##### 用virtual来避免二义性。
```c++
class B : virtual public A.
```
#### 继承与包含

一个类的成员变量列表中包含另一个类的对象，叫做包含（包容）。

包含和继承都能使一个类使用另一个类的成员，但它们的适用场合和目的不同
 
 - 包含：

1）使程序看上去更清晰易懂

2）不存在继承带来的问题

3）可以包括另一个类的多个对象

 - 私有继承：

1）可以访问基类的保护成员

2）可以重定义虚函数，实现多态
