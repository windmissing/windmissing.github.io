---
layout: post
title:  "间接调用虚函数"
category: [编程语言]
tags: [C++, 析构函数]
---

# 错误描述

![](https://img-blog.csdn.net/20180714153718373?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhYnliYWJ5dXA=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

<!-- more -->

# 出错的代码

```python
from urllib import request
headers = { 'User-Agent': 'Mozilla/5.0 Chrome/64.0.3282.186 Safari/537.36', }
url = 'https://xxxxxxxxx'
req = request.Request(url, headers=headers)
response = request.urlopen(req)
data = response.read().decode('UTF-8')
print(data)
```

# 解决方法

```python
from urllib import request
import ssl                     # 新增
headers = { 'User-Agent': 'Mozilla/5.0 Chrome/64.0.3282.186 Safari/537.36', }
url = 'https://xxxxxxxxx'
context = ssl._create_unverified_context()       # 新增
req = request.Request(url, headers=headers)
response = request.urlopen(req, context=context)        # 修改
data = response.read().decode('UTF-8')
print(data)
```

# 参考

https://blog.csdn.net/babybabyup/article/details/81044277
