---
layout: post
title:  "virtual关键字在子类"
category: [编程语言]
tags: [C++, virtual]
---

# 运行结果是什么？

![](\images\2019\10.png)


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
  pf->B();
  delete pf;
  father *ps = new son();
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
