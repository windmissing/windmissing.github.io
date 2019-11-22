---
layout: post
title:  "13-2 soft voting"
category: [liuyubo play with machine-learning]
tags: []
---

> 这个系列课程不错，墙裂推荐  
> 本文只是对课程内容做笔记，建议读者看原视频学习  
> 因为看本文只能知道一些知识点，但看原视频明理解这些知识点  

更合理的投票，应该有权值。  

假如一个二分类问题，5个模型分别对一个样本进行分类。以下是每个模型认为每种分类的概率：  

模型1：A-99%，B-1%   
模型2：A-49%，B-51%  
模型3：A-40%，B-60%  
模型4：A-90%，B-10%  
模型5：A-30%，B-70%  

按照hard voting，投票结果为B  
但考虑上每种类的概率，投票结果为A   
把每个分类的概率当作权值，就是soft voting  

<!-- more -->

soft voting要求集合中的每一个模型都能估计概率   
即有predict_proba这个函数   

逻辑回归，KNN，决策树（叶子结点的每个类的比例），都能估计概率。  
SVM本身没有考虑概率，因为它是计算margin。但SVM可以有一种方法来计算概率。  
# 自己实现集成学习

## 逻辑回归

```python
from sklearn.linear_model import LogisticRegression

log_clf = LogisticRegression()
log_clf.fit(X_train, y_train)
log_clf.score(X_test, y_test)
```

输出：0.864  

## SVM

```python
from sklearn.svm import SVC

svm_clf = SVC()
svm_clf.fit(X_train, y_train)
svm_clf.score(X_test, y_test)
```

输出：0.888   

## 决策树

```python
from sklearn.tree import DecisionTreeClassifier

dt_clf = DecisionTreeClassifier()
dt_clf.fit(X_train, y_train)
dt_clf.score(X_test, y_test)
```

输出：0.84  

## 集成学习

```python
y_predict1 = log_clf.predict(X_test)
y_predict2 = svm_clf.predict(X_test)
y_predict3 = dt_clf.predict(X_test)

y_predict = np.array((y_predict1+y_predict2+y_predict3) >= 2, dtype='int')

from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_predict)
```

输出：0.896  
使用集成学习方法提高了准确率  

# 使用Voting Classifier

```python
from sklearn.ensemble import VotingClassifier

voting_clf = VotingClassifier(estimators=[
    ('log_clf', LogisticRegression()),
    ('svm_clf', SVC()),
    ('dt_clf', DecisionTreeClassifier())
], voting='hard')

voting_clf.fit(X_train, y_train)
voting_clf.score(X_test, y_test)
```

输出：0.896
