---
layout: post 
title:  "NULL是什么"
categories: 编程语言
tags: [c/c++, null]
---

对于NULL，大家都不会陌生。非常常用，尤其是在指针里面。
可是很奇怪，在很多编译器里，NULL是黑色的，它不是一个关键字。既然不是关键字，却不用定义就可以使用。

与其说NULL是一个关键字，不如说NULL是一个宏，一个定义在stdlib.h里的宏。
翻看stdlib.h，可以得到答案

```
#ifndef NULL
#ifdef __cplusplus
#define NULL 0
#else
#define NULL ((void *)0)
#endif
#endif
```

那么问题又来了，为什么在C和在C++中，NULL的定义不一样？0和((void*)0)有什么区别？

（1）为什么C可以使用((void *)0)
C支持从void *到任意指针的隐式转换

（2）为什么C不使用0
C也支持从0到空指针的转换。
NULL的本质还是一个指针。把NULL赋值给一个整型时，应当有warning出现，以提示使用者检查代码。
如果把NULL定义成0，就不会出现这样的warning，因此使用((void *)0)更好。

（3）为什么C++可以使用0
C++支持整数0到空指针的转换

（4）为什么C++不使用((void *)0)
C++不支持从void *到任意指针的隐式转换，指针转换必须显式转换