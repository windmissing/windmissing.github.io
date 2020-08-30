---
layout: post
title:  "非线性的衡量指标"
category: [DPD & PA]
tags: []
---

# 1 dB压缩点 1 dB compression Point 

1 dB压缩点是输入功率范围内的某个值。  
![](http://windmissing.github.io/images/2020/9.png)  
图中的横纵坐标都是dB为单位的功率。  
将PA的线性区的输出功率拟合成一根直线f(x)，对应图中红线。f(x)为输入功率为x时主信道的期望输出功率。    
PA的真实输出功率为g(x)，对应图中蓝线。g(x)为输出功率为x时主信道的真实输出功率。     
1 dB压缩点是满足等式f(x) - g(x) = 1dB的x。  

同理也可以定义出n dB压缩点  

<!-- more -->

# 三阶交调点 Third Order Intercept Point

三阶交调点是输入功率范围内的某个值。    
![](http://windmissing.github.io/images/2020/6.png)  
图中的横纵坐标都是dB为单位的功率。  
将PA的线性区的增益拟合成一根直线f(x)，对应图中上面的直线。f(x)为输入功率为x时主信道的期望输出功率。      
PA的三阶交调项的功率为g(x)，对应图中下面的直线。 g(x)为输出功率为x时的三阶交调项的输出功率。      
三阶交调点是满足等式f(x) = g(x)的x。  

同理也可以定义出n阶交调点。  

# C/IMD = Carrier to Inter-Modulation Distortion Ratio

C/IMD比较是指在输入功率固定的情况下，主频段的输出功率和三阶交调项的输出功率的差异。  
![](http://windmissing.github.io/images/2020/7.png)  
图中的横纵坐标是主频段和交调项的频率范围。其中f1、f2之间为主信道。2f2-f1和2f1-f2为三阶交调信号。3f2-2f1和3f1-2f2为五阶交调信号。纵坐标为频率对应的输出功率。  
CIMD原来是一个比值，因为这里的纵坐标单位是dB，所以表现为两个功率的差值。  

# ACLR = Adjacent Channel Leakage Ratio

ACLR是指在输入功率固定的情况下，主信道的输出功率和邻近信道的输出功率的差异。  
![](http://windmissing.github.io/images/2020/8.png)  
图中的横坐标是根据BW定义的主信道和邻近信道。纵坐标是[?]Power Spectrum Density。  

# 误差向量幅度 = Error Vector Magnitude = EVM

EVM是指参考星座点(向量)和真实星座点（向量）之间的误差（向量）。  
![](http://windmissing.github.io/images/2020/10.png)  

 EVM 用于描述带内失真  
 = 一段时间内，理想参数信号与实际参数信号的向量差的模  
 = 一段时间内，误差向量的有效值 RMS  
 = NMSE

 $$
 \begin{aligned}
 EVM(\%) &=& \sqrt{\frac{\frac{1}{N}\sum|\text{第i个误差向量}|^2}{\frac{1}{N}\sum|\text{第i个参考向量}|^2}} \\
 &=& \sqrt{\frac{\frac{1}{N}\sum|\text{第i个真实向量}-\text{第i个参考向量}|^2}{\frac{1}{N}\sum|\text{第i个真实向量}|^2}}
 \end{aligned}
 $$

# 邻道功率比 = Adjacent Channel Power Ration = ACPR

ACPR用于描述带外失真，即主通道功率泄露到邻道的程度。  

$$
\begin{aligned}
ACPR = \frac{\text{邻道平均功率}}{\text{主频信道平均功率}}   \\
= 10 \lg\frac{\int_{\text{邻}}|P(f)|^2}{\int_{\text{主}}|P(f)|^2}
\end{aligned}
$$

P(f)代表功率谱密度函数，也可以直接用峰值功率或均值功率代替。  


