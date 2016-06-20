---
layout: post
title:  "swift - 类的初始化"
category: [ios, 编程语言]
tags: [ios, swift, class, init]
---

##### 1.声明一个类，类有一个成员，并对成员初始化  

```swift
class person{
    var name : String = "lily"
}
let me : person = person()
```

<!-- more -->

##### 2.使用构造函数初始化类的成员

```swift
class person{
    var name : String
    init(personName : String)
    {
        self.name = personName
    }
}
let me : person = perons("lily")
```

##### 3.不初始化成员

```swift
class person{
    var name : String?
}
let me : person = person()
me.name = "lily"
```
对于optional?成员，可以不初始化。  
不初始化则默认初始化为nil。
