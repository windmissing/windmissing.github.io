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

##### 
#### 返回值类型

#### 参数属性

#### 参数个数
