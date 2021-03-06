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

在入门阶段，只直学习别人已经推好的公式，以前的数学知道还勉强够用。到了初级阶段，跟着课本一起推公式时就有些吃力了。  
这是因为对数学基础还不够扎实。在这一阶段就要系统地学习数学基础理论，相比于入门的“知其然”，现在要“知其所以然” 。  
很多攻略都建议不用专门去学习数学基础，用到的时候补一下就可以。  
但我认为，想要学好机器学习，数学是早晚要面对的，不能逃避。而早一点掌握数学基础，就相当于早一点得到学习机器学习的利器。   

《现性代数》：推荐Strang
《概率论》：还没找到比较好的材料

## 算法

材料：《统计学习方法》  
作者：李航  
资源链接：https://pan.baidu.com/s/1Mk_O71k-H8GHeaivWbzM-Q 密码：adep
学习笔记：https://windmising.gitbook.io/lihang-tongjixuexifangfa/  
《统计学习方法》的前面七章仍然是讲基础的机器学习算法。这些算法已经在《python3入门机器学习 经典算法与应用》和《机器学习实战》中学过很多次了。此时对这些算法已经有了基本的了解。  
但《python3》和《机器》的定位是入门学习，在介绍算法过程中使用的语言是非专业性的语言。而《统计》的定位是初级，虽然算法上没有讲得太深入，但语言上使用的专业语言。因此在《统计》中会学到大量术语和公式。这让没有基础的同学有点晕。  
如果《python3》和《机器》的基础打得比较好，此时只是学习用专业性的术语和严谨的数据公式来描述已经熟知的内容，就不会觉得太难，反而是学习术语和公式推导的好机会。  

材料：《CS229》
作者：吴恩达  
资源链接：https://pan.baidu.com/s/1MC_yWjcz_m5YoZFNBcsRSQ 密码：6rw6
学习笔记：看的时候不是太懂，就没做笔记。现在转向转向深度学习了。这个计划就搁置了。
第一次读这个材料时痛不欲生，因此把它归为“中级”。实际上仔细想想，其实它在算法本身的介绍上并没有那么难。主要还是对算法过程的讲解。对于公式的推导和算法更深层次的解读不是太多。涉及到的数学概念基本上都是大学数学的知识。所以又把它移到了的初级。  
既然它本身算法方向没有那么难，那么它难在哪？因为它有英语和术语的加成。对于很多人来说，英语本身就是一个坎。尤其是当英语和术语结合的时候。我们大部分在学习数学都用的中文材料，算法入门用的也是中文材料。其中的数学术语和算法术语都是中文的。但翻译成英文就不一定认识了。阅读英文材料时，里面本来包含了一个很熟悉的术语，但如果没有刻意去查，有些可能查普通词典还不一定查得到，就会把它当作一个陌生的词语，这就影响了阅读。  
这个材料适合英文比较好的同学使用。阅读前把各种术语的英文版撸一遍会大有帮助。  

## 初级

材料：scikit-learn的官方文档
资源链接：http://sklearn.apachecn.org/cn/0.19.0/
学习笔记：转向深度学习了。这个计划就搁置了。  
网上推荐的。“有理论有实战，最好的库学习资源，没有之一。”

pandas

# 中级

## 数学

材料：《CS229》配套的数学部分  
作者：吴恩达  
资源链接：https://pan.baidu.com/s/1NrCAW38C9lXFqPwqTlrVRA 密码：3k3m
学习笔记：看的时候不是太懂，就没做笔记。现在转向转向深度学习了。这个计划就搁置了。    
是对CS229课程的数学补充。将数学知识综合应用到机器学习算法中。经常一个公式里同时包含高数、现代、概率论。对数学要求比较高。

## 算法

材料：《机器学习》
作者：周志华  
资源链接：https://pan.baidu.com/s/1lJoQnWToonvBU6cYwjrRKg 密码：7rzl
学习笔记：还没开始看  
西瓜书，网上评价比较好，很多人推荐。书上有些公式推导不是很细，需要有一定数学基础。 

## 实践

材料：《hands-on-ml-with-sklearn-and-tf》
资源链接：https://pan.baidu.com/s/1x318qTHGt9oZKQwHkoUvKA 密码：xssj
学习笔记：看的时候不是太懂，就没做笔记。现在转向转向深度学习了。这个计划就搁置了。
网上推荐的。“不仅能学习到库的应用，还能深入了解工业界的流程解决方案，最好的实战教学书，没有之一。”

# 高级

我也不知道，因为我自己还只是初级，想像不出高级的大佬时是怎么学习的。  
我想，可以考虑阅读sklearn的源码。  