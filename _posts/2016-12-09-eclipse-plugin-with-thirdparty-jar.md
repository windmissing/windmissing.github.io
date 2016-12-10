---
layout: post
title:  "eclipse插件运行时提示NoClassDefFoundError"
category: [编程语言]
tags: [eclipse, plugin, export, java]
---

运行插件时，在Console出现类似这样的错误提示：  

```
Caused by: java.lang.NoClassDefFoundError: org/eclipse/jdt/internal/ui/packageview/PackageFragmentRootContainer
	at com.test.myplugin.Environment.getCurrentProject(Environment.java:63)
	at com.test.myplugin.Environment.<init>(Environment.java:21)
	at com.test.myplugin.handlers.ReferenceHandler.execute(ReferenceHandler.java:31)
	at org.eclipse.ui.internal.handlers.HandlerProxy.execute(HandlerProxy.java:290)
	at org.eclipse.ui.internal.handlers.E4HandlerProxy.execute(E4HandlerProxy.java:90)
	at sun.reflect.GeneratedMethodAccessor22.invoke(Unknown Source)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:606)
	at org.eclipse.e4.core.internal.di.MethodRequestor.execute(MethodRequestor.java:56)
	... 36 more
```

<!-- more -->

#### 原因

运行过程中无法加载PackageFragmentRootContainer类  

#### 解决方法一：把PackageFragmentRootContainer放到插件环境中  
打开plugin工程的plugin.xml  
打开Runtime选项卡   
找到右下角的Classpath  
把库add到classpath中  
![](/image/eclipse-plugin-with-thirdparty-jar-0.jpg)  

#### 解决方法二：  


#### NoClassDefFoundError与ClassNotFoundException的区别

我们经常被java.lang.ClassNotFoundException和java.lang.NoClassDefFoundError这两个错误迷惑不清，尽管他们都与Java classpath有关，但是他们完全不同。  

||NoClassDefFoundError|ClassNotFoundException|
|---|---|---|
|发生时间|JVM在动态运行时加载对应的类|在编译的时候|
|查找类的路径|classpath|classpath|
|原因|一定是环境问题|如果是在J2EE的环境下工作，并且得到NoClassDefFoundError的异常，而且对应的错误的类是确实存在的，这说明这个类对于类加载器来说，可能是不可见的。|

#### 参考来源

http://blog.csdn.net/jamesjxin/article/details/46606307