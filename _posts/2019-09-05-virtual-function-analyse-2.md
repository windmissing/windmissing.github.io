---
layout: post
title:  "virtual关键字在子类"
category: [编程语言]
tags: [C++, virtual]
---

# 运行结果是什么？

![](\images\2019\10.png)

```c++
father *pf = new father();
pf->f();
delete pf;
father *ps = new son();
ps->f();
delete ps;
son *ps1 = new son();
ps1->f();
delete ps1;
son *pss = new sonson();
pss->f();
delete pss;
```

<!-- more -->

# 运行结果

```
father::f()
father::f()
son::f()
sonson::f()
```

id  | 指针名  | 指针的类型 | 实际的类型 | 运行结果 | 解释
--|---|---|---|---|---
1  | pf  | father  | father  | father::f()  |  
2  | ps  | father  | son  | father::f()  | 实际调用的是指针的类型的函数，说明没有多态
3  | ps1  | son  | son  | son::f()  |  
4  | pss  | son  | sonson  | sonson::f()  | 实际调用的是对象的类型的函数，说明有多态的效果

# 解释与结论

## 构造对象时

构造对象时，先构造基类部分，基类的f()没有带有关键字virtual，因此vtable是空的。

> vtable是空的

再构造派生类部分时，因为发现f()带有关键字virtual，于是把f()和它的地址加到vtable中。

> vtable中f()的地址：son::f()

如果要创建的是sonson类型的对象，到这一步就结束了。

如果要创建的是sonson类型的对象，还会构造sonson部分，sonson::f()虽然没带关键字virtual，还是会认为它是virtual的，并更新vtable。

> vtable中f()的地址：sonson::f()

## case 2

case 2创建的是son类型的对象，所以它的vtable是这样的：

> son类型对象的vtable中f()的地址：son::f()  

case 2是以`father *`的指针来调用f()的。所以会先判断father::f()是不是一个虚函数。

本例中，由于father::f()没有带有关键字virtual，所以**认为father::f()不是虚函数**，因此也**不会去查vtable**，直接调用father::f()

## case 3

与case 2不同的是，case 3是以`son *`的指针来调用f()的。于是先判断son::f()是不是一个虚函数。

本例中，由于son::f()带有关键字virtual，是个虚函数，查表vtable，得到f()真正的地址son::f()。


## case 4

case 4创建是sonson类型的对象，所以它的vtable是这样的：

> sonson类型对象的vtable中f()的地址：sonson::f()  

case 4是以`son *`的指针来调用f()的。所以会先判断son::f()是不是一个虚函数。

本例中，由于son::f()带有关键字virtual，是个虚函数，查表vtable，得到f()真正的地址sonson::f()。

结论：

1. 如果virtual只写在派生类中，而没有写在基类中，则不会有多态的效果

2. 如果在某一层的派生类中加了virtual标签，那么从这一层开始以后的每一层，这个函数都会有多态的效果。

# 其它测试

[virtual关键字在父类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-1.html)

[析构函数的virtual在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-3.html)

[间接调用虚函数](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-4.html)

# 完整代码

```c++
#include <iostream>
using namespace std;

class father
{
public:
  void f()
  {
    cout<<"father::f()"<<endl;
  }
};

class son : public father
{
public:
  virtual void f()
  {
    cout<<"son::f()"<<endl;
  }
};

class sonson : public son
{
public:
  void f()
  {
    cout<<"sonson::f()"<<endl;
  }
};

int main()
{
    father *pf = new father();
    pf->f();
    delete pf;
    father *ps = new son();
    ps->f();
    delete ps;
    son *ps1 = new son();
    ps1->f();
    delete ps1;
    son *pss = new sonson();
    pss->f();
    delete pss;
    return 0;
}
```
