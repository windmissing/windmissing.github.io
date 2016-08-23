---
layout: post
title:  "windows短信猫二次开发"
category: [back-end]
tags: [modem, java]
---

短信猫用于批量收/发短信或其它SIM卡服务。  
短信猫与PC通过GSM无线网络交互。  
交互过程可以分为三个层次：  
1.物理层，即无线网络通信。  
2.指令层，短信猫支持M35AT指令。   
3.应用层，APP需要与短信猫交互的内容。  

在做二次开发过程中，真正需要关心的只是应用层的内容。为了避免重复开始，关于物理层和指令层，可以直接使用现有的开源项目。  

<!-- more -->

#### 一、Rxtx

将rxtxSerial.dll复制到 JAVA_HOME\bin目录下  
将RXTXcomm.jar复制到 JAVA_HOME\jre\lib\ext目录下

#### 二、Smslib

从[smslib官网](http://smslib.org/download/)下载SMSLib (Java - jar file) v3.5.4  
解压，把jar包导入到项目中


暂时就这么多。
