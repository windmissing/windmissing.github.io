---
layout: post
title:  "ImportError: No module named 'cPickle'"
category: [编程语言]
tags: []
---

**代码：**  

在python3.x下使用如下代码：  
```python
import cPickle as pk
```

**错误：**  

```
ImportError: No module named 'cPickle'
```

**原因：**  

python2有cPickle，但是在python3下，是没有cPickle的；

**解决办法：**  
将cPickle改为pickle即可，代码如下：  
```python
import pickle as pk
```