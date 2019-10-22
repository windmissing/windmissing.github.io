---
layout: post
title:  "5-10 线性回归的可解释性和更多思考"
category: [liuyubo play with machine-learning]
tags: []
---

> 这个系列课程不错，墙裂推荐  
> 本文只是对课程内容做笔记，建议读者看原视频学习  
> 因为看本文只能知道一些知识点，但看原视频明理解这些知识点  

```python
import matplotlib.pyplot as plt
from sklearn import datasets

boston = datasets.load_boston()
X = boston.data
y = boston.target
X = X[y < 50.0]
y = y[y < 50.0]

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

lin_reg.coef_
```

输出结果：
![](http://windmissing.github.io/images/2019/65.png)

怎么解释这些数字？

<!-- more -->

- 系数的正负代表这个特征与房价是正相关还是负相关  
- 系数的绝对值大小代码这个特征对房价的影响程度  
输入：`boston.feature_names[np.argsort(lin_reg.coef_)]`  
输出：
```
array(['NOX', 'DIS', 'PTRATIO', 'LSTAT', 'CRIM', 'INDUS', 'AGE', 'TAX',
       'B', 'ZN', 'RAD', 'CHAS', 'RM'], dtype='<U7')
```

即使使用线性回归法预测的模型不够好，观察的它的系数对分析问题也是有帮助的。

# 线性回归算法的总结

![](http://windmissing.github.io/images/2019/65.png)

  | 线性回归算法  | KNN算法
--|---|--
模型参数  | 典型的参数学习  | 非参数学习
分类问题  | 是很多分类算法的基础  | 可以解决分类问题
回归问题  | 只能解决回归问题  | 可以解决回归问题 
