---
layout: post
title:  "6-9 有关梯度下降法的更多深入讨论"
category: [liuyubo play with machine-learning]
tags: []
---

> 这个系列课程不错，墙裂推荐  
> 本文只是对课程内容做笔记，建议读者看原视频学习  
> 因为看本文只能知道一些知识点，但看原视频明理解这些知识点  

- 批量梯度下降法 Batch Gradient Descent，缺点：慢，优点：稳定  
- 随机梯度下降法 Stochastic Gradient Descent，优点：快，缺点：不稳定  
- 小批量梯度下降法 Mini-Batch Gradient Descent，以上两种结合  

<!-- more -->

# 随机

随机梯度下降法可以跳出局部最优解  
随机梯度下降法运行速度更快  
机器学习领域很多算法都要使用随机的特点，例如随机搜索、随机森林
