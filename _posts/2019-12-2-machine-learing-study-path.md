---
layout: post
title:  "Machine Learning自学路线"
category: [Machine Learning]
tags: []
---

# 入门

## 数学

材料：《深度学习》 第一部分 应用数学与机器学习基础  
作者：深度学习的三大开山鼻祖之一Yoshua Bengio  
资源链接：https://pan.baidu.com/s/1GmmbqFewyCuEA7blXNC-7g 密码：6qqm  
学习笔记：https://windmising.gitbook.io/mathematics-basic-for-ml/  
如果学过大学数学的课程（高数、现代、概率论），这个阶段不需要专门地学习数学，只需要把这知识回顾一下。  
《深度学习》 第一部分，总结了机器学习需要的常用的数学基本概念和公式。不涉及推导细节，可直接记住结论。  
在学习基础学习的算法中，对掌握不太好的基础知识查漏补缺即可。  

<!-- more -->

## 算法

材料：《python3入门机器学习 经典算法与应用》   
作者：刘宇波    
资源链接：https://coding.imooc.com/class/169.html   
学习笔记：https://windmising.gitbook.io/liu-yu-bo-play-with-machine-learning   
对常见机器学习算法做了基础的介绍。既有原理也有编程实践。还有一些对算法的思考。  
在讲原理有少量的数学推导，数学基础不好也能看懂。  
简单的算法配有python3实现，复杂算法使用slearn观察算法效果，对算法有直观印象。  
机器学习入门必备。  

## 实践

材料：编译基础语法查询  
python：https://www.runoob.com/python3/python3-tutorial.html  
numpy：https://www.runoob.com/numpy/numpy-tutorial.html  
笔记：https://programmingbasicsforml.netlify.com/readme.html  

材料：《机器学习实战》  
作者：Peter Harrington  
资源链接：链接：https://pan.baidu.com/s/15XtFOH18si316076GLKYfg 密码：sawb   
学习笔记：https://github.com/windmissing/MachineLearningInAction   
网上很多人推荐，因为对算法的介绍比较基础，且配有代码实现。实际感觉质量低于我的预期。   
理论描述废话很多，我不得不从大段的废话中找到一点干货。而真正的干货却没有充分的展开。只介绍了算法过程，而缺少对算法更高层次的解读，不如《python3入门机器学习 经典算法与应用》那样有启发性。代码部分也写得啰嗦，不够简洁优雅。代码的解释虽然很详细，但只是解释了代码在做什么，却没有解释为什么要这样做。  
这本书做为多年来的经典入门书籍，也有他独特的优势。对于广大把编程语言用得比母语还溜的码农来说，通过语言文字来学习算法远不如通过代码学习来得直观。而这本书把十多种经典的机器学习算法用代码实现了一遍，而且对代码解释的详细到几乎是逐行解释了。在这方面目前还没有发现其它资料可以替代。因此，虽然满满的吐槽，还是很认真的把这本书从头到尾看了一遍。
总之，这本书虽然简单，但并不适合完全没有算法基础的人当作入门书籍。适合有算法有一定了解（看过《python3入门机器学习 经典算法与应用》）但编程功底比较弱的人拿来对照练习写代码。或者有编程基础的人通过代码的方式来学习算法。    

# 初级

## 数学

在学习理论和实践的过程中发现，知道一些数学结论可以帮助理解算法的原理和过程，但如果想要自己推导就捉襟见肘的感觉了。  
这是因为对数学基础还不够扎实。在这一阶段就要系统地学习数学基础理论，相比于入门的“知其然”，现在要“知其所以然” 。  
很多攻略都建议不用专门去学习数学基础，用到的时候补一下就可以。  
但我认为，想要学好机器学习，数学是早晚要面对的，不能逃避。而早一点掌握数学基础，就相当于早一点得到学习机器学习的利器。   

《现性代数》推荐：Strang

## 算法

材料：《统计学习方法》  
作者：李航  
资源链接：https://pan.baidu.com/s/1Mk_O71k-H8GHeaivWbzM-Q 密码：adep
学习笔记：https://windmising.gitbook.io/lihang-tongjixuexifangfa/  
网上评价比较好，很多人推荐 

材料：《机器学习》
作者：周志华  
资源链接：https://pan.baidu.com/s/1lJoQnWToonvBU6cYwjrRKg 密码：7rzl
学习笔记：还没开始看  
西瓜书，网上评价比较好，很多人推荐。书上有些公式推导不是很细，需要有一定数学基础。 

## 初级

材料：scikit-learn的官方文档
资源链接：http://sklearn.apachecn.org/cn/0.19.0/
学习笔记：还没开始看
网上推荐的。“有理论有实战，最好的库学习资源，没有之一。”

pandas

# 中级

## 数学

材料：《CS229》配套的数学部分  
作者：吴恩达  
资源链接：https://pan.baidu.com/s/1NrCAW38C9lXFqPwqTlrVRA 密码：3k3m
学习笔记：还没完全看懂  
是对CS229课程的数学补充。将数学知识综合应用到机器学习算法中。经常一个公式里同时包含高数、现代、概率论。对数学要求比较高。

## 算法

材料：《CS229》
作者：吴恩达  
资源链接：https://pan.baidu.com/s/1MC_yWjcz_m5YoZFNBcsRSQ 密码：6rw6
学习笔记：还没完全看懂
与入门的算法介绍不同，这里不再详细说明算法的过程和作用，而是重点在算法的推导过程和背后的原理。  
非常理论，不涉及实践。对数学要求较高。

## 实践

材料：《hands-on-ml-with-sklearn-and-tf》
资源链接：https://pan.baidu.com/s/1x318qTHGt9oZKQwHkoUvKA 密码：xssj
学习笔记：还没开始看
网上推荐的。“不仅能学习到库的应用，还能深入了解工业界的流程解决方案，最好的实战教学书，没有之一。”