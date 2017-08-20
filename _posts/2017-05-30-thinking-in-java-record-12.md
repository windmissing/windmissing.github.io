---
layout: post
title:  "《thinking in JAVA》片断记录 (十二)"
category: [读书笔记]
tags: []
---

传统的错误处理模型：返回某个特殊值或者设置某个标志，并且假定接收者对这个返回值或标志进行检查。  
缺点：  
1. 认为那是别人造成的，因此不去检查错误情形  
2. 错误情形的检查确实很无聊  
3. 代码很可能会变得难以阅读  
解决办法：用强制规定的形式来消除错误处理过程中随心所欲的因素    
优点：  
1. 把一个问题提交到一个更高级别的环境中，在这里做出正确的决定  
2. 降低处理错误代码的复杂度  
3. 只需在一个地方处理错误  

---

把异常问题和普通情形相区分很重要：   
异常情形：在当前环境下无法获得必要的信息来解决问题  
普通情形：在当前环境下能得到足够的信息来处理这个错误  

---

抛出异常后的处理过程：  
1. 使用new在堆上创建异常对象  
2. 当前的执行路径被终止  
3. 从当前环境中弹出对异常对象的引用  
4. 异常处理机制接管程序  
5. 合适异常处理程序继续执行  

---

||||
|---|---|---|
|异常|不允许程序沿着正常的路径继续走下去|强制程序处理问题，并返回到稳定状态|
|C/C++|没有任何办法强制程序在出问题时停止运行|较长时间忽略问题，陷入完全不恰当的状态中|

---

从效果上看，throw一个异常对象是从方法return了一个异常对象。  
可以简单地把throw看作一种不同的return机制。  
实际上，异常对象返回的地点与return返回的地点完全不同。  

---

要自己定义异常类，必须从已有的异常类继承。  
定义自己的异常类，可以为该异常类添加许多功能，例如：  
1. 输出异常到日志  
2. 生成日志消息  
3. 覆盖getMessage()以产生更详细的信息。  
但是，对异常来说，最重要的是类名，其它功能也许都用不上。  

---

JAVA强制把方法可能抛出的异常告知给客户端，即异常说明。  

```java
void f() throws xxx
```
方法里的代码产生了异常，要么处理这个异常，要么在异常说明中表明。  

---

可以在异常说明中表明异常，但实际不抛出异常。  
这种用法常用于抽象基类或接口。  

---

可以使用一些方法来打印异常的信息：  

```java
String getMessage()
Strubg getLocalizedMessage()
String toString()
void printStackTrace()
getClass()/getName()/getSimpleName()
```

---

#### 重新抛出异常

##### 1. 获取异常后重新抛出，不更新栈信息

```java
catch (Exception e)
{
    throw e;
}
```

##### 2. 获取异常后重新抛出，更新栈信息

```java
catch (Exception e)
{
    throw (Exception)e.fillInStackTrace();
}
```

##### 3. 获取异常后抛出另一异常，不带原异常信息

```java
catch (Exception e)
{
    throw new Exception();
}
```

##### 4. 获取异常后抛出另一异常，带原异常信息

```java
catch (Exception e)
{
    throw new Exception(e);
}
```
或

```java
catch (Exception e)
{
    Exception e2 = new Exception();
    e2.initCause(e);
    throw new Exception(e2);
}
```

---

用户方法及运行时故障都可能抛出Exception异常。  
异常是用名称代表发生的问题，并且异常的名称应该可以望文生义。  
运行时异常，能自动被JVM抛出，都是从RuntimeException类继承而来。  
代码中可以忽略RuntimeException（及其子类）异常。  

---

finally子句：无论try块中的异常是否抛出，它们都能得到执行。  
它的作用是把内存之外的资源恢复到它们的初始化状态。  
当涉及break和continue语句的时候，finally子句也会得到执行。（无例子）  
即使try块中有return语句，finally也会得到执行。  

```java
public stativ void f()
{
    try {
        ...
        return;
    } finally {
        ... // 仍旧会执行
    }
}
```

---

在finally中加return，会导致try中的异常丢失

```java
public stativ void f()
{
    try {
        throw new Exception();
    } finally {
        return; //上面的异常会丢失
    }
}
```

---

异常限制：当子类覆盖基类的方法时，只能抛出在基类方法的异常说明里列出的那些异常。这使得对象的可替换性得到了保证。  
异常限制对构造器的策略不同：  
（1）派生类构造器可以抛出基类构造器未异常说明的异常。  
（2）派生类构造器的异常说明必须包含基类构造器的异常说明。  
（3）派生类构造器不能捕获基类构造器抛出的异常。   

---

异常说明本身不属于方法类型的一部分。  
不能基于异常说明来重载方法。  

---

如果在构造器内抛出了异常，清理行为也许就不能正常工作了。  
即使使用finally也不能简单地解决问题。  
对于在构造阶段可能会抛出异常并且清理的类，最安全的方式是使用嵌套的try子句。  
在创建需要清理的对象之后，立即进入一个try-finally语句块。  

```java
public class Cleanup{
    public static void main(String[] args)
    {
        try {
            InputFile in = new InputFile("Cleanup.java");
            //创建成功后，进入一个新的try-finally
            try {
                ...//
            }catch(Exception e)
            {
                ...//
            }finally{
                in.dispose(); //清理InputFile
            }
        }
        catch (Exception e)
        {
            ...//创建InputFile失败
        }
    }
}
```

---

派生类的对象可以匹配其基类的处理程序。  

---

原则：只有在你知道如何处理的情况下才捕获异常  
目标：把错误处理的代码同错误发生的地点分离。  
精髓：不在于恢复而在于报告。  