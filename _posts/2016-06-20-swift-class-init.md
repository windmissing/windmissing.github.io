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
let me : person = person(personName : "lily")
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
    convenience init(personName : String)
    {
        self.init(personName : personName, personAge : 0)
    }
}

let a : person = person(personName : "lily", personAge : 15)
let b : person = person(personName : "lucy")
```
convenience的构造函数必须调用self.init函数

#### 继承一个类，并初始化

##### 没有成员需要初始化

父类相对于子类没有增加成员，不需要初始化

```swift
class person
{
    var name : String = "lily"
}
class student : person
{
}
var me : student = student()
```

##### 子类初始化时用到父类的成员

使用super.父类函数()来调用父类成员

```swift
class person
{
    var name : String
    init(personName : String)
    {
        self.name = personName
    }
}
class student : person
{
    init()
    {
        super.init(personName: "lily")
    }
}
var me : student = student()
```

##### 区分父类与子类

super.父类函数()
self.子类函数()
