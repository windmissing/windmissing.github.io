---
layout: post
title:  "swift - 函数"
category: [ios, 编程语言]
tags: [ios, swift, function]
---

#### 函数声明

```swift
func 函数名(参数1, 参数2 ... ) -> 返回值类型
```

<!-- more -->

#### 参数名
参数名分为内参名和外参名。外参名是给调用者用的标签，内参名是函数内代表参数的名字。
##### 完整的函数名

```swift
//声明
func area(length l : Int, width w : Int) -> Int {
    return l * w;
}
//完整的函数名
area(length : width :)
//调用
let a = area(length : 2, width : 3)
```
其中length和width是外参名，l和w是内参名

##### 非显示的外参名

```swift
//声明
func area(length : Int, width : Int) -> Int {
    return length * width
}
//函数名
area( _ ： width : )
//调用
let a = area(2, width : 3)
```

##### 没有外参名

```swift
//声明
func area(length : Int, _ width : Int) {
    return length * width
}
//函数名
area( _ : _ : )
//调用
let a = area(2, 3)
```

##### 没有函数

```swift
func no_param_function(_ : Void)
```
括号中的内容不能去掉  

#### 返回值类型
##### 返回Void
##### 返回多个数据时可以使用元组

```swift
func parseStringToDate(string str : String) -> (day : Int, month : String, year : Int) {
    ...
    return (day : d, month : m, year : y)
}
let (d, m) = parseStringToDate(string : str)
```

##### 返回optionals时使用nil表示失败  
#### 参数属性
##### 设置参数默认值

```swift
func area(length : Int, width : Int = 2) -> Int
```
带默认值的参数必须是最后一个参数  

##### optional参数
使用这个参数时要结合if let  

##### 参数值可变量
默认情况下，函数的参数是按值传递的，参数到了函数内部会拷贝一份再使用。也就是说，函数内对参数的改变不影响函数外的调用者。  
如果希望改变，可以有两种方法：  
1.var关键字  

```swift
func area(var length : Int, width : Int) -> Int {
    length = length + 1
    return length
}
var length = 2
length = area(length, width : 2)
```
说明：使用var的参数仍然是按值拷贝，但是在函数结束时它会再拷贝一份出来

2.inout关键字  

```swift
func area(inout length : Int, _ width : Int) -> Int {
    length = length + 1
    return length * width
}
var length : Int = 1
let a = area(&length, 3)
```
说明：  
inout关键字与默认值不能同时使用  
使用inout后会以引用方式传参  
#### 参数个数

```swift
func recipe(title t : String, ingredients : String ...) -> String {
    for ing in ingredients {
        ...
    }
    ...
}
let page = recipe(title : "title", ingredients : "aaa", "bbb", "ccc")
```
说明：  
ingredients是一个String类的数组，后面的可变个数的参数都必须是String的  
可变长参数必须是最后一个参数
