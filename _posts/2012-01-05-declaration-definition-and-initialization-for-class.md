---
layout: post 
title:  "类的声明、定义与初始化"
categories: 编程语言
tags: [c++, 类]
---

#### 一、类的声明

##### 1.类的声明和定义

```c++
class Mat  
{  
public:  
    __int64 s[MAX][MAX];  
    int sizei,sizej;  
public:  
    Mat(int a = MAX, int b = MAX, int type = 0);  
    void clear(int type = 0);  
    void ReSize(int a = MAX, int b = MAX, int type = 0);  
    void Add(const Mat& B);  
    void Multiply(const Mat &B);  
    void Er_work(int n);  
    void solve(int p) ;  
};  
```
##### 2.不完全类

只声明而尚未定义的类称为不完全类

不完全类只能用于定义指针、引用、参数类型、返回值类型，不能定义对象

```c++
class Mat; //求定义的类  
Mat Test(Mat& B);//正确  
Mat *pMat;//正确  
Mat mt;//错误，如果在任何位置（即使是在这句话的后面）定义了这个类，这句就是正确的  
```

#### 二、类的定义过程中的常用关键字

##### 1.typedef:

类可以定义自己的局部类型的名字,局部类型名和原类型名可以混用

定义方法：typedef 原类型名 局部类型名

例：

```c++
class Mat  
{  
public:  
    typedef int myType  
    myType s[MAX][MAX];  
    Mat(myType a = MAX, myType b = MAX, myType type = 0);  
};  
Mat::Mat(int a, int b, int type)  
    :sizei(a),sizej(b){  
        memset(s, 0, sizeof(s));  
}  
```

##### 2.const：（难点，易错点）

见[const总结](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2016-01/const-summarize.html)

const成员函数返回的引用，也是const

```c++
#include<iostream>  
using namespace std;  
class A  
{  
public:  
    int x;  
    void set(int x){this->x = x;}  
    /*const成员函数返回的引用也是const &a, 如果把A&前面的const去掉会出错。 
    因为返回的是一个const的对象，返回类型却不是const。返回的内容和返回的类型不符*/  
    const A& Test1()const  
    {  
        /*错误。这是const成员函数的特点*/  
        x = 2;  
        /*不限于*this。不管返回的是什么，哪怕是一个定义为非const的对象，结果也是一样的*/  
        return *this;  
    }  
};  
int main()  
{  
    A a, b;  
    
    /*正确，虽然返回的是一个const，却用另一个非const来接收*/  
    b = a.Test1();  
    /*错误，既然是别名，那么别名的类型要与原来的类型相同*/  
    A &c = a.Test1();  
    //正确虽然在a.Test1()中a不能改变，但是这里已经出了这个成员函数的作用域  
    a.set(2);  

    //正确，b接收了a.Test1()返回的数据的内容，但是它不是const  
    b.set(2);  
    /*错误。a.Test1()表示一个没有名字的对象，这个对象是函数a.Test1()的返回值. 
    对象的值是a.Test1()返回的值，对象的类型是a.Test1()返回的类型（const A&），*/
    a.Test1().set(2);  
    
    return 0;  
}  
```

##### 3.mutable：

mutable将数据声明为可变数据成员。可变数据成员永远不能成为const,即使它是const对象的成员

例：

```c++
class A  
{  
public:  
    int x;  
    mutable int y;  
    A(int a, int b):x(a),y(b){}  
};  
int main()  
{  
    const A a(1,2);//const对象必须初始化  
    a.x = 3;//错误  
    a.y = 3;//正确  
    return 0;  
}  
```

##### 4.friend（重点）：

见[友元friend总结](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2012-01/friend-member-of-class.html)

##### 5.static（重点，难点，易错点）：

见类中使用[static总结](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2012-01/static-summarize.html)

#### 三.类的定义

##### 1.类内定义

不推荐。

##### 2.类外定义（重点）

如果成员函数在类外定义，则：

（1）成员名必须有 类名:: 来限定

（2）形参表和成员函数可以不限定

（3）函数返回类型，如果使用的是类定义的类型，则需要使用完全限定名

例：

```c++
class A  
{  
public:  
    typedef int myType;  
    int x;  
    myType y;  
    int Test1(int a);  
    myType Test2(myType a);  
};  
int A::Test1(int a)             //函数名Test1必须由A::来限定
{  
    x = a;                      //函数体中用到了类内的成员，不需要由A::限定
    return x;  
}  
A::myType A::Test2(myType a)    //返回值的类型用到了类内的类型，需要由A::来限定
{                               //参数的类型用到了类内的类型，需要由A::来限定
    y = a;  
    return y;  
}  
```

#### 三、类的初始化

##### 1.使用构造函数初始化

###### （1）在构造函数中为成员赋值

```c++
class A  
{  
    int x;  
public:  
    A(int i){x = i;cout<<"construct A "<<i<<endl;}  
    ~A(){cout<<"delete A "<<x<<endl;}  
};  
```

##### （2）使用初始化列表初始化

列表中初始化与在构造函数的函数体中赋初值的区别

```c++
class A  
{  
    int x;  
public:  
    A(int i):x(i){cout<<"construct A "<<i<<endl;}  
    ~A(){cout<<"delete A "<<x<<endl;}  
};  
```

##### (3)使用初始化列表和在构造函数中为成员赋值的区别

定义是指开辟空间，初始化是指给一个初值。

在初始化列表中初始化时，定义和初始化同时进行，因此初始化的顺序与初始化列表的顺序无关，只与声明成员的次序相同

在函数体上赋值时，已经定义好了，再赋值

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

###### （4）必须使用初始化列表的成员

有些成员必须构造函数初始化列表中初始化，不可以在构造函数的函数体中初始化，如const成员或引用类型的成员

例：

```c++
class A  
{  
    int x;  
public:  
    A(int i):x(i){}  
};  
class B  
{  
public:  
    int a;  
    const int b;  
    int &c;  
    A d;  
    //赋值  
    B(int i)  
    {  
        a = i;//正确  
        b = i;//错误，const不能被赋值  
        c = i;//错误，别名不能被赋值  
        d = i;//错误，已经开辟了空间，不能调用带一个参数的构造函数，也没有其它相应的函数  
    }  
    //初始化，这种做法效率较高,d(i)调用带一个参数的构造函数  
    A(int i):a(i),b(i),c(i)，d(i){}  
};  
```

##### 2.使用与初始化数组元素相同的方法初始化

对于没有定义构造函数并且全体数据成员均为public的类，可以采用与初始化数组元素相同的方式初始化成员，但这种方法**不提倡**

例：

```c++
class A  
{  
public:  
    int a;  
    char *b;  
};  
int main()  
{  
    A a = {1, "a+b"};  
    return 0;  
}  
```

##### 3.使用复制构造函数初始化

通过复制构造函数，通过一个对象初始化另一个对象，见[复制构造函数总结](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2012-01/copy-constructor-summarize.html)
