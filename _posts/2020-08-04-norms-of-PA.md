---
layout: post
title: "PA相关中英文术语"
category: [DPD & PA]
tags: []
---

|英文|中文|解释|
|---|---|---|
|adjacent channel|邻信道||
|ambient temperature|环境温度||
|amplitude|幅度||
|amplitude modulated signal|调幅信号|
|analog circuitry|模拟电路||
|angular frequency|角频|角速度标量，单位：弧度/秒|
|bandpass signal|带通信号|把基带信号经过载波调制后,把信号的频率范围搬移到较高的频段以便在信道中传输(即仅在一段频率范围内能够通过信道)。<br>由于每一路基带信号的频谱被搬移到不同的频段上,因此合在一起后并不会互相干扰。这样做可以在一条线路中同时传送许多路的数字信号,因而提高了线路的利用率。|
|bandwidth|带宽||
|code division multiplexing|CDMA 码分复用||
|complex modulation cheme|复数调制||
|crest factor reduction|CFR[?]|[?]|
|DC operating point|直流工作点|又叫静态工作点。就是输入信号为零时,电路处于直流工作状态,这些直流电流,电压的数值在三极管特性曲线上表示为一个确定的点,设置静态工作点的目的就是要保证在被被放大的交流信号加入电路时,不论是正半周还是负半周都能满足发射结正向偏置,集电结反向偏置的三极管放大状态.|
|direct current|直流电路||
|drain efficiency|[?]<br>drain是PA内部某个位置的硬件|=输出功率/消耗功率|
|drain voltage|漏电压||
|driving signal|驱动信号||
|envelop|包络|原来等bai幅振荡的脉冲信号，经过调du制之后，每次振荡的幅度会有变化，zhi把每次振荡信号的最dao高点和最低点分别用虚线连接起来，虚线的形状就是脉冲信号的包络。|
|envelop bandwidth|包络带宽|包络信号也是一个新的脉冲信号（周期更大），这个脉冲信号在时间上观察也会有一定的宽度（每个周期内会有一段时间为0），这是时间上宽度就是脉冲包络宽度。<br>脉冲的带宽和脉冲宽度成反比，即脉冲时间上的宽度越窄，频谱上的带宽越大<br>不是IBW|
|envelop fluctuation|包络波动||
|fractional bandwidth|分数带宽|分数带宽(fractionalbandwidth)BW3dB/f0×100[%],也常用来表征滤波器通带带宽|
|frequency response|频率响应|与频率相关联的变化关系，即因频率变化而导致的信号相位幅度的变化<br>flat：相位、幅度对不同频率的响应是一致的|
|frequency up-conversion|上变频|将基带信号的频谱移到所需要的较高载波频率上。<br>优点：抗干扰能力强、频率响应平坦|
|fundamental frequency|基频||
|gate voltage|触发电压||
|harmonic|谐波||
|in-band|带内||
|in-phase|同相||
|in-phase/quadrature|I/Q 同相正交||
|in-band third order inter-modulation products|带内三阶交调产物|角频为$2\omega_1-\omega_2$或$2\omega_2-\omega_1$的分量|
|instantaneous bandwidth|IBW|房产证面积，与OBW相比较|
|instantaneous complex gain|瞬时复数增益|
|integration bandwidth|积分带宽|[?]频谱仪上的概念|
|inter-modulation|交调||
|Junction Temperature|结温|电子设备中半导体的实际工作温度。在操作中，它通常较封装外壳温度（Case Temperature）高。温度差等于其间热的功率乘以热阻。|
|low-pass equivalent signal|低通等效信号|带通信号经过下变频得到低通等效信号，低能等效信号经过IQ调制得到基带信号|
|magnitude|幅度|amplitude VS. magnitude，前者有符号，后者没有符号|
|modulated signal|调制信号||
|narrow band|窄带|信号带宽远小于中心频率的是窄带信号，带宽能和中心频率相比拟或着是远大于中心dao频率的信号是宽带信号。<br>窄带信号的功率集中在中心频率附近，两者的功率谱密度和频谱密度图有很大的差距。处理方法也有很大差距。|
|orthogonal frequency division multiplexing|OFDMA 正交频分复用||
|occupied bandwidth|OBW|实际面积，与IBW相比较|
|out-of-band|带外||
|output power back-off|OPBO 输出功率回退|
|peak-to-average power ration|PAPR 功率峰均比||
|phase|相位||
|phase modulated signal|调相信号|相位随时间变化的信号|
|piecewise-linear limiter|分段线性限制器|[?]|
|power spectrum density|功率谱密度|[?]|
|quadrature amplitude modulation|正交调幅||
|quadrature component|正交分量|
|reference constellation point|参考星座点|[?]|
|small signal|小信号|DAC到PA之间的信号|
|spectrum emission mask|频谱发射掩模|[?]|
|spectrum regrowth|频谱再生||
|two-tone signal|双频信号|$x(t) = A_1 \cos (\omega_1t) + A_2 \cos(\omega_2 t)$|
|volterra series|沃尔泰拉级数|沃尔泰级数是非线性行为中的一种模型，类似于泰勒级数。它不同于泰勒级数的地方在于能够捕捉记忆效应。在非线性系统中，泰勒级数能够用于对输入的响应的逼近，如果在特定的某个时间内，输出是严格取决于输入的。对于沃尔泰级数，非线性系统的输出取决于任何其他的时间内的输入。这种属性使得其有能力捕捉一些器件的记忆效应，比如电容和电感。|
|wireless transmitter|无线发射器||