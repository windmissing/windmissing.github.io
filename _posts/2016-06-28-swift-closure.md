---
layout: post
title:  "swift - closure"
category: [ios, 编程语言]
tags: [ios, swift, closure]
---

#### closure

closure是一种类似于函数的类型，也是first class type的一种。  
closure是引用类型，有自己的指令和空间。  
closure可以看作是一种轻量级的函数，它的一般格式如下：  

```swift
//声明
let 名字 = {(参数) -> 返回值 in
    closure的内容
}
//调用
let 返回值 = 名(参数)

//声明与调用合并使用
let 返回值 = {(参数) -> 返回值 in closure的内容}(实参)
```

<!-- more -->

#### closure参数的语法

##### 有外参名
这种情况下closure与function的参数用法是一样的

```swift
func area(length l : Int, width w : Int) -> Int {
    return l * w
}
let a = area(length : 2, width : 3)

let area{ (length l : Int, width w : Int) -> Int in
    return l * w
}
let a = area(length : 2, width : 3)
```
##### 无外参名
closure不需要通过`_`来隐藏外参名

```swift
func area(length : Int, _width : Int) -> Int {
    return length * width
}
let a = area(2, 3)

let area{ (length : Int, width : Int) -> Int in
    return length * width
}
let a = area(2, 3)
```

看上去closure只是参数和返回值放在函数体里面的function？  
**NO！**  
swift的类型推导功能在closure上发挥得淋漓尽致。使得closure的语法更简洁易读。  

#### 类型推导
##### Void
假设c1是一个没有入参和返回值的closure，那么它应该这么写。

```swift
let c1 = {(_ : Void) -> Void in
    ...
}
```
事实上它可以写得更简洁：  
（1）当closure的参数是Void类型时，可以省略不写

```swift
let c1 = {() -> Void in
    ...
}
```
（2）当closure的返回值是Void类型时，也可以省略不写

```swift
let c1 = { () in
    ...
}
```
（3）当closure的参数和返回值都是Void类型时，整体可以直接进入closure体

```swift
let c1 = { ... }
```

##### 赋值
赋值表示式的一般格式为`expression = value`
在closure中，只要其中一方指明了类型，另一方的类型就可以自动推导出来

```swift
let tm = { () -> String in
    ...
    return str
}
```
自动推导出tm的格式为`() -> String`  
或者这样写：

```swift
let tm : () -> String = {
    ...
    return str
}
```
这种情况下，就不需要写明closure表达式的参数和返回值了。

##### 作为参数
假设有这样一个需求：  

```swift
func bySquare(edge : Int) -> Int {
    return edge * edge
}
func area(length : Int, calculate : Int -> Int) -> Int {
    return calculate(length)
}
let a = area(5, calculate : bySquare)
```
这里使用了函数bySquare作为参数来决定使用什么方式计划面积。如果要使用closure bySquare作为参数，则应该这么写：

```swift
func area(length : Int,
          bySquare : {(edge : Int) -> Int in
                       return edge * edge
                     }
         )
```
（1）closure的内容只有一行，因此return可以去掉

```swift
func area(length : Int,
          bySquare : {(edge : Int) -> Int in
                       edge * edge
                     }
         )
```
（2）参数类型和返回值可以根据closure内容推导出来，所以可以省去。用'$'+'数字'代表使用的是第几个参数。

```swift
func area(length : Int,
          bySquare : { $0 * $0 }
         )
```

（3）因为closure是最后一个参数，因此可以使用trailing closure语法

```swift
func area(length : Int) { $0 * $0 } )
```

##### 语句表达式

```siwft
let area = {(r : Double) -> Double in
                return 3.14 * r * r
           }
```
可简化为：

```siwft
let area = { 3.14 $0 * $0 }
```

##### 语境
例子1：

```swift
let array = [1, 2, 3, 4, 5]
array.map( { (u:Int) -> Bool in
                return (u%2) == 0
           }
         )
```
可简化为：

```swift
let array = [1, 2, 3, 4, 5]
array.map() { ($0%2) == 0 }
```

例子2：如果closure内容只是一个函数调用，可以进一步简化

```swift
let yy = radians.map() { sin($0) }
let yy = radians.map( sin )
```
