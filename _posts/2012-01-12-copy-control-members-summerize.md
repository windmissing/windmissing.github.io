---
layout: post 
title:  "复制控制成员总结"
categories: 编程语言
tags: [c++, 类, 复制控制成员]
---

##### 1.复制控制成员是指：复制构造函数、赋值操作符函数、析构函数

##### 2.关于复制构造函数，见：[复制构造函数总结](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2012-01/copy-constructor-summarize.html)

##### 3.如果没有自己的赋值操作符函数，编译器会提供一个。

赋值操作符也是依次复制每个非static成员，也是浅层复制。

赋值操作符与复制构造的区别，只是不用为对象开辟新空间。

##### 4.析构对象的顺序，是创建对象的逆序，也即声明次序的逆序

例：

```c++
class A  
{  
    int x;  
public:  
    A(int i){x = i;cout<<"construct A "<<i<<endl;}  
    ~A(){cout<<"delete A "<<x<<endl;}  
};  
class B  
{  
    A a;  
    A b;  
    A c;  
public:  
    B():c(3),b(2),a(1){cout<<"construct B"<<endl;}  
    ~B(){cout<<"delete B"<<endl;}  
};  
int main()  
{  
    B b;  
    return 0;  
}  
```

输出结果：

```
construct A 1
construct A 2
construct A 3
construct B
delete B
delete A 3
delete A 2
delete A 1
```

这里特意让初始化列表的顺序不同，可以看出构造与析构的顺序与初始化列表无关，只与声明顺序有关

##### 5.和其它函数不同的是，即使定义了自己的析构函数，还是会执行默认的析构函数

先运行自己的析构函数，再运行默认的析构函数

##### 6.在复制控制函数中，复制时只复制内容，这种复制称为浅层复制

比如复制指针，只复制指针中的地址，不复制指针指向的内容。

当类中有指针成员时，浅层复制会出错。需要定义自己的深层复制

如果需要定义自己的析构函数，就肯定需要定义自己的所有这也三个控制成员函数

##### 7.定义自己的控制成员函数

```c++
class A  
{  
    int val;  
    int *ptr;  
public:  
    /*构造函数 
    ptr(new int(p))：创建一个int，int的内容与p相同，ptr指向该int*/  
    A(const int &p, int i):ptr(new int(p)),val(i){}  
    /*复制构造函数 
    *orig.ptr：取指针orig.ptr指向的内容 
    ptr(new int(*orig.ptr))：创建一个int，int的内容与*orig.ptr相同，ptr指向该int*/  
    A(const A &orig):ptr(new int(*orig.ptr)),val(orig.val){}  
    /*赋值操作符不需要开辟空间*/  
    A& operator=(const A &orig)  
    {  
        /*是函数内容的意思 
        rig.ptr指向的内容赋给ptr指向的内容*/  
        *ptr = *orig.ptr;  
        val = orig.val;  
        return *this;  
    }  
    //析构函数  
    ~A(){delete ptr;}  
};  
```

需要注意的是，在本例中，this对象可以访问orig对象的私有成员。

对于私有的定义是这样的：只允许类的创建者(在这里是this)和该类的成员函数可以访问

我理解的可以访问是指可以访问创建者的私有成员。

为什么在本例中this对象可以访问orig对象的私有成员？求解释

##### 8.如果类中有指针成员，复制控制函数一定要自己写。

有时候，复制控制的应用不是很明显，容易被忽略。

所以发现类中有指针成员时，一定要仔细分析类的使用，不能忽视任意一处可能的复制控制的使用

最保险的方法就是，只要看到类中有指针成员，就自己写复制控制
