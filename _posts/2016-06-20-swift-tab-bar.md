---
layout: post
title:  "IOS开发 - 标签栏（tab bar）"
category: [ios]
tags: [ios, swift]
---

#### 一、启用tab bar
##### 步骤
1.选中view controller  
2.Editor->Embed in->Tab Bar Controller  
##### 效果：  
（1）页面变成了Tab Bar Controller  
（2）下方出现了一个item  
（3）右边多了一个View Controller  
（4）当前View Controller与新的View Controller之间有个relationship  
（5）如果当前页面有内容，内容会移到新的View Controller上  

#### 二、增加一个tab item
##### 步骤
1.拖进一个控件View Controller（页面3）  
2.点击tab bar Controller  
3.Ctrl，同时点击、拖拽至页面3  
4.relationship seque->view controllers  
##### 效果
（1）页面1有两个item  
（3）页面1与页面3之间有一个relationship  

#### 运行效果
打开后页面下方有2个tab item
默认显示与第一个item相关联的页面
