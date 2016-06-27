---
layout: post
title:  "swift - 数据和类型"
category: [ios, 编程语言]
tags: [ios, swift]
---

## 数据 - 常量 & 变量  
语法格式：  

```swift
//关键字 变量名 : 变量类型
var age : Int
let age : Int

//关键字 名字 : 类型 = 表达式
var msg : String = "Hello world"
let msg : String = "Hello world"
```
不管是变量还是常量，未初始化前不能使用，否则编译器报错  

<!-- more -->

---

## 类型  

swift支持的类型包括：Int, Double, String, Array, Dictionary, Tuple, Optional, Class  
其中Class是引用类型，其它都是值类型。关于引用类型和值类型将在下文介绍。

#### 1.Int, Double  
Int和Double都是用于表示数值的。  
Swift是强类型检查的语言。即使是Int和Double之间做类型转换也必须是简式的  

```swift
let iAge : Int = 5
let dAge : Double = Double(iAge)
```

#### 2.String  
有一个类似于C中sprintf的操作，比较常用。

```swift
let introduce : String = String(format : "I'm %d years old", age)
```

#### 3.Tuple 元组
##### 命令元组  

```swift
//把单个数据组成元组
//关键字 元组名 : (类型1, 类型2 ... ) = [数据1, 数据2 ...]
let student : (String, Int) = ["lily", 15]

//把元组解析成单个数据
//关键字 (数据名1, 数据名2 ... ) : (类型1, 类型2 ...) = 元组名
let (name, age) : (String, Int) = student
//关键字 (数据名1 : 类型1, 数据名2 : 类型2 ... ) = 元组名
let (name : String, age : Int) = student
```

##### 无命名元组‘

```swift
//把单个数据组成元组
let student = (name : "lily", age : 15)
let name = student.name
let age = student.age
```
##### 用法

 - 类似C结构体的用法
 - 作为函数的多个返回值
 - store compound data in arrays

#### 4.optionals
##### nil
nil类似于C中的NULL、python中的None  
nil可以赋值给任意类型  
数据被赋值为nil也算是初始化过  
##### optionals类型  
从某个角度讲，它和指针类似。因为它不是作为一个独立的类型存在的。它是在原有类型的基本上加一些后缀所形成的与原类型相似却又有区别的新类型。  
例如Int，它对应的optionals类型为Int?和Int!  
##### ?
变量和常量在使用前必须被初始化。如果不知道初始化为什么值，可以初始化为nil。  
如果  一个对象可以被初始化为nil && 期待使用这个对象时是否nil会有不同的行为，那么  建议把类型设置为optional?  

###### （1）optional?类型的默认初始化为nil

```swift
var age : Int?
```
并没有显式地初始化age，但age已被初始化为nil

###### （2）仅当对象不为空时对使用
直接使用空对象可能会出错，这一种保护机制。  
`if let`是固定搭配  

```swift
var age : Int?
...
if age != nil { print age }    //不推荐用法
if let a = age { print a }     //推荐用法
```

###### （3）当对象为空是返回特殊值

```swift
var age : Int?
...
let a : Int = age?? -1
...
```
###### （4）作为函数返回值
`string2Int`把字符串转换为数字。  
如果输入的字符串不能转换为数字，则返回nil  

```swift
```

###### （5）接收optional?
`function_may_fail`可能返回一个有意义的值，也可能返回nil。  
如果`function_may_fail`返回nil，后面将不再继续执行，而是将nil返回给val  

```swift
let val = function_may_fail()?.another_function()
```

##### !
如果 一个对象不能赋为nil，如果为nil将会非常危险，那么 建议使用optional!类型  
```swift
let age = Int!
```
 - 如果没有显式地初始化对象，系统也不会默认地初始化对象  
 - 不能把optional!的对象赋值为nil，否则会导致crash
 - 使用optional!时非常省心，不需要做判断，因为完全不用担心它是nil
 
###### 用法实战  

在myViewController中有对控件view对象的引用。  
在[《ios开发中的MVC模型》](/ios/2016-06/model-view-controller.html)提到过，view对象都是lazy instantiate的。它们在被引用之前都是weak nil reference。在第一次被引用时由UIViewController创建。  
如何确保在引用时，UIViewController已经做了创建的工作？就是在myViewController把引用设置为optional!类型。  
如果这个对象没有创建，在运行时能够及时地得到反馈。  
 
#### 5.字典

```swift
//关键字 字典名 : [key类型 : value类型 ] = [ key1 : value1, key2 : value2 ...]
let student : [String, Int] = [ "Lily" : 15, "Lucy", 16]
```

读取字典的内容时**强烈建议**使用`if let`组合。因为如果key不存在，就会返回nil。

```swift
if let age = student["Tom"] { ... }
```

#### 6.其它类型  
functions, enumerations, protocols

## 类型推断

swift可以根据数据的内容推断出数据的类型，所以在声明对象时，类型常常可以省略

```
var age : Int = 15
var age = 15
```

## 类型的类型 ： 值类型、引用类型

#### 引用类型（通常是class类型）  

当声明一个类的对象时，对象名类似一个指针，指向对象所在的空间  

```swift
var xx : class_type = class_type("lily", 15)
```

```
     引用        -----------------
xx ------------>|                 |
                |                 |
                -------------------
```

把一个对象赋值给另一个对象时，两个对象指向同一个空间（浅拷贝）

```
var yy : class_type = xx
``

```

```
     引用        -----------------           引用
xx ------------>|                 | <------------- yy
                |                 |
                -------------------
```

 - xx和yy共享一段内存，一个改变另一个也会改变  
 - need class inheritance  
 - 用`xx === yy`来判断xx和yy是否指向同一空间

#### 值类型

把一个对象赋值给另一个对象时使用深拷贝，两个对象有各自的空间，互相独立，互不干扰  
虽然是深拷贝，但使用了写时复制技术（效率）  
no ckass inheritance needed
