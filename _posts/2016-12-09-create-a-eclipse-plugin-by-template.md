---
layout: post
title:  "eclipse插件开发 Hello World"
category: [编程语言]
tags: [eclipse, plugin, java]
---

#### 使用模板创建一个插件

File -> New -> Other -> Plug-in Project  
**如果Wizards中没有Plub-in Project，可能因为使用的是Java SE版本的eclipse，换成Java EE版本的eclipse就可以了。**  
  
输入Project name

选择一个模板，例如“Hello, World Command”，Finish

#### 运行效果

出现了这样的一个工程：  
![](/image/create-a-eclipse-plugin-by-template-0.jpg)  
点击运行按钮，将再开一个eclipse  
效果一：菜单栏Run后面出现“Sample Menu”，点击后弹出对话框：“Hello, Eclipse world”  
效果二：工具栏出现一个紫色的小球，点击后弹出对话框：“Hello, Eclipse world”  

#### 插件导出与加载

##### 导出

File -> Export -> Plugin 

##### 加载

打开eclipse的安装目录ECLIPSE  
把jar包copy到ECLIPSE/plugins  
重启eclipse  

#### 工程说明

