---
layout: post
title:  "JAVA设计模之观察者模式"
category: [设计模式]
tags: []
---

考虑这样的一个场景：  
数据库类有两个对象dbA和dbB，界面显示类有一个对象ui。ui根据dbA和dbB的内容显示。当dbA和dbB发生改变时，ui需要做相应的更新。  

<!-- more -->

#### 轮询模式

最直观的方法就是开启一起线程来监视dbA和dbB的情况。每过一段时间就询问一下对象是否有改变，如果有则刷新。  
这种方法类似于早期操作系统中的轮询，所以我称它为轮询模式。  
这种方法的缺点显而易见。  

#### 回调模式

由于轮询的种种缺点，后来的操作系统将轮询升级为中断。  
中断过程是由硬件完成。但软中断信号的过程仍具有参考价值。  
通过系统调用signal用来设定某个信号signum的处理方法handler。  

```c
void (*signal(int signum, void (*handler)(int)))(int); 
```

用户不需要不停地检测signum信号是否发生。当系统捕捉到signum信号时，就会自动调用用户设置的handler作相应的处理。  
这个handler实际上是一个回调函数，因此我称它为回调模式。  
类似地，ui也可以把数据改变时要做的更新动作以参数的方式注册到对象dbA和dbB。  
当dbA和dbB发生改变时，依次调用向它们注册过的回调函数。  
redis就是这么做的。  

#### 观察者模式

对于这种问题，回调模式是C常用的解决方案。  
JAVA作为面向对象语言，可以用更优雅的方式实现相同的效果。    
![](http://www.yesky.com/20020603/observer.gif?_=2088121)  
看上去比回调模式复杂不少，可千万不要被吓到了，其实它和回调模式最大的区别在于注册的内容不同。  
在回调模式中，用户向数据库对象注册回调函数，数据库对象自动调用回调函数。  
而在这里，回调函数被放在了ui对象中，然后把整个ui对象注册到数据库对象。数据库对象自动地通过ui对象调用回调函数。  
其中，数据库对象是被观察者，ui对象是观察者。  
为什么注册的是对象而不是函数？我的理解是，面向过程的程序中，是以函数为单位管理代码逻辑的。在面向对象的程序中，是以对象为单位管理代码逻辑的。  

#### JAVA的观察者模式

相比于其它设计模式而言，观察者模式对于JAVA尤其重要。以致于JAVA已经实现了一套观察者框架。只需要继承观察者类和被观察者类就能实现观察者的功能。

![](http://www.yesky.com/20020603/javautilmethods.gif?_=2088121)

```java
package com.zj.observer;
import java.util.Observable;
 
public class db extends Observable {
    private int data = 0;
 
    public int getData() {
       return data;
    }
 
    public void setData(int i) {
       data = i;
       setChanged();
       notifyObservers();
    }
}

package com.zj.observer;
import java.util.Observable;
import java.util.Observer;
 
public class ui implements Observer{
    public void update(Observable o, Object arg) {
       NumObservable myObserable=(NumObservable) o;
       System.out.println("Data has changed to " +myObserable.getData());
    }
}
```

