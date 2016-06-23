---
layout: post
title:  "IOS开发 - 标签栏（tab bar）"
category: [ios]
tags: [ios, swift]
---

#### 一、期待目标

![](/image/xcode-tab-bar-show.png)

<!-- more -->

#### 二、启用tab bar
##### 步骤
1.选中view controller  
![](/image/xcode-view-controller-logo.png)  
2.Editor->Embed in->Tab Bar Controller  
##### 效果：  
（1）页面变成了Tab Bar Controller  
![](/image/xcode-tab-bar-controller.png)  
（2）下方出现了一个item  
![](/image/xcode-sub-item.png)  
（3）右边多了一个View Controller,当前View Controller与新的View Controller之间有个relationship  
![](/image/xcode-new-view-controller-relationship.png)  
（4）如果当前页面有内容，内容会移到新的View Controller上  

#### 三、增加一个tab item
##### 步骤
1.拖进一个控件View Controller（页面3）  
![](/image/xcode-view-controller-outlet.png)  
2.点击tab bar Controller  
3.Ctrl，同时点击、拖拽至页面3  
4.relationship seque->view controllers  
##### 效果
（1）页面1有两个item  
![](/image/xcode-two-sub-item.png)   
（2）页面1与页面3之间有一个relationship  

#### 四、运行效果
打开后页面下方有2个tab item  
默认显示与第一个item相关联的页面
