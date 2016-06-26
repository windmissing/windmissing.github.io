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

##### filter

```swift
func isEven(val : Int) -> Bool {
    return (val % 2) == 0
}
let evens = array.filter(isEven)
```
events为[2, 4]  

##### reduce

```swift
func f(a : Int, _ b : Int) -> Int {
    return a + b
}
let array = [1, 2, 3, 4, 5]
let sum = array.reduce(0, combine : f)
```
sum为15  
计算过程如下：  
y = 0  
y = f(y, 1)  
y = f(y, 2)  
y = f(y, 3)  
y = f(y, 4)  
y = f(y, 5)  
return y

#### 三、操作符函数
##### 一元操作符
prefix和postfix分别用于一元的前置操作符和后置操作符  
关键字放在func前  

```swift
prefix operator$$ { }
prefix func $$ ( u : [Double] ) -> Double {
    return u.reduce(0.0, combine : f)
}
let vec = [1.0, 3.0, 6.0]
let sum = $$vec
```
sum = 10

##### 二元操作符infix

```swift
infix operator **{associativity left precedence 160} //定义结合性和优先级
func **(a : Int, _ b : Int) -> Int {
    return pow(a, b)
}
```
2 ** 8    //256  
4 ** 3 ** 2    //4096

#### 四、嵌套函数

#### 五、函数作为返回值
