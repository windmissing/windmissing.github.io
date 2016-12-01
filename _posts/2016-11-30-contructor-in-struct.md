---
layout: post
title:  "构造函数对结构体初始化的影响"
category: [编程语言]
tags: [struct, contructor]
---

带构造函数的结构体不能使用初始化列表的方式初始化  

<!-- more -->

#### 初始化结构体的两种方法

```
struct noContructor{
    int param1;
    int param2;
};
int main()
{
    //方法一：初始化列表
    noContructor str1={1,2};
    
    //方法二：先定义，再初始化
    noContructor str2;
    str2.param1 = 1;
    str2.param2 = 2;
};
```

#### 带构造函数的结构体的初始化

```
struct withContructor{
    int param1;
    int param2;
};
int main()
{
    //方法一：初始化列表， error C2552: 不能用初始值设定项列表初始化非聚合
    noContructor str1={1,2};
    
    //方法二：先定义，再初始化， 正确
    noContructor str2;
    str2.param1 = 1;
    str2.param2 = 2;
};
```