---
layout: post
title: "PA行为模型"
category: [DPD & PA]
tags: []
---

# 无记忆模型

## Saleh模型

用于描述行波管功放（TWTA）  

AM-AM失真曲线：  
$$
F(\mu) = \frac{\alpha_1\mu}{1+\beta_1\mu^2}
$$

AM-PM失真曲线：  
$$
F(\mu) = \frac{\alpha_2\mu^2}{1+\beta_2\mu^2}
$$

<!-- more -->

## Ghorbani模型

AM-AM失真曲线：  
$$
F(\mu) = \frac{a + \mu^b}{1+c \mu^b} + d\mu
$$

AM-PM失真曲线：  
$$
F(\mu) = \frac{A + \mu^B}{1+C \mu^B} + D\mu
$$

# 有记忆模型

## Volterra级数模型

$$
\begin{aligned}
y(n) = \sum_{k=1}^K y_k(n)   \\
y_k(n) \sum_{q_1=0}^Q \cdots \sum_{q_k=0}^Q h_k(q_1, q_2, \cdots, q_k)\prod_{l=1}^K x(n-q_l)
\end{aligned}
$h_k(q_1, q_2, \cdots, q_k)$：k阶内核  
$x(n-q_l)$：输入信号  
$y(n)$：输出信号  

公式说明：  
K： 非线性的阶数  
Q： 记忆深度  
$$

优点：描述准确  
缺点：计算复杂  

## 记忆多项式模型 MP

k阶内核矩阵内保留对角线位置  
$$
y(n) = \sum_{k=1}^K\sum_{q=0}^Q h_{k,q}x^k(n-q)
$$

复基带形式：  
$$
y(n) = \sum_{k=1}^K\sum_{q=0}^Q h_{k,q} x(n-q)|x(n-q)|^{k-1}
$$

优点：  
描述准确，但计算不复杂  
只考虑奇次阶非线性，k=2l+1  

## GMP

## MPM Momery Polynomial Model

简写：  
$$
y(n) = \sum_{q=0}^Q f_q(x(n-q))
$$

$f_q$为非线性函数  

## NMA 

非线性移动平均，nonlinear moving average

## NARMA模型

ARMA：自回归（auto regressive）移动平均  
NARMA：非线性自回归移动平均

![](http://windmissing.github.io/images/2020/11.png)  
把一组x和一组y分别NL变换后再相加。  

## Wiener模型

## Hammerstein模型

## Wiener-Hannerstein模型