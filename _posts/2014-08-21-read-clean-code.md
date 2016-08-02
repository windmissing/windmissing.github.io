---
layout: post
title:  "读《代码整洁之道》"
category: [dojo]
tags: [clean code, updating]
---

#### 一、从clean中得到的收获

1.发现算法逻辑上的问题  
2.更好地理解算法  
3.发现BUG时，迅速定位到是哪个函数  
4.看到代码在进步，很开心  
5.看到哪里不爽就可以放心地改掉，而不用担心会引入什么问题  
6.对原有算法有了新的想法  

#### 二、测试

测试是clean code的基础，没有测试用例的code不是clean code  
因为有了高覆盖率的测试，才敢放手去优化代码  
开发与写测试例同时进行，让代码的每个分支都被测试用用例覆盖到

##### 1.UT框架

有许多比较好的测试框架可以直接使用：  
 - gtest：  
貌似用得的比较多，很容易能搜到使用方法  
http://windmissing.github.io/linux/2016-01/build-gtest-in-linux.html  
 - CPPUTest：
怎么把CPPUTest用到VS中：  
http://www.cnblogs.com/wanghonggang/archive/2013/03/13/CppUTest_in_Visual_Studio_2010.html  
 - VS自带UT：  
网上资料比较多。  
需要结合/clr:safe，却又和/MT冲突，最后没搭起来  

##### 2.UT用例

#### 三、命名

[通过《算法导论》学习《代码整洁之道》——有意义的名称  ](http://windmissing.github.io/dojo/2014-10/learn-clean-code-from-algorithm.html)

#### 四、函数

参数尽量少  
函数要短小  

#### 五、注释
不要写注释，因为修改代码时一般不会同步修改注释  
要写注释是因为代码的表达能力不够，这时应该考虑如何让代码的表达力更好  
以下三种情况可以写注释：  
（1）版权作息  
（2）为什么要这样做，而不是要做什么  
（3）正则表达式  

#### 六、（还在看）

