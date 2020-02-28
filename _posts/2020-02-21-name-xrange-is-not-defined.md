---
layout: post
title:  "NameError: name 'xrange' is not defined"
category: [编程语言]
tags: []
---

**代码：**  

在python3.x下使用如下代码：  
```python
for j in xrange(epochs):
```

**错误：**  

```
NameError: name 'xrange' is not defined
```

<!-- more -->

**原因：**  

在Python 3中，range()与xrange()合并为range( )。  

**解决办法：**  
将xrange( )函数全部换为range( )。  
```python
for j in range(epochs):
```