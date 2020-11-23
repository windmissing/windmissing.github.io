---
layout: post
title: "Transformer"
category: [Machine Learning]
tags: []
---

Transformer用Attention代替了传统序列转换问题模型中的**recurrent**结构。  
所谓的**recurrent**结构是指存在从当前时间步的hidden state流向下一个时间步的hidden state的数据流动。  
Transformer摒弃了recurrent结构，这不代表在Transformer中每个时间步之间没有关系。实际上在Transformer中，还是存在从当前时间步到下一个时间步的数据流动。下一个时间步使用了当时步的输出。  

![](/images/2020/20.png)  

存在图上红线的路径才叫recurrent结构。Transformer中不存在红线路径，但仍存在绿线路径。  

# Transformer的主要创新点   

## 用Positional Encoding来表达序列顺序信息

### 传统方法：  

1. RNN  
只使用Input Embedding来表示输入数据。  
RNN结构本身包含了序列顺序信息。  
Transformer没有recurrent，用Positional Encoding来表达序列顺序信息。  
2. CNN  
[?] 论文提到了CNN，不知道Transformer跟CNN有什么关系？  

### 本文方法

用Input Embedding + Positional Encoding的方法来表达带序列顺序信息的输入数据
用Output Embedding + Positional Encoding的方法来表达带序列顺序信息的上一个时间步的输出数据   
![](/images/2020/23.png)   
具体步骤：  
1. 生成Positional Encoding  

$$
\begin{aligned}
    PE(pos, 2i) = \sin\left(\frac{pos}{10000^{\frac{2i}{d_{model}}}}\right)   \\
    PE(pos, 2i+1) = \cos\left(\frac{pos}{10000^{\frac{2i}{d_{model}}}}\right)
\end{aligned}
$$

pos：代表序列中的第几个时间步  
i：代表某个时间步的Encoding Vector中的第几个值  
$d_{model}$：PE Vector的长度，与Embedding的长度相同   

以上是本文使用的PE计算方法，称为sinusoidal PE，具有以下特点：  
- [?] forms a geometric progression(几何级数) from $2\pi$ to $10000\cdot 2\pi$  
- [?] for any fixed offset k, PE(pos+k) can be represented as a linear function of PE(pos)。  
- 推断序列可以长于训练序列  

除了本文所用的sinusoidal PE，还有其它PE计算方式，例如learned positional attention[9]。  
从本文实验上看，两种PE算法的性能差不多，选择sinusoidal PE是因为它的第三个特点。  

2. 把Positional Encoding与Input Embedding结合  
貌似只是把两个向量相加  


### 比较

## 改进的注意力机制 Multi-Head Attention

### 传统方法

通过某种算法，将问题向量q、键矩阵K、值矩阵V共同映射成一个特定长度的向量   
也可以把所有n_q个问题向量合并成问题矩阵Q，最后得到n_q个输出向量。  
Q的大小为n_q * d_k，n_q为问题个数，d_k为问题向量的维度。  
K的大小为n_k * d_k，n_k为键值对的个数，d_k为键向量的维度。  
V的大小为n_k * d_v，n_k为键值对的个数，d_v为值向量的维度。    

1. dot-product attention  

![](/images/2020/24.png)   

$$
Attention(Q, K, V) = \text{softmax}(QK^\top)V
$$

softmax的对象是一个n_q * n_k的矩阵。softmax的行为是对矩阵的每一行分别做softmax。即矩阵每一行的和为1。  

2. scaled dot-product attention  

2在1的基础上增加scaled，公式为：  

$$
Attention(Q, K, V) = \text{softmax}(\frac{QK^\top}{\sqrt{d_k}})V
$$

[?] 不明白这里为什么要Scaled，softmax本身就有Scaled的作用。  

3. additive attention

参考文献[2]  

### 本文方法

Multi-Head Attention  
将问题、键、值分别生成几组不同d_k和d_v的矩阵。  
每组用上面的scaled dot-product attention生成一个或（n_q）个输出向量。  
同一个问题对应的所有组输出向量concat到一起，得到一个或（n_q）个长的向量。  

### 比较

## Encoder Unit

### 传统方法

[LSTM](https://windmissing.github.io/Bible-DeepLearning/Chapter10/10Gate/1LSTM.html)  
[GRU](https://windmissing.github.io/Bible-DeepLearning/Chapter10/10Gate/2OtherGates.html)  

### 本文方法

由Attention、FC、residual connection、layer normalization组成的block
![](/images/2020/21.png)   

### 比较

## Decoder Unit

### 传统方法

[LSTM](https://windmissing.github.io/Bible-DeepLearning/Chapter10/10Gate/1LSTM.html)  
[GRU](https://windmissing.github.io/Bible-DeepLearning/Chapter10/10Gate/2OtherGates.html)  

### 本文方法

由Attention、FC、residual connection、layer normalization组成的block
![](/images/2020/22.png)     

### 比较

# Transformer中使用了的技术

attention  
self-attention  
dot-product attention  
Multi-Head Attention  
residual connection[11]  
layer normalization[1]
Softmax  
encoding  

# 其它提到的技术  

factorization tricks[21]  
conditional computation[32]  
additive attention[2]  
learned positional attention[9]
<!-- more -->