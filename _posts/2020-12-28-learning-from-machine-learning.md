---
layout: post
title: "向 机器学习 学习 学习"
category: [随便想想]
tags: []
---

标题应该这样断句：向”机器学习“学习”学习“。  

突飞猛进的”机器学习“技术，不仅给生活带了翻天覆地的变化，还能给机器所学习的领域带来颠覆性的思考，例如研究AlphaGo的棋谱启发出新的围棋战术。同时，对于”机器是如何学习的“这件事本身，对”人类如何学习“也有借鉴的意义。  

大多数ML/DL算法都遵循这样的[套路](https://windmissing.github.io/Water-MachineLearning/CommonSense/1.html#%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E7%9A%84%E6%A1%86%E6%9E%B6)（少数无参数、无迭代的算法剑走偏锋，不在此讨论之列）：  
![](https://windmissing.github.io/Water-MachineLearning/assets/2.png)  

一个算法主要包含三个要素：样本空间（定义一组函数）、损失函数（定义算法目标）、优化算法（定义迭代过程）。  

这三者中，我认为最重要的是损失函数（学习目标）。因为（1）如果样本空间（学习范围）或者优化算法（学习方法）定义错了，学习过程中就能及时发现并改正，但如果损失函数（学习目标）定义错了，只有等到学习结果出来了发现与预期不一致时才会考虑调整目标。（2）不同的学习目标有不同的学习范围和学习方法。比如学ML，目标可以是高参侠、组装侠、科学家，它们的学习范围和方法肯定是不一样的。  

其中重要的是优化方法，也对应学习过程中的学习方法。ML的学习方法很有意思，它暗含了”实践-反馈-调整（再学习）“的闭环思维。把当前参数用于训练数据的前向传播过程就是实践。实践结果$\hat y$与预期结果$y$做比较、分析的过程就是反馈。根据反馈梯度调整学习方向更新参数的反向传播过程就是调整（再学习）。不同的学习目标，“实践-反馈-调整（再学习）”的迭代过程也不同。三个环节缺一不可。如果只是不停地学习而不把学到的东西用于实践，也就无从获取反馈，亦不知自己学到什么程度，在哪里还有欠缺，越学越迷茫。而如果只是一味地解题建模，而不对建模的结果进行深入思考，最终也只是熟练工，而无法得到质的提升，达到最优的那个点。   

最后是模型，是ML中发展变化最大、讨论最多、论文最常见的部分，仿佛模型结构代表了算法的全部。正如学习过程中，说到怎么学习ML，往往会得到一大堆可能推荐者自己都没有看过的学习材料，却少有人会跟你讨论学习目标和学习方法。学习材料也是五花八门，有经典也有旁门左道。好的材料能让你get到ML的精髓，而差的材料可能让人浪费很多时间（收敛慢）、也可能让你云里雾里不得要要领（欠拟合），也可能只是得到一些针对特定问题的tricky（过拟合）。材料的好坏没有一定的标准。它与目标有很大的关系。如果目标是调侠，可以从工程实践类的材料开始。如果目标是组装侠，则需要广泛阅读论文，从别人的成果中获得灵感。如果目标是科学家，也许要先打好数学基础。  

可能天天学ML走火入魔了吧。因为Machine Learning那么高效，把自己也想象成一个Machine，像Machine一样地去Learning。这种想法对我有一些帮助。就我个人的学习经历而言，在学习ML的过程中常常会觉得迷茫，就是犯了“只注重理论学习而忽略实践”的错误。而我以前学习算法时，写了大量的代码做了大量的习题，却忘记了对练习结果做反思总结，虽然练就了不错了编程功底，却始终无法成为真正的高手。  

<!-- more -->