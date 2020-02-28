---
layout: post
title:  "ImportError: No module named 'cPickle'"
category: [编程语言]
tags: []
---

**代码：**  
  
```python
from theano.tensor.signal import downsample
pooled_out = downsample.max_pool_2d(
       input=conv_out,
       ds=poolsize,
       ignore_border=True
)
```

**错误：**  

```
ImportError: cannot import name 'downsample' from 'theano.tensor.signal'
```

<!-- more -->

**原因：**  

theano库的接口变更

**解决办法：**  
 
```python
from theano.tensor.signal import pool
pooled_out = pool.pool_2d(
     input=conv_out,
     ws=poolsize,
     ignore_border=True
)
```