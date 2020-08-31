---
layout: post
title: "《通信之道》第3章 笔记"
category: [DPD & PA]
tags: []
---

# 连续系统 VS 离散系统

连续系统以“连续时间t”为自变量：$y(t) = H\{x(t)\}$  
离散系统以“整数n”为自变量：$y[n] = H\{x[n]\}$  
连续系统和离散系统是从自变量的角度去区别的。  
其中：  
$x[n]$代表离散信号第n个点的值，$x(t)$代表模拟信号在t时刻的值    
$x[n] = x(n\Delta t)$  
n可以为正数、负数或0，但必须是整数。  
当n取小数时，x[n]没有意义。当t取小数时，x(t)的意义。  

<!-- more -->

# 模拟系统 VS 数字系统

模拟系统和数字系统是从因变量的取值上去区别的。  

连续&模拟 系统  ---（采样）---> 离散&模拟 系统 ---（A/D）---> 离散&数字系统  


# 线性系统 & 时/移不变系统

- 连续 & 线性 系统

叠加性：两个信号的和的输出 = 两个信号的输出的和  
$$
\begin{aligned}
H\{x_1(t) + x_2(t)\} = H\{x_1(t)\} + H\{x_2(t)\} 
\end{aligned}
$$

数乘性：如果输入信号放大a倍，则输出信号也放大a倍  
$$
H\{\alpha \cdot x(t)\} = \alpha \cdot H\{x(t)\}
$$

- 离散 & 线性 系统

叠加性：两个信号的和的输出 = 两个信号的输出的和  
$$
\begin{aligned}
H\{x_1(n) + x_2(n)\} = H\{x_1(n)] + H\{x_2(n)\} 
\end{aligned}
$$

数乘性：如果输入信号放大a倍，则输出信号也放大a倍  
$$
H\{\alpha \cdot x(n)\} = \alpha \cdot H\{x(n)\}
$$

- 连续 & 时不变 系统

如果输入信号延迟了一段时间$\tau$，那么输出信号也延迟相同的时间。  
$$
y(t-\tau) = H\{x(t - \tau)\}
$$

- 离散 & 移不变 系统

如果输入信号的序号移动m个点，那么输出信号的序号也移动同样的点。  
$$
y[n+m] = H\{x(n+m)\}
$$

# “离散&线性”系统对激励的响应

这一节不是太懂，下面我的理解不一定对  

## 定义

- 离散冲激序列：  
$$
\delta[n] = \begin{cases}
1, n = 0  \\
0, n \neq 0
\end{cases}
$$

- 离散输入信号$x[n]$与脉冲强度序列$\chi$、离散冲激序列$\delta$之间的关系  
*Note，书上离散输入信号和脉冲强度序列用的是同一个符号x，但我觉得是不同的概念，混在一起让人费解*   
$$
x[n] = \sum_{k=-\infty}^\infty \chi[k]\delta[n-k]
$$

- 冲激响应函数  
$$
h[n] = H\{\delta[n]\}
$$

## 根据x[n]计算y[n]

$$
\begin{aligned}
y[n] &=& H\{x[n]\}  && 离散系统的定义  \\
&=& H\{\sum_{k=-\infty}^\infty \chi[k]\delta[n-k]\}  &&  上文中的定义   \\
&=& \sum_{k=-\infty}^\infty \chi[k]H\{\delta[n-k]\}  &&  线性系统的特性   \\
&=& \sum_{k=-\infty}^\infty \chi[k]h[n-k]  &&  冲激响应函数的特性，移不变系统的特性  \\
&=& y[n] = \chi[n] * h[n]
\end{aligned}
$$

最后得到的结果是离散卷积公式   
$$
y[n] = \chi[n] * h[n]
$$

其中，$\chi[n]$脉冲强度，h[n]是系统的冲激响应，反应了系统的特性。  

## 因果系统

如果没有信号输入，系统就没有输出  
n时刻系统的输出信号与该时刻之后的输入信号无关。  
$$
y[n] = \sum_{k=-\infty}^n \chi[k] h[n-k]
$$

# “连续&线性”系统对激励的响应

## 定义

- 冲激函数、狄拉克函数、奇异函数  

$$
\begin{cases}
\int_{-\infty}^{\infty}\delta(t)dt = 1 \\
\delta(t) = 0, t \neq 0
\end{cases}
$$

目的：模拟实际系统中持续时间极短、取值极大的信号

- x(t)是通过\delta(t)对$\chi(t)$的抽样  
$$
x(t_0) = \int_{-\infty}^{\infty} \chi(\tau)\delta(t-\tau)d\tau
$$

- 冲激响应函数  
$$
h(t) = H\{\delta(t)\}
$$

## 根据x(t)计算y(t)

$$
\begin{aligned}
y(t) &=& H\{x(t)\} \\
&=& H\{\int_{-\infty}^{\infty} \chi(\tau)\delta(t-\tau)d\tau\}  \\
&=& \int_{-\infty}^{\infty}\chi(\tau) H\{\delta(t-\tau)\}d\tau  \\
&=& \int_{-\infty}^{\infty}\chi(\tau)h(t-\tau)d\tau  \\
&=& \chi(t) * h(t)
\end{aligned}
$$

## 因果系统

$$
y(t) = \int_{\infty}^t \chi(\tau) h(t-\tau)d\tau
$$

# 卷积的性质

交换率、分配率、结合率

# 遗留问题

1. P35，最后一个公式，等式两个的x是同一个概念吗？  
答：是同一个概念，只是x的两种写法，**这个公式不是一个卷积公式，y[n]那个才是卷积公式**  
2. P36，什么是冲激响应的反折？  
答：例如$[1 2 3 4] * [1 2] = [8 10 7 4]$，先把[1 2 3 4]反过来，再依次取2项与[1 2]做点乘。因此称为反折。  
这里的卷积运算与CNN里的卷积运算不同。CNN里的卷积运算没有反折这一步。[link](https://windmissing.github.io/Bible-DeepLearning/Chapter9/1Convolution.html)  
3. P37，因果系统的概念和公式是怎么扯上关系的？  
答：还是没懂  
4. P38，图3.5没看懂？  
答：一个输入点，经过一次冲激后变成了多个点，这是记忆效应。记忆效应与线性不矛盾。  
5. P42，非线性系统不适合用卷积？  
