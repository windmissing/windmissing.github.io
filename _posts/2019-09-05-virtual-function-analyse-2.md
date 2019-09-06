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

# 解释与结论

id  | 指针名  | 指针的类型 | 实际的类型 | 运行结果 | 解释
--|---|---|---|---|---
1  | pf  | father  | father  | father::f()  |  
2  | ps  | father  | son  | father::f()  | 实际调用的是指针的类型的函数，说明没有多态
3  | ps1  | son  | son  | son::f()  |  
4  | pss  | son  | sonson  | sonson::f()  | 实际调用的是对象的类型的函数，说明有多态的效果

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
