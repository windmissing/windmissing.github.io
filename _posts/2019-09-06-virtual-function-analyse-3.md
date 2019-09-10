---
layout: post
title:  "析构函数的virtual在子类"
category: [编程语言]
tags: [C++, virtual, 析构函数]
---

# 运行结果是什么？

![](\images\2019\11.png)

```c++
father *pf = new father();
delete pf;
father *ps = new son();
delete ps;
son *ps1 = new son();
delete ps1;
son *pss = new sonson();
delete pss;
father *pss1 = new sonson();
delete pss1;
```

<!-- more -->

# 运行结果

```
delete father()
delete father()
delete son()
delete father()
delete sonson()
delete son()
delete father()
delete father()
```

# 解释与结论

[virtual关键字在父类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-1.html)和[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)已经说明virtual关键字在父类的情况能够正常地进行多态。因此这里仅把关注点放在virtual关键字在子类的情况。

由于析构函数与普通函数略有不同，把virtual关键字在子类的情况对析构函数再测一遍。结论与[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)类似。

id  | 指针名  | 指针的类型 | 实际的类型 | 运行结果 | 解释
--|---|---|---|---|---
1  | pf  | father  | father  | delete father()  |  
2  | ps  | father  | son  | delete father()  | 实际调用的是指针的类型(father)的析构函数，说明没有多态
3  | ps1  | son  | son  | delete son()<br>delete father()  | 调用了~son()，~son()又调用了~father() ，由编译器完成。
4  | pss  | son  | sonson  | delete sonson()<br>delete son()<br>delete father()  | 实际调用的是对象的类型(sonson)的函数，说明有多态的效果。~sonson()又调用了~son()以及~father()，由编译器完成。
5  | pss1  | father  | sonson  | delete father()  | 实际调用的是指针的类型(father)的析构函数，说明没有多态

结论：

1. 结论与[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)类似，可以对照着看。

2. 如果virtual只写在派生类的析构函数中，而没有写在基类中的析构函数中，则不会有多态的效果。有可能只析构基类部分而不析构派生类部分，造成内存泄漏。

3. 如果在某一层的派生类中加了virtual标签，那么从这一层开始以后的每一层，这个函数都会有多态的效果。

# 其它测试

[virtual关键字在父类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-1.html)

[virtual关键字在子类](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-2.html)

[间接调用虚函数](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/virtual-function-analyse-4.html)

# 完整代码

```c++
#include <iostream>
using namespace std;

class father
{
public:
  ~father()
  {
    cout<<"delete father()"<<endl;
  }
};

class son : public father
{
public:
  virtual ~son()
  {
    cout<<"delete son()"<<endl;
  }
};

class sonson : public son
{
public:
  ~sonson()
  {
    cout<<"delete sonson()"<<endl;
  }
};

int main()
{
  father *pf = new father();
  delete pf;
  father *ps = new son();
  delete ps;
  son *ps1 = new son();
  delete ps1;
  son *pss = new sonson();
  delete pss;
  father *pss1 = new sonson();
  delete pss1;
  return 0;
}

```
