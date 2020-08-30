---
layout: post
title:  "PA的非线性"
category: [DPD & PA]
tags: []
---

# 什么是非线性

假设不考虑PA的记忆效应，在特定设备的频率的情况下，输入的功率与输出的功率呈非线性关系，如图  
![](http://windmissing.github.io/images/2020/2.png)  
注意：横坐标与纵坐标都是功率（单位db）。  
并非PA的整个工作区间都是非线性的，它为分线性区与饱和区。  

<!-- more -->

PA的非线性会导致：  
1. 带外频谱扩展 --- 邻道干扰 ACI  
2. 带内传输信号失真 --- 误码率BER 性能下降

问：功率和幅度是什么关系？  
答：I的幅度的平均 + Q的幅度的平均 = 功率

# 非线性有什么影响

## AM-AM失真

假设P(A)中无记忆的。定义：  
$$
\begin{aligned}
v_{out}(t) = f(v_{in}(t))   && (1)
\end{aligned}
$$

其中：  
$v_{in}(t)$是t时刻是输入幅度，$v_{out}(t)$是t时刻的输出幅度。  
f是某种非线性函数，定义为：  
$$
\begin{aligned}
f(x) = k_1x + K_2x^2 + k_3x^3 + \cdots   && (2)
\end{aligned}
$$

再假设输入信号为某种单频信号：  
$$
\begin{aligned}
v_{in}(t) = V \cos wt   && (3)
\end{aligned}
$$

把（2）和（3）代入（1）得：  
$$
v_{out}(t) = [\cdots] + [\cdots] \cos wt +  [\cdots] \cos 2wt + [\cdots] \cos 3wt + ...
$$

以上的$v_{out}(t)$看上去复杂，具体可以分成三种分量。公式中的$[\cdots]$代表某个暂时不需要关系具体值，是这些分量的系数。  

|分量|成分|
|---|---|
|直流分量|$[\cdots]$|
|基波分量|$(k_1V + \frac{3}{4}K_3V^3) \cos wt$|
|谐波分量|$[\cdots] \cos 2wt + [\cdots] \cos 3wt + ...$|

重点关心基波分量：  
$$
(k_1V + \frac{3}{4}K_3V^3) \cos wt  = (k_1 + \frac{3}{4}K_3V^2)V\cos wt
$$

定义:  
k1为线性增益。  
$\frac{3}{4}K_3V^2$为线性失真项。  

当K3<0时，$(k_1V + \frac{3}{4}K_3V^3) \cos wt < K_1 V \cos wt$，称为增益压缩  
当K3>0时，$(k_1V + \frac{3}{4}K_3V^3) \cos wt < K_1 V \cos wt$，称为增益扩张    
PA属于第一种。  
![](http://windmissing.github.io/images/2020/3.png)  

## 互调失真 IMD

上一页提到，一个单频信号经过PA的非线性失真，会得到三种分量。现在考虑双频信号：　　
$$
v_{in}(t) = A_1\cos w_1t + A_2\cos w_2 t
$$

这个双频信号由两个步骤和幅度都不同的单频信号组成，得到的输出为：  

|分量|成分|作用|
|---|---|---|
|直流项|$[\cdots]$|无干扰|
|基波项|$a\cdot [A_1\cos w_1t + A_2\cos w_2 t]$ | 线性增益|
||$[\cdots]\cos w_1 t+ [cdos]\cos w_2 t$|主信道失真|
|谐波项|$[\cdots]\cos 2w_1 t+ [cdos]\cos 2w_2 t + \cdots$|无干扰|
|互调项|$[\cdots]\cos(2w_1 - w_2)t$ + $[\cdots]\cos(2w_2 - w_1)t$|带内邻信道干扰|
||$[\cdots]\cos(\pm rw_1 \pm sw_2)t$|无干扰|

互调项中，带外部分直接使用滤波器过滤掉，不会成为问题。  
带内部分可能会成为问题。 

公式里使用了两个离散的频率值来做计算，实际上频率值是连续的。  
也就是说，真实场景的输入信号中，会有很多w混在一起，且这些w彼此非常接近。  
基于这样的w的前提，类似于w1+w2, w1-w2这样的频率肯定是带外的。类似于2w1-w2, 2w2-w1这样的频率是带内的，是会产生干扰的。  

## AM-PM失真

输入信号幅度变化时输出信息相位失真。  

以上公式只是用了一个正弦曲线来表示输入数据。实际上输入数据是两路相互正交的正弦曲线。  
![](http://windmissing.github.io/images/2020/4.jpg)  
用另一种图来表示会更加直观：  
![](http://windmissing.github.io/images/2020/5.png)  
图中同心圆上的点幅度相同，相位不同。斜线上的点，相位相同，幅度不同。  
假设期望out的点为图点，实际out的点为灰点。图a称为相位失真，图b称为幅度失真。图c称为幅度和相位同时失真。

## PM-AM、PM-PM

PA不会引入这两种失真。  
这两种失真是因为：  
1. gain and phase imbalances in the frequency up-conversion(上变频) stage  
2. 发射器has a non-flat frequency response over a bandwidth equal to that of the input signal  
解决方法：  
发射器的careful design    
本文不考虑这种失真。   

# 怎样解决非线性

## 输出功率回退

前面介绍过，PA的工作区间分为线性区和饱和区。  
可以限制PA始终工作在线性性。  
实验数据表明：  
在线性区间线性程度好，但工作效率低。  
在饱和区间线性程度低，但工作效率高。  

## DPD

DPD + PA = 线性PA  
使用DPD方法，在得到线性效果的同时保证比较好的工作效率。  
