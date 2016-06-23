---
layout: post
title:  "IOS开发 - 导航栏（Navigation Controller）"
category: [ios]
tags: [ios, swift]
---

#### 一、期待目标

<!-- more -->

#### 二、启用Navigation Bar
##### 步骤
1.选中view controller  
2.Editor->Embed in->启用Navigation Controller  
##### 效果：  
（1）页面变成了Navigation Controller  
（2）上方出现了一个灰色区域  
（3）右边多了一个View Controller（页面2）  
（4）当前View Controller与新的View Controller之间有个relationship  
（5）如果当前页面有内容，内容会移到新的View Controller上  

#### 三、增加一个tab item
##### 步骤
0.在页面2上增加一个按钮
1.拖进一个控件View Controller（页面3）  
2.点击页面2中的按钮  
3.Ctrl，同时点击、拖拽至页面3  
4.relationship seque->Show  
##### 效果
页面2与页面3之间有一个relationship  

#### 四、设置标题
1.点击页面2上文灰色区域
2.点击aspect
3.填入title为“message”
4.填入Back Button为“Back"

#### 四、运行效果
打开时显示的是页面2
页面上方是填的title
点击页面2的按时时，页面3从右边进入
点击页面3上方的Back Button，回到页面2
