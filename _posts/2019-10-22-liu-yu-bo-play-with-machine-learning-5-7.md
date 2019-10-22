---
layout: post
title:  "5-7 简单线性回归和正规方程解"
category: [liuyubo play with machine-learning]
tags: []
---

> 这个系列课程不错，墙裂推荐  
> 本文只是对课程内容做笔记，建议读者看原视频学习  
> 因为看本文只能知道一些知识点，但看原视频明理解这些知识点  

![](http://windmissing.github.io/images/2019/61.png)

<!-- more -->

化简结果：  
构造矩阵Xb
![](http://windmissing.github.io/images/2019/62.png)
要使目标函数最小，必须满足
![](http://windmissing.github.io/images/2019/63.png)

直接使用这个公式求解，  
缺点：时间复杂度太高，O(n^3)  
优点：不需要对数据进行规一化
