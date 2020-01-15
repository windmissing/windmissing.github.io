layout: post
title:  "ML advice - Debugging Learning Algorithms"
category: [Machine Learning]
tags: []

**Q1：使用Bayesian算法做逻辑回归问题，test error过高怎么办？**

# 常规方法：

- 增加训练数据
- 减少特征
- 增加特征
- 提取新的特征
- 增加迭代次数
- 更换核函数
- 调整超参数
- 使用SVM

这些方法也许有用，但太耗时，而且太考验人品。

<!-- more -->

# 达叔建议

诊断一个到底是什么问题，然后fix这个问题
（这个回答好抽象。。。）

举个粒子：

## 比如你遇到的问题是：过拟合（高方差）、欠拟合（高偏差）

诊断：
过拟合（高方差）：training error明显低于test error
![](http://windmissing.github.io/images/2019/109.png)
欠拟合（高偏差）:training error和test error一样高
![](http://windmissing.github.io/images/2019/110.png)

fix：
高方差问题解决方法：
- 增加训练数据
- 减少特征
高偏差问题解决方法：
- 增加特征
- 提取新的特征

结论：
偏差/方差诊断法是一种常见的诊断方法。
对于其它问题，则需要构建自己的诊断方法来找出问题。

------------------------------------------------

**Q2：Bayesian logistic效率高但错误太高怎么？**

假设Bayesian logistic和SVM的性能如下：

  | error on spam  | error on non-spam  | computational efficiency
--|---|---|--
Bayesian logistic regression  | 2%  | **2%<br>太高，不可接受**  | 高
SVM  | 10%  | 0.01%  | 低

后面的没看懂
