---
layout: post 
title:  "多态总结"
categories: 编程语言
tags: [c++, 类, 多态]
---

#### 一、多态

##### 1.多态分为两种

（1）编译时的多态：通过函数重载实现

（2）运行时的多态，通过虚函数实现，即动态联编

##### 2.继承不是多态

```c++
class father  
{  
public:  
    virtual void run(){cout<<"父跑"<<endl;}  
    void jump(){cout<<"父跳"<<endl;}  
};  
class son:public father  
{  
public:  
    void run(){cout<<"子跑"<<endl;}  
    void jump(){cout<<"子跳"<<endl;}  
};  
int main()  
{  
    father *pf = new son;  
    pf->run();  
    pf->jump();  
    delete p;  
    return 0;  
}  
```

#### 二、重载

#####1.操作符重载

见[操作符重载总结](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2012-01/operator-overloading-in-cpp.html)

##### 2.函数重载

###### 1.令B公有继承于A，以下函数都是公有

（1）A有几个Test()的重载，B没有Test()

则：b.Test()调用A相应的重载

（2）A有几个Test()的重载，B有Test()的重载1，没有Test()的重载2

则：b.hello()重载1，则调用B的相应重载

        b.hello()重载2，则出错

        b.A::hello()，则调用A的相应重载

###### 2.void Test(int i)const与void Test(int i)是两个不同的函数，可以同时存在这两个重载

##### 3.多重继承中的重载

见[基类与派生类、继承关系总结](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2015-12/supperclass-inheritance.html)

#### 三、动态联编

##### 1.什么是动态联编

######（1）联编：将一个调用函数者联结上正确的被调用者

静态联编：在编译时联编，在执行时不联编

动态联编：在编译时不联编，在执行时联编

######（2）动态联编开销大

##### 2.动态联编的使用方法

######（1）多态的正确使用方法：

```c++
class father  
{  
public:  
    virtual void Test(){cout<<"父"<<endl;}  
};  
class son:public father  
{  
public:  
    void Test(){cout<<"子"<<endl;}  
};  
class daughter:public father  
{  
public:  
    void Test(){cout<<"女"<<endl;}  
};  
  
void one(father one){one.Test();}  
void two(father *two){two->Test();}  
void three(father &three){three.Test();}  
  
int main()  
{  
    int n;  
    father *ps = new son;one(*ps);delete ps;              //1  
    father *pd = new daughter;two(pd);delete pd;          //2  
    father *pf = new father();three(*pf);delete pf;       //3  
    return 0;  
}  
```

输出：

```
父
女
父
```

解释：

1.由于不是以指针或引用的方式调用，即使是virtual函数，也无法实现多态

2.以指针的方式调用虚函数，因此是多态

3.以引用的方式调用虚函数，因此是多态

######（2）只有在使用指针或引用时，才能实现动态联编，错误的动态联编如下：

```c++
class A  
{  
    int x;  
public:  
    A(){x = 1;cout<<"A"<<endl;}  
    void get(){cout<<x<<endl;}  
};  
class B: public A  
{  
    int x;  
public:  
    B(){x = 2;cout<<"B"<<endl;}  
    void get(){cout<<x<<endl;}  
};  
class C : public A  
{  
    int x;  
public:  
    C(){x = 3;cout<<"C"<<endl;}  
    void get(){cout<<x<<endl;}  
};  
int main()  
{  
    A p;  
    int choice;  
    while(cin>>choice)  
    {  
        switch(choice)  
        {  
        case 1:p = A();break;  
        case 2:p = B();break;  
        case 3:p = C();break;  
        }  
        p.get();  
    }  
    return 0;  
}  
```


输出：A

输入：1

输出：A 1

输入：2

输出：A B 1

输入：3

输出：A C 1

不管输入什么，p.get();时都输出1，可见没有实现多态

######（3）在虚函数中使用成员限定名，可以强制解除动态联编

```c++
class father  
{  
public:  
    virtual void Test(){cout<<"父"<<endl;}  
};  
class son:public father  
{  
public:  
    void Test(){cout<<"子"<<endl;}  
};  
  
int main()  
{  
    father *pf = new son;  
    pf->Test();  
    pf->father::Test();  
    return 0;  
}  
```

输出：

```
子
父
```

######（4）直接调用非虚函数不会出现多态。

虚函数调用非虚函数，全部都能实现多态

######（5）基类的一个函数为虚函数，其派生类的这个函数也是虚函数

##### 3.动态联编举例

```c++
father *pf = new son;  
//先构造父，再构造子，但pf指向的是父的对象。因此pf只能调用father的成员，不能调用son的成员  
delete pf;  
//只析构父，不析构子，造成内存泄漏  
```

解决方法：

1）pf强制转换为son类，这种方法不好，容易出错

2）将father的析构函数定义为virtual，以实现多态
