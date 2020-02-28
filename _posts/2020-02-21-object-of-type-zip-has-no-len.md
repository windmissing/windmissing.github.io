---
layout: post
title:  "object of type 'zip' has no len()"
category: [编程语言]
tags: []
---

**代码：**  

在python3.x下使用如下代码：  
```python
test_data = zip(test_inputs, te_d[1])
n_test = len(test_data)
```

**错误：**  

```
object of type 'zip' has no len()
```

<!-- more -->

**原因：**  

python2与python3的不同

**解决办法：**  
先把zip转成list再求len 
```python
test_data = list(zip(test_inputs, te_d[1]))
n_test = len(test_data)
```