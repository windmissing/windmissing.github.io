---
layout: post
title:  "9-7 逻辑回归中使用正则化"
category: [liuyubo play with machine-learning]
tags: []
---

> 这个系列课程不错，墙裂推荐  
> 本文只是对课程内容做笔记，建议读者看原视频学习  
> 因为看本文只能知道一些知识点，但看原视频明理解这些知识点  

在逻辑回归中引入了多项式，模型就会变得复杂，容易出现过拟合。  
解决过拟合一个常规的手段就是在模型中添加正则化。  
新的目标函数可以是：J(theta) + a * L2或J(theta) + a * L1，其中a用于表示正则项的重要程度。  
但在逻辑回归中，通常这样正则化：



<!-- more -->

# 准备数据

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(666)
X = np.random.normal(0, 1, size=(200,2))
y = np.array(X[:,0]**2 + X[:,1]**2 < 1.5, dtype='int')

plt.scatter(X[y==0,0],X[y==0,1])
plt.scatter(X[y==1,0],X[y==1,1])
plt.show()
```

![](http://windmissing.github.io/images/2019/176.png)  

# 使用逻辑回归

```python
log_reg = LogisticRegression()   # 使用9-4中实现的LogisticRegression类
log_reg.fit(X, y)

log_reg.score(X, y)   # score = 0.605
plot_decision_boundary(log_reg, axis=[-4,4,-4,4])   # 使用9-5中的绘制决策边界的函数
plt.scatter(X[y==0,0],X[y==0,1])
plt.scatter(X[y==1,0],X[y==1,1])
plt.show()
```

![](http://windmissing.github.io/images/2019/177.png)  

# 逻辑回归 + 多项式

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

def PolynomialLogisticRegression(degree):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('log_reg', LogisticRegression())   # 遵循sklearn标准构建的类可以无缝结合到管道中
    ])

poly_log_reg = PolynomialLogisticRegression(degree=2)
poly_log_reg.fit(X, y)
plot_decision_boundary(poly_log_reg, axis=[-4,4,-4,4])
plt.scatter(X[y==0,0],X[y==0,1])
plt.scatter(X[y==1,0],X[y==1,1])
plt.show()
```

degree取2时的决策边界：
![](http://windmissing.github.io/images/2019/178.png)  
degree取20时的决策边界：
![](http://windmissing.github.io/images/2019/179.png)  

**Note 1:代码中的LogisticRegression是在9-4中自己实现的类。只要是遵循sklearn标准构建的类可以无缝结合到管道中。**   
**Note 2:逻辑回归中如果使用了多项式，也可以使用与多项式回归相同的正则表达式来约束过拟合的情况。**
