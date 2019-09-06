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

由此可见，只要在基类里写了virtual，派生类里写不写都没有影响的。最后都起到多态的效果。

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
