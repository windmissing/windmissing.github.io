---
layout: post
title:  "windows tomcat 无法启动"
category: [back-end]
tags: [back-end, tomcat]
---

#### 现象
双击tomcat9w.exe，启动到一半就退出，并显示stopped  
浏览器中输出127.0.0.1:8080无法打开网页  

<!-- more -->

#### debug方法

1.在cmd中使用startup.bat，可以看到一些打印信息  
2.访问127.0.0.1:8080页面会提示一些信息  

#### 可能的原因

（1）浏览器设置了代理。  
访问localhost不能使用代理，需要把代理关掉或者设置过滤。  
过滤在advanced里设置  
  
（2）提示500 - can not create folder  
原因：当前帐号对tomcat的目录没有写权限  
方法一：右键-属性-security tab-SYSTEM，给当前用户加权限  
方法二：使用管理员帐登陆  
[参考链接](http://stackoverflow.com/questions/10577494/tomcat-installation-exception)

（3）现象忘记了，重启一下tomcat就可以了
