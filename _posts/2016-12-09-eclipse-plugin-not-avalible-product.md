---
layout: post
title:  "eclipse插件在真实环境中没有效果"
category: [编程语言]
tags: [eclipse, plugin, java]
---

在测试环境上有效果，实际使用中没有效果

<!-- more -->

#### 现象

在开发plugin的工程中，点击Run运行查看效果，插件正常运行。  
把插件导出，并在另一个eclipse中加载该插件，发现插件没有效果。  
打开放插件的目录，删除该插件，删除成功。  

#### 原因一：eclipse没有加载该插件

解决方法：  
1. 删除整个目录/eclipse/configuration/org.eclipse.update/，重启eclipse  
2. 在启动eclipse时带上 -clean参数  如：d:\eclipse\eclipse.exe -clean  
3. 在/configuration/config.ini文件中加入一行  osgi.checkconfiguration=true  这样它会寻找并安装插件，找到后可以把那行再注释掉，这样以后每次启动就不会因寻找插件而显得慢了。  

#### 原因二：jre不匹配  

解决方法：  
打开plug工程的plugin.xml  
选择Overview选项卡  
找到Execution Environments  
点击Add添加支持的运行环境  
![](/image/eclipse-plugin-not-available-0.jpg)  