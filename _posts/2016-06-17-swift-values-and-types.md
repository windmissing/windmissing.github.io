---
layout: post
title:  "swift - 数据和类型"
category: [ios, 编程语言]
tags: [ios, swift]
---

#### 数据 - 常量 & 变量  
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

#### 类型  

swift支持的类型包括：Int, Double, String, Array, Dictionary, Tuple, Optional, Class  
其中Class是引用类型，其它都是值类型。关于引用类型和值类型将在下文介绍。

##### 1.Int, Double  
Int和Double都是用于表示数值的。  
Swift是强类型检查的语言。即使是Int和Double之间做类型转换也必须是简式的  

```swift
let iAge : Int = 5
let dAge : Double = Double(iAge)
```

##### 2.String  
有一个类似于C中sprintf的操作，比较常用。

```swift
let introduce : String = String(format : "I'm %d years old", age)
```

##### 3.Tuple 元组
###### 语法  

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

###### 用法

 - 类似C结构体的用法
 - 作为函数的多个返回值
 - store compound data in arrays

##### 4.optionals
###### nil
nil类似于C中的NULL、python中的None  
nil可以赋值给任意类型  
数据被赋值为nil也算是初始化过  
###### optionals类型  
