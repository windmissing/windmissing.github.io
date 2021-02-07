---
layout: post
title: "learn from nmt attention"
category: [随便想想]
tags: []
---

一个算法由多个组件组成, 例如encoder, attention, decoder.有两种方法实现.两种我都试了,最终选择了第二种.  
(1) 可以定义多个model,在自定义的process函数中把这几个模型结合起来, 由GradientTape跟踪计算process的梯度,自定义迭代过程.   
好处:  
- 每个组件用一个model定义,组件之间的关系更清楚  
- 每个组件都可以用Sequential实现,组件结果更明确,替换成方便.  
- 自定义的process过程和迭代过程,使用更灵活.  
- 通过在process中加打印来分析迭代过程,debug更方便.  

(2) 可以把所有组件定义到一个model中,不同组件之间的结合也都放到这个model中,用正常的model使用方法来使用这个model  
好处:   
- 可以直接使用model.compile和model.fit提供的功能,例如迭代, 打印, 验证.  
- model.summary可以查看完整的模型信息  



GrandientTap内的所有操作都必须使用tensorflow支持的操作,否则无法计算梯度.尤其注意不能使用相同功能的numpy函数.  

ML的debug很玄学.即使代表写错了,也能正常运行,只是结果拟合效果不好而已.而中间过程又是大量的数字,无从Debug.在NMT attention的debug过程中学到了一些很初步的Debug方法:  
(1)保证loss的是下降的,如果没有,调一下learning rate.如果无法保证loss下降,说明程序中最基本的迭代流程都是有问题的,  
(2)保证`val_loss`是下降的.验证集不参与训练,因此`val_loss`是对当前模型状态的客观评价.如果`val_loss`在下降,至少代码没有大问题.  
(3)打印中间信息时,把样本数和迭代次数设置为1,减少信息量.  
