---
layout: post
title:  "8-10 L1,L2和弹性网络"
category: [liuyubo play with machine-learning]
tags: []
---

> 这个系列课程不错，墙裂推荐  
> 本文只是对课程内容做笔记，建议读者看原视频学习  
> 因为看本文只能知道一些知识点，但看原视频明理解这些知识点  

![](http://windmissing.github.io/images/2019/152.png)

将类似的思想应用于不同的场景，就成了不同的名词。  
其实这些名词背后的数学原理是非常想像的。  

<!-- more -->

![](http://windmissing.github.io/images/2019/153.png)  

在正则化过程中，通常不会使用n>=3的正则项，但理论上是存在的。  

L0正则项如下：  
![](http://windmissing.github.io/images/2019/154.png)  
求L0正则项是一个NP难问题，所以也不使用。  
如果要限制theta的个数，则使用L1代替L0。

# 弹性网 Elastic Net

超参数r表示两种正则项之间的比例  
同时结合了岭回归和lasso回归的优势  
在实际应用中通常都先尝试岭回归   
但如果特征特别多，岭回归的计算量会特别大，此时优先选择弹性网。  
lasso回归则急于将特征化为0，可能会产生一些错误，使得结果偏差较大。  

# 其他

批量梯度下降法 + 随机梯度下降法 = 小批量梯度下降法  
岭回归 + lasso回归 = 弹性网  
