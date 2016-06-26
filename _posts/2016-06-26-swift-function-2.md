---
layout: post
title:  "swift - 函数2"
category: [ios, 编程语言]
tags: [ios, swift, function]
---

#### 一、first class type

函数也是有类型的，格式为`(type, type ...)->type`，这种类型称为first class type。  
具有first class type的有函数和closure  
这是引用类型  
first class type类型的对象像其它类型的对象一样，可以用于赋值、传参、作为返回值。  
有自己的指令和空间

#### 二、函数作为参数
优点：  
动态改变行为  
避免重复代码

##### sort

```swift
func compare(a : Int, _ b : Int) -> Bool {
    return a < b
}
let array = [1, -1, 2, -2, 3]
let sorted = array.sord(compare)
```
sorted为[-2, -3, 1, 2, 3]  
compare可以自由定制，完成更复杂的排序功能  

##### map

```swift
func isEven(val : Int) -> Bool {
    return (val % 2) == 0
}
let array = [1, 2, 3, 4, 5]
let evens = array.map(isEven)
```
evens为[false, true, false, true, false]  
map功能完成了从Int到Bool的映射  
Bool可以是其它类型，Int必须是Int
