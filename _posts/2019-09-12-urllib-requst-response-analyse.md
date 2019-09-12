---
layout: post
title:  "使用urllib获取页面以及解析页面"
category: [编程语言]
tags: [python]
---

虽然现在有很多爬虫框架可以帮我们方便地爬取页面。

但框架在方便的同时会有各自的限制。并且有很时只是要简单地获取一些信息，没有必要使用框架，使用urllib就能很简单地实现目标。

```python
from urllib import request
headers = { 'User-Agent': 'Mozilla/5.0 Chrome/64.0.3282.186 Safari/537.36', }
url = 'https://xxxxxxxxx'
req = request.Request(url, headers=headers)
response = request.urlopen(req)
data = response.read().decode('UTF-8')
print(data)
```

<!-- more -->

这大概是最简单的爬虫程序了。

response.read()读出来的是string，要从string中解析出想要信息很难。此时可以借助lxml。

使用`pip install lxml`安装lxml

```python
from lxml import etree
from urllib import request

headers = { 'User-Agent': 'Mozilla/5.0 Chrome/64.0.3282.186 Safari/537.36', }
url = 'https://xxxxxxxxx'
req = request.Request(url, headers=headers)
response = request.urlopen(req)
data = response.read().decode('UTF-8')
html = etree.HTML(response.read().decode('utf-8'))
title = html.xpath('xxxxxxxxx')[0]
print title.text
```

# 提取xpath

（1）用chrome打开目标页面，找到要想获取的元素

（2）点击“尾页” -> 右键 -> inspect -> copy -> xpath

目标元素的xpath就存在于剪贴版中了

目前碰到的问题：

如果目标元素是table中的一个元素，复制到的xpath是这样的：

`/html/body/div[2]/table[4]/tbody/tr[2]/td[2]/p/span`

这个path解析不出来，要把tbody去掉，即

`/html/body/div[2]/table[4]/tr[2]/td[2]/p/span`

# 参考链接

[常见python爬虫框架](https://www.cnblogs.com/Lijcyy/p/9778318.html)。

如果提示CERTIFICAYE_VERIFY_FAILED参考[link](http://windmissing.github.io/%E7%BC%96%E7%A8%8B%E8%AF%AD%E8%A8%80/2019-09/urllib-error-certificated-verify-failed.html)解决。

response的用法参考[link](https://blog.csdn.net/topleeyap/article/details/78845946)。

reponse读的页面保存到文件[link](https://blog.csdn.net/qq_22521211/article/details/80052085)

Python使用lxml解析HTML response[link](https://blog.csdn.net/zjuxsl/article/details/76975956)

提取xpath[link](http://windmissing.github.io/spider/2016-02/scrapy-fetch-csdn-articles.html)
