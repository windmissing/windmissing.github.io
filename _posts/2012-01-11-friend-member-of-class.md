---
layout: post 
title:  "友元friend总结"
categories: 编程语言
tags: [c++, 类, 友元]
---

##### 1.关键字friend只出现在类定义的内部（这点与const不同）

##### 2.友元是授予友元关系的那个类的成员

##### 3.定义类B为类A的友元，B可以访问A的私有成员

例1：    

```c++
/*要注意友元的使用顺序，声明B->定义A->定义B*/
class B;/*只声明而未定义的类称为不完全类，可用定义类型，不能用于定义对象*/    
class A    
{    
private:    
    int x;    
public:    
    A(int i):x(i){}    
    friend B;/*将B声明为友元，B可以访问A的private*/    
};    
class B    
{    
private:    
    int x;    
public:    
    void Test(A a)    
    {    
        x = a.x;    
    }    
    int Get(){return x;}    
};    
int main()    
{    
    A a(3);    
    B b;    
    b.Test(a);    
    //输出3.说明Test()函数赋值成功，也说明Test()中的x是B的成员，从而得知，Test()是属于B的     
    cout<<b.Get()<<endl;    
    return 0;    
}    
```

##### 4.定义类B的Test()函数为类A的友元，B的Test()函数可以访问A的私有成员


例2：

```c++
/*要注意友元的使用顺序， 
声明A->定义B(要作为友元的那个函数只声明不定义)->定义A->定义B的函数*/  
class A;/*只声明而未定义的类称为不完全类，可用定义类型，不能用于定义对象*/  
class B  
{  
private:  
    int x;  
public:  
    void Test(A a);  
    int Get(){return x;}  
};  
class A  
{  
private:  
    int x;  
public:  
    A(int i):x(i){}  
    friend void B::Test(A a);/*将B的Test()声明为友元，B的Test()可以访问A的private*/  
};  
void B::Test(A a){x = a.x;}  
int main()  
{  
    A a(3);  
    B b;  
    b.Test(a);  
    //输出3.说明Test()函数赋值成功，也说明Test()中的x是B的成员，从而得知，Test()是属于B的  
    cout<<b.Get()<<endl;  
    return 0;  
}  
```

##### 5.友元声明将已命名的类或非成员函数引入到外围作用域中。此外，友元函数可以在类的内部定义，该函数的作用域扩展到包围该类定义的作用域。

例3：

```c++
/*本来A和f()的作用域只限于在它们声明之后。 
但是因为类B提前引入了它们，使得它们的作用域与类B的作用域相同*/  
class B  
{  
    friend class A;  
    friend void f();  
};  
class C  
{  
public:  
    A *p;  
    void g(){return f();}  
};  
class A;  
void f()  
{  
    cout<<"1"<<endl;  
}  
int main()  
{  
    C c;  
    c.g();//输入1  
    return 0;  
}  
```

##### 6.友元函数的重载函数，如果要成为友元，必须要用friend声明。
例4：

```c++
class A;/*只声明而未定义的类称为不完全类，可用定义类型，不能用于定义对象*/  
class B  
{  
private:  
    int x;  
public:  
    void Test(A a);  
    void Test(A a1, A a2);  
    void Test(A a1, A a2, A a3);  
    int Get(){return x;}  
};  
class A  
{  
private:  
    int x;  
public:  
    A(int i):x(i){}  
    friend void B::Test(A a);/*将B的Test()声明为友元，B的Test()可以访问A的private*/  
    friend void B::Test(A a1, A a2);  
};  
//正确，因为已经被定义为友元  
void B::Test(A a){x = a.x;}  
//正确，因为已经被定义为友元  
void B::Test(A a1, A a2){x = a1.x + a2.x;}  
//错误，不能因为Test(A a)是友元，就认为它的重载也是友元  
void B::Test(A a1, A a2, A a3){x = a1.x + a2.x + a3.x;}  
```
