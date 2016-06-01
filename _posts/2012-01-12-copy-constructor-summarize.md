---
layout: post 
title:  "复制构造函数总结"
categories: 编程语言
tags: [c++, 类, 复制构造函数]
---

#### 一、什么情况下会调用复制构造函数？

##### 1.用同一类型的对象来初始化另一对象

例1：

```c++
class A  
{  
public:  
    A(){}  
    A(const A& a){cout<<"copy"<<endl;}  
};  
int main()  
{  
    A a, c;  
    A b = a;//显式复制构造函数（1）  
    c = a;//赋值函数（2）  
    return 0;  
}  
```
输出：

```
copy
```
本例要注意的是（1）和（2）的区别：

复制构造函数也是构造函数的一种。只要是构造函数，就要开辟空间。

（1）在初始化的同时还要完成开辟空间的任务，所以在复制构造函数

（2）在L9已经开辟了空间（变通构造函数），这里只是赋值

##### 2.**按值**传参数或**按值**传返回值

例2：

```c++
class A  
{  
public:  
    A(){}  
    A(const A& a){cout<<"copy"<<endl;}  
};  
A Test(A a)  
{  
    return a;  
}  
int main()  
{  
    A a;  
    Test(a);  
    return 0;  
}  
```
输出：

```
copy
copy
```
`Test(a)`调用了两次构造函数，一次传参，一次是返回值

##### 3.初始化顺序容器中的元素,顺序容包括vector、list、deque

例3：

```c++
class A  
{  
    int x;  
public:  
    A(int i):x(i){cout<<"construct "<<i<<endl;}  
    A(const A& a){cout<<"copy"<<endl;}  
};  
int main()  
{  
    list<A> a(10, 5);  
    return 0;  
}  
```
输出：

```
construct 5
copy
copy
copy
copy
copy
copy
copy
copy
copy
copy
```
先构造一个临时对象，再把它依次复制到容器中

##### 4.根据元素初始化列表初始化数组元素

例：

```c++
class A  
{  
    int x;  
public:  
    A(){cout<<"construct "<<endl;}  
    A(int i):x(i){cout<<"construct "<<i<<endl;}  
    A(const A& a){cout<<"copy"<<endl;}  
};  
int main()  
{  
    cout<<"****Test1****"<<endl;  
    A s1[5];  
    cout<<"****Test2****"<<endl;  
    A s2[5] = {1, 2, 3, 4, 5};  
    cout<<"****Test3****"<<endl;  
    A a(1), b(2), c(3), d(4), e(5);  
    A s[5] = {a, b, c, d, e};  
    return 0;  
}  
```

输出结果： 

```c++
****Test1****
construct
construct
construct
construct
construct
****Test2****
construct 1
construct 2
construct 3
construct 4
construct 5
****Test3****
construct 1
construct 2
construct 3
construct 4
construct 5
copy
copy
copy
copy
copy
```

分析结果：

Test1：构造

Test2：构造（隐式类型转换）

Test3：L16是构造L17是复制

#### 默认的复制构造函数

##### 是否由系统提供

如果定义了自己的构造函数，系统还是会提供一个默认的复制构造函数

如果定义了自己的复制构造函数，系统不会提供一个默认的复制构造函数

##### 默认构造函数做什么？

复制构造函数的行为：依次复制每一个非static成员，只是复制内容，称为浅层复制。

如果类中有指针成员，浅层复制会出错。需要定义自己的复制构造函数，使用深层复制。

##### 复制构造函数的特殊用法

如果要禁止复制，可以复制构造函数声明为私有

如果连友元和成员也要禁止复制，可声明为私有，且只声明不定义。

例如iostream类，iostream类禁止复制，它的复制构造函数是私有的
