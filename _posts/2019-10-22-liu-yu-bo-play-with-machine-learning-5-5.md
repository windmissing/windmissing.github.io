---
layout: post
title:  "5-5 衡量线性回归算法的指标"
category: [liuyubo play with machine-learning]
tags: []
---

> 这个系列课程不错，墙裂推荐  
> 本文只是对课程内容做笔记，建议读者看原视频学习  
> 因为看本文只能知道一些知识点，但看原视频明理解这些知识点  

分类问题使用accuracy来评价分类结果。  
回归问题怎样评价预测结果？

<!-- more -->

# MSE RMSE MAE

## 均方误差 MSE Mean Squared Error

![](http://windmissing.github.io/images/2019/52.png)

问题：量纲

## 均方根误差 RMSE Root Mean Squared Error

![](http://windmissing.github.io/images/2019/53.png)
与MSE本质上是一样的  
放大了最大的错误

## 平均绝对误差 MAE Mean Absolute Error

![](http://windmissing.github.io/images/2019/54.png)

训练过程中，没有把这个函数定义成目标函数，是因为它不是处处可导。  
但它仍可以用于评价算法  
评价一个算法所使用的标准可以和训练时所用的标准不同

# 编程实现三种

```python
import numpy as np

class SimpleLinearRegression2:
    def __init__(self):
        """初始化Single Linear Regression模型"""
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        """根据训练数据集X_train, y_train训练Single Linear Regression模型"""
        assert x_train.ndim == 1, "Simple Linear Regressor can only solve single feature training data"
        assert len(x_train) == len(y_train), "the size of x_train must be equal to the size of y_train"

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = (x_train - x_mean).dot(y_train - y_mean)
        d = (x_train - x_mean).dot(x_train - x_mean)

        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

    def predict(self, x_predict):
        """给定待测数据集X_predict，返回表示x_predict的结果向量"""
        assert x_predict.ndim == 1, "Simple Linear Regressor can only solve single feature training data"
        assert self.a_ is not None and self.b_ is not None, "must fit before predict"
        return [self._predict(x) for x in x_predict]

    def _predict(self, x_single):
        """给定单个待预测数据s_single，返回x_single的预测结果"""
        return self.a_ * x_single + self.b_

    def __repr__(self):
        return "SimpleLinearRegression2()"
```

## 绘制结果

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1., 2., 3., 4., 5.])
y = np.array([1., 3., 2., 3., 5.])

reg2 = SimpleLinearRegression2()
reg2.fit(x, y)

y_hat2 = reg2.predict(x)

plt.scatter(x, y)
plt.plot(x, y_hat2, color='r')
plt.axis([0, 6, 0, 6])
plt.show()
```

输出结果：
![](http://windmissing.github.io/images/2019/50.png)

# 向量化实现的性能测试

```python
m = 1000000
big_x = np.random.random(size = m)
big_y = big_x * 3.0 + 2.0 + np.random.normal(size = m)

%timeit reg1.fit(big_x, big_y)    # reg1见5-4
%timeit reg2.fit(big_x, big_y)
```

输出结果：  
1.15 s ± 12.7 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)  
25.2 ms ± 2.08 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)   

可见向量化计算能大幅度地提高性能，因此能用向量化计算的地方尽量用向量化计算  
