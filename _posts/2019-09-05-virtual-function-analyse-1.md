---
layout: post
title:  "virtual关键字在父类"
category: [编程语言]
tags: [C++, virtual]
---

# 运行结果是什么？

![](\images\2019\9.png)

```c++
father *pss1 = new sonson();
pss1->f();
delete pss1;
son *pss2 = new sonson();
pss2->f();
delete pss2;
sonson *pss3 = new sonson();
pss3->f();
delete pss3;
```

<!-- more -->

# 运行结果

```
sonson::f()
sonson::f()
sonson::f()
```

# 解释与结论

## 构造对象时

构造对象时，先构造基类部分，此时发现f()带有关键字virtual，就把f()的地址填入vtable中。

> vtable中f()的地址：father::f()

再构造派生类部分时，因为在构造基类时已经知道f()是个virtual了，（不管f()是否带关键字virtual），所以直接认为派生类的f()也是virtual的，按照virtual来处理f()，即“把派生类的f()的地址更新到vtable中”。

> son类型对象的vtable中f()的地址：son::f()  
> sonson类型对象的vtable中f()的地址：sonson::f()

这样这个对象的vtable表里f()地址永远都是最后更新的那一层的f()的地址。如果对象是son类型的，最后构造的son部分，vtable存的就是son::f()的地址。如果对象是sonson类型的，最后构造的是sonson部分，vtable存的就是sonson::f()的地址。

## 调用f()时

调用f()时，先根据指针的类型来分析f()是不是virtual，根据上文可知，不管哪一层，都会认为f()是virtual的。

既然f()是virtual的，就不直接根据指针类型调用f()，而是查vtable表获取f()的地址，根据地址调用f()，也就是多态的效果。

## 结论

由此可见，只要在基类里写了virtual，派生类里写不写都没有影响的。最后都能起到多态的效果。

此例是virtual关键字的基本用法，用于与后面其它的测试场景做对比。

# 其它测试

[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)

[析构函数的virtual在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-3.html)

[间接调用虚函数](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-4.html)

# 完整代码
```c++
#include <iostream>
using namespace std;

class father
{
public:
  virtual void f()
  {
    cout<<"father::f()"<<endl;
  }
};

class son : public father
{
public:
  void f()
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
  father *pss1 = new sonson();
  pss1->f();
  delete pss1;
  son *pss2 = new sonson();
  pss2->f();
  delete pss2;
  sonson *pss3 = new sonson();
  pss3->f();
  delete pss3;
  return 0;
}
```
