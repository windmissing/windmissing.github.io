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

# 解释与结论

id  | 指针名  | 指针的类型 | 实际的类型 | 运行结果 | 解释
--|---|---|---|---|---
1  | pf  | father  | father  | this is father::B()<br>this is father::B()  |  
2  | ps  | father  | son  | this is father::B()<br>this is father::B()  | 由[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)可知此处不会有多态
3  | ps1  | son  | son  | this is father::B()<br>this is son::B()  | 此例中，指针的类型和对象的类型都是son，为什么最后调用的是fathher::B()?
4  | pss  | son  | sonson  | this is father::B()<br>this is sonson::B()  | 由[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)可知此处应该有多态效果，为什么最后调用的还是fathher::B()?

解释：

在上面的测试用例中，`ps1->A();`和`pss->A();`的运行结果都是`father::B()`。它们都有一个共同的特点，就是指针通过A()去调用B()。

当程序通过A()调用B时，它已经处理father::A()的作用域里面了，因此此时它实际上已经不再通过ps1或者pss去访问B()，而是通过father::this。

father::this显然是father类型的指针，所以它会先去查看father::B()。它发现father::B()不是虚函数，也就不会去查vtable，而是直接调用father::B()了。这一部分的原理与[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)相同。

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
