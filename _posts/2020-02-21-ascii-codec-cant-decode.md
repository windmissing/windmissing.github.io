---
layout: post
title:  "'ascii' codec can't decode byte 0x90 in position 614: ordinal not in range(128)"
category: [编程语言]
tags: []
---

**代码：**  

在python3.x下使用如下代码：  
```python
pickle.load(f)
```

**错误：**  

```
'ascii' codec can't decode byte 0x90 in position 614: ordinal not in range(128)
```

<!-- more -->

**原因：**  

python编码问题

**解决办法：**  
指定编码方式   
```python
pickle.load(f,encoding='bytes')
```