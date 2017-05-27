---
layout: post
title:  "《thinking in JAVA》片断记录 (八)"
category: [读书笔记]
tags: []
---

多态通过分离做什么和怎么做，从另一个角度将接口和实现分离开来。  

#### 早期绑定和后期绑定

C只有早期绑定。  
JAVA办有后期绑定（static, final, private这类不能被重写的方法除外）  
C++可以通过关键字自由选择早期绑定还是后期绑定。默认为早期绑定，加上virtual是后期绑定。

<!-- more -->

#### 域没有多态

```java
class Super {
    public int field;
}
class Sub extends Super {
    public int field;
}
```

Sub实现上包含两个field域：它自己的（field）和从Super处得到的（super.field）  

#### 继承情况下的构造与清理

调用子类构造函数时，会自动地调用父类构造函数。  
调用子类的清理函数（dispose）时不会自动地调用父类的清理函数，需要手动调用。  

#### 当构造函数遇到多态

在C++中，构造函数调用多态函数，那么这个多态函数不会多态的效果。  
在JAVA中没有这样的保证，因此在JAVA的构造器中只能调finaly才是安全的。  
