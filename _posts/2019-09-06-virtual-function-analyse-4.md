---
layout: post
title:  "间接调用虚函数"
category: [编程语言]
tags: [C++, 析构函数]
---

# 运行结果是什么？

![](\images\2019\12.png)

```c++
father *pf = new father();
pf->A();
pf->B();
delete pf;

father *ps = new son();
ps->A();
ps->B();
delete ps;

son *ps1 = new son();
ps1->A();
ps1->B();
delete ps1;

son *pss = new sonson();
pss->A();
pss->B();
delete pss;
```

<!-- more -->

# 运行结果

```
this is father::B()
this is father::B()
this is father::B()
this is father::B()
this is father::B()
this is son::B()
this is father::B()
this is sonson::B()
```

id  | 指针名  | 指针的类型 | 实际的类型 | 运行结果 | 解释
--|---|---|---|---|---
1  | pf  | father  | father  | this is father::B()<br>this is father::B()  |  
2  | ps  | father  | son  | this is father::B()<br>this is father::B()  | 由[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)可知此处不会有多态
3  | ps1  | son  | son  | this is father::B()<br>this is son::B()  | 此例中，指针的类型和对象的类型都是son，为什么最后调用的是fathher::B()?
4  | pss  | son  | sonson  | this is father::B()<br>this is sonson::B()  | 由[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)可知此处应该有多态效果，为什么最后调用的还是fathher::B()?

# 解释与结论

## 构造对象时

本文中的virtual写法与[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)，最后每个对象的生成的vtable如下：

> father类型对象的vtable中B()的地址：father::B()  
> son类型对象的vtable中B()的地址：son::B()  
> sonson类型对象的vtable中B()的地址：sonson::B()

## case 3

执行`ps->A();`时，虽然ps的类型和它指向的对象的类型都是son，但son本身没有son::A()函数，所以会调用father::A()。

我们都知道，类里有一个隐藏的指针this。所以father::A()实际上是这样的。

```c++
void father::A(){ father::this->B(); }
```

可见实际上是以father类型的指针来调用B()。这就和[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)中的case 2很类似了。

由于father::B()不是虚函数，所以没有查表，而是直接调用了father::B()。

## case 4

case 4和case 3的原因类型，不管ps1和pss的指针和对象是什么类型，实际上都是以father类型的指针来调用B()的。

# 其它测试

[virtual关键字在父类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-1.html)

[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)

[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)

# 完整代码

```c++
#include <iostream>
using namespace std;

class father
{
public:
  void A()  { B(); }
  void B()
  {
    cout<<"this is father::B()"<<endl;
  }
};

class son : public father
{
public:
  virtual void B()
  {
    cout<<"this is son::B()"<<endl;
  }
};

class sonson : public son
{
public:
  void B()
  {
    cout<<"this is sonson::B()"<<endl;
  }
};

int main()
{
  father *pf = new father();
  pf->A();
  pf->B();
  delete pf;
  father *ps = new son();
  ps->A();
  ps->B();
  delete ps;
  son *ps1 = new son();
  ps1->A();
  ps1->B();
  delete ps1;
  son *pss = new sonson();
  pss->A();
  pss->B();
  delete pss;
  return 0;
}
```
