---
layout: post 
title:  "函数返回值总结"
categories: 编程语言
tags: [c++]
---

##### 例1：

```c++
class A  
{  
    int x;  
public:  
    A(int i):x(i){}  
    int get(){return x;}  
};  
A& func()  
{  
    A a(23);  
    return a;  
}  
int main()  
{  
    A &r = func();  
    cout<<r.get()<<endl;  
    return 0;  
}  
```

输出：1245000

解释：r被初始化为返回值的别名。由于是按引用返回，返回值就是a的别名。因此，r就是a的别名。

a是一个局部变量，func()结束后，a消失了。r成了一个空的引用。

因此，输出的是上个随机值。
 
##### 例2：

```c++
class A  
{  
    int x;  
public:  
    A(int i):x(i){cout<<"construct     "<<this<<endl;}  
    A(const A& a){x = a.x;cout<<"copy     "<<this<<endl;}  
    ~A(){cout<<"delete     "<<this<<endl;}  
    int get(){return x;}  
};  
A func()  
{  
    A a(23);  
    return a;  
}  
int main()  
{  
    A &r = func();  
    cout<<r.get()<<endl;  
    return 0;  
}  
```

输出：

```
construct     0012FEC8
copy     0012FF34
delete     0012FEC8
23
delete     0012FF34
```

解释：r被初始化为返回值的别名，返回值是a的副本。

虽然返回值不是局部变量，但是正常情况下，返回值应该在func()后，下一句执行之前析构，

既然引用的对象还是会消失，为什么能正常输出结果呢？这里提出一个概念：

如果引用的是一个临时变量，那么这么个临时变量的生存期会不小于这个引用的生存期。因此，返回值（即a的副本）到r的作用域结束时才析构。

r是返回值的引用，不是原a的引用
 
##### 例3：

这个例子是为了和例2做对照，用于说明正常情况下，返回值是在函数结束后，下一句执行前，析构的。

```c++
class A  
{  
    int x;  
public:  
    A(int i):x(i){cout<<"construct     "<<this<<endl;}  
    A(const A& a){x = a.x;cout<<"copy     "<<this<<endl;}  
    ~A(){cout<<"delete     "<<this<<endl;}  
    int get(){return x;}  
};  
A func()  
{  
    A a(23);  
    return a;  
}  
int main()  
{  
    func();  
    cout<<"Test"<<endl;  
    return 0;  
}  
```

输出：

```
construct     0012FEDC     //a构造
copy     0012FF44               //返回值的构造
delete     0012FEDC          //a的析构
delete     0012FF44            //返回值的析构
Test                                      //先析构再执行输出，证明了上述结论
```

##### 例4.本例同样与例2做对比

```c++
class A  
{  
    int x;  
public:  
    A(int i):x(i){cout<<"construct     "<<this<<endl;}  
    A(const A& a){x = a.x;cout<<"copy     "<<this<<endl;}  
    ~A(){cout<<"delete     "<<this<<endl;}  
    int get(){return x;}  
};  
A func()  
{  
    A a(23);  
    return a;  
}  
int main()  
{  
    A *r = &func();  
    cout<<r->get()<<endl;  
    return 0;  
}  
```

输出：

```
construct     0012FED4                //a的构造
copy     0012FF40                         //返回值的构造
delete     0012FED4                     //a的析构
delete     0012FF40                      //返回值的析构
23                                                    //其实些时r指向的对象已经析构了
```

解释：

&func()的意思是对func()的返回值取地址。因此，r指向的对象是返回值（即a的副本）。

和例2不同的是，引用可以延长返回的寿命，而指针不行。

为什么析构了还能输出正确的值呢？

因为析构函数析构某个对象后，只是告诉编译器这个内存不在被对象独占了。你可以访问它，别的对象也可以访问它。

在该内存没有被别的数据覆盖之前，原数据都没有被删除。
 
##### 例5.

```c++
class A  
{  
    int x;  
public:  
    A(int i):x(i){cout<<"construct     "<<this<<endl;}  
    A(const A& a){x = a.x;cout<<"copy     "<<this<<endl;}  
    ~A(){cout<<"delete     "<<this<<endl;}  
    int get(){return x;}  
};  
A func()  
{  
    A *p = new A(23);  
    return *p;  
}  
int main()  
{  
    A &r = func();  
    cout<<r.get()<<endl;  
    return 0;  
}  
```

输出：

```
construct     00251DF8  //a的构造
copy     0012FF34       //返回值的构造
23
delete     0012FF34     //返回值的析构。引用延长了返回值的寿命
```

解释：

如果读懂了例2，本题的输出很好理解。

构造的新对象无法析构，造成内存泄漏

 ##### 例6.

```c++
class A  
{  
    int x;  
public:  
    A(int i):x(i){cout<<"construct     "<<this<<endl;}  
    A(const A& a){x = a.x;cout<<"copy     "<<this<<endl;}  
    ~A(){cout<<"delete     "<<this<<endl;}  
    int get(){return x;}  
};  
A& func()  
{  
    A *p = new A(23);  
    return *p;  
}  
int main()  
{  
    A &r = func();  
    cout<<r.get()<<endl;  
    A *pa = &r;  
    delete pa;  
    cout<<r.get()<<endl;  
    return 0;  
}  
```

输出：

```
construct     004B1DF8
23
delete     004B1DF8
-572662307
```

解释：

由于是按值返回，r是p所指向的未命名空间的别名。

虽然指针p已经消失了，但是是又给了它一个新的指针，即pa

L17和L19的&r不同。L17是为了说明r是一个别名。L19表示对r取地址

因此，r是未命名空间的名字，pa是指向r的指针。

释放了pa，r也就成了空引用

##### 例7：

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
};  
A& func(A &a)  
{  
    a.set(99);  
    return a;  
}  
int main()  
{  
    A *p = new A(23);  
    cout<<p->get()<<endl;  
    func(*p);  
    cout<<p->get()<<endl;  
    delete p;  
    return 0;  
}  
```

输出：

```
construct     00701DF8
23
99
delete     00701DF8
```

解释：

按引用传参，p所指向的对象=r所引用的对象=返回值

返回值其实没有用，没有返回值，结果也是一样的

##### 8.当函数按值返回在该函数中创建的栈中对象时，会把该对象复制到执行调用该函数的作用域中。

复制对象的工作结束后，接着会调用析构函数销毁复制的对象。

如果用指针接收，函数返回后，对象和它的复本都被析构，副本的内存地址返回给指针，在该地址的数据没有被覆盖前，指针仍可访问该数据

当按地址返回一个堆中对象，并用引用接收时，需要一个指针来存储引用的地址，这个指针用于删除对象
