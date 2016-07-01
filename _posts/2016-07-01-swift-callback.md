---
layout: post
title:  "swift - 回调"
category: [ios, 编程语言]
tags: [ios, swift, callback]
---

#### 一、回调函数

> 回调函数就是允许用户A把需要调用的方法B的指针作为参数注册给另一个函数C，以便该函数在处理相似事件的时候可以灵活的使用不同的方法。  
回调函数B不由该函数的实现方A直接调用，而是在特定的事件或条件发生时由另外的一方C调用，用于对该事件或条件进行响应。

在swift中有同步和异步两种形式的回调函数：

| 同步回调函数 | 异回调函数步 |
|---|---|
| C调用方法B，B可以是函数或者closure | C调用函数B并使B在另一线程（也可以是相同线程）上运行 |
| B返回之前C处理block状态 | B和C运行在不同的线程，不会互相block。|
| B返回之后C继续执行 | B结束后会通知C |

<!-- more -->

主线程不能被block住，否则  
 - UI无响应
 - APP卡住
因此如果回调函数要执耗时且有可能失败的操作，建议使用异步式的回调函数

同步回调函数有时用于作为delegation的替代品。

#### 二、同步回调函数的例子

```swift
func C( x : Double, fn : (Double -> Double) ) -> Double?
{
    ....
    return fn(x)
}
//调用者A
let ret = C(0.01, fn : B)
```
例子中fn是一个回调函数，由sync的用户动态地决定sync操作触发什么函数  
如果fn是一个耗时且可能出错的函数，例如访问网络数据。那么就不能让fn在主线程上运行。要把它改成异步调用的方式。

#### 三、异步回调函数（一）

```swift
let P = NSBlockOperation() {
    let res = C(0.01){B}
    let Qres = NSBlockOperation() {
        if let p = ret {...}
        else {...}
    }
    NSOperationQueue.mainQueue().addOperation(Qres)
}
let Q = NSOperationQueue()
Q.addOperation(P)
```

1. 将C和B封装到一个操作P中。  
P是一个使用了trailing closure语法的closure
2. 把P加入到操作队列Q中，Q队列中的操作会在一个独立的线程中执行
3. 修改操作P，将B完成后的后续处理封装到操作Qres中
4. 把Qres加入到主线程的操作队列

效果：  
在另一个线程执行P中的C  
C执行结果后执行主线程中的Qres  
在另一个线程上执行P时，主线程不受影响

#### 四、异步操作的回调函数（二）

```swift
func C(x : Double, fn : Double -> Double, completion : Double? -> Void) {
    let P1 = {
        ...
        ret = fn(x)
    }
    let P2 = {
        completion( ret )
    }
    NSOperationQueue.mainQueue.addOperationWithBlock(P2)
}
//调用
C(0.01, fn : B, completion : comp)
```

1.把调用回调函数的过程与结果分别封装到两个operation中  
2.在其它线程执行P1  
3.P1结束后在主线程执行P2
