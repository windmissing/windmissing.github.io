---
layout: post 
title:  "操作符重载总结"
categories: 编程语言
tags: [c++, 类, 重载]
---

#### 一、重载的基本规则

##### 1.重载操作符的形参数目应与操作符的操作数数目相同。

重载操作符作为类的成员函数，隐含一个*this作为函数的第一个函数

##### 2.重载后，优先级、结合性、操作数目不变。但是不能保证求值顺序

求值顺序是指：在优先级、结合性相同的情况下，先求哪个

##### 3.不能创建新的操作符

##### 4.重载操作符必须至少有一个类类型或枚举类型

##### 5.不可重载的操作符：（1）：：               （2）.                     （3）？：                  （4）#           

既可做一元又可做二元的操作符：（1）+                    （2）-                   （3）*                    （4）&

可使用默认实参的操作符：（1）()
 
##### 6.操作符作为非成员函数重载时通常要声明该类的友元。除非该类的数据成员是公有的

##### 7.在某些特殊的情况下，赋值运算符必须先释放一些旧值，然后才能根据新值的类型分配新的数据。此时，自复制会出错

##### 8.operator关键字配合要转换的类型，构成了转换运算符的重载函数。该函数没有返回值，但可以在函数中返回一个转换后的值
 
#### 2.[]操作符重载举例

1）重载后的[]操作符仅限本类的对象使用

2）必须重载为非static成员

3）不能重载为友元函数

4）重载好的优点：不用将数组长度定义为常量；可避免越界

```c++
char& operator[](int i)  
{  
    if(i >= 0 && i < length)  
        return size[i];  
    else  
    {  
        cout<<"error"<<endl;  
        return size[length-1];  
    }  
}  
```

#### 3.++操作符前置自加与后置自加重载举例

1）前置自加按引用返回。

后置自加按值返回，且返回的是临时对象。

2）后置自加中的参数没有实际意义，只是为了区分前置

3）很显然前置自加效率更高，尽量用前置

```c++
class A  
{  
    int x;  
public:  
    A(int i):x(i){cout<<"construct     "<<this<<endl;}  
    A(const A& a){x = a.x;cout<<"copy     "<<this<<endl;}  
    ~A(){cout<<"delete     "<<this<<endl;}  
    int get(){return x;}  
    void set(int i){x = i;}  
    //前置自加  
    const A& operator++()  
    {  
        ++x;  
        return *this;  
    }  
    //后置自加  
    const A operator++(int o)  
    {  
        A temp(*this);  
        ++x;  
        return temp;  
    }  
};  

int main()  
{  
    A a(1);  
    cout<<a.get()<<endl;  
    A b = ++a;  
    cout<<b.get()<<endl;  
    cout<<a.get()<<endl;  
    b = a++;  
    cout<<b.get()<<endl;  
    cout<<a.get()<<endl;  
    return 0;  
}  
```

输出：

```
construct     0012FF38
1
copy     0012FF34
2
2
copy     0012FEB8
copy     0012FF30
delete     0012FEB8
delete     0012FF30
2
3
delete     0012FF34
delete     0012FF38
```

#### 4.输入输出运算符重载举例

##### 1.输出运算符的重载

```c++
ostream& operator<<(ostream& s, const A& a)  
{  
    s<<a.rx<<' '<<a.ry<<endl;  
    return s;  
}  
```

##### 2.输入运算符重载

```c++
istream& operator>>(istream& s, A& a)  
{  
    s>>a.rx>>a.ry;  
    return s;  
}  
```

##### 3.根据运算符左边对象的类型判断是流运算符还是移位运算符
 
##### 4.ostream类没有公有的复制构造函数，因此该函数无法调用该类的复制构造函数复制对象，必须按引用方式接受ostream的对象，并按引用方式返回ostream对象
 
##### 5.iostream是多重继承的一个应用
 
##### 6.流运算符不能重载为一个类的成员函数，因为它包含其它的对象。只能将其重载为友元函数
 
##### 7.例：

```c++
int a = 3;
cout << ++a << a++ <<endl;
```
输出：53

解释：

当一个函数传进来的参数不是一个简单的变量，而是一个有运算的表达式时，要把表达式求值，再把值入栈。

求值的顺序是从右到左，所以先求a++

1）执行a++，a=4，返回3

2）执行++a，a=5，返回5

3）执行cout<<返回值（5）<<返回值（3）<<endl;
