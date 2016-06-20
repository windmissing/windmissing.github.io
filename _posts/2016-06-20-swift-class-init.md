---
layout: post
title:  "swift - 类的初始化"
category: [ios, 编程语言]
tags: [ios, swift, class, init]
---

#### 声明一个类，并初始化
##### 1.使用赋值的方式初始化类的成员  

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

##### 4.convenience构造函数

```swift
class person{
    var name : String
    var age : Int
    init(personName : String, personAge : Int){
        self.name = personName
        self.age = personAge
    }
    convenience override init(personName : String)
    {
        self.init(personName : personName, personAge : 0)
    }
}

#### 继承一个类，并初始化

##### 
