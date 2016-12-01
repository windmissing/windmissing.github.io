---
layout: post 
title:  "scrapy - 通过设置agent client解决401问题"
categories: spider
tags: [python, spider, scrapy, agent client, middleware, 401]
---

#### 一、问题现象  

在使用scrapy爬取有些网页时会返回401错误，如图所示：  
![](/image/401-error-from-scrapy.jpg)  
401错误是指认证失败，一般有两个原因：  
1.登陆网页需要提供用户名、密码，而没有提供或者提供的不正确  
2.服务器做了客户端过滤，只允许浏览器访问，而不允许spider访问  
本文只解决原因2导致的401错误，对于原因1的解决方法，请参考[《scrapy - 模拟登陆》](/spider/2016-06/scrapy-login.html)  

<!-- more -->

#### 二、服务器是怎么对客户端过滤的？
    
##### 1.什么是agent client  

agent client是指访问服务器所使用的客户端  
浏览器向服务器发送POST消息时，把这个内容放在消息的`User-Agent`中发给服务器  
有些服务器对验证`User-Agent`的内容，只对认识的agent-client放行否则返回401错误  

##### 2.如何获取agent client

那么`User-Agent`填的是什么呢？可以在浏览器访问页面时同时抓消息查看  
chrome提供这样的功能，以chrome为例：

 - 打开chrome浏览器  
 - 右键->Inspect -> network  
 - 登陆网页  
![](/image/inspect-network.jpg)
 - 选择其中一条查看，找到`User-Agent`  
![](/image/request-headers-agent-client.jpg)  
本文得到的`User-Agent`是`'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'`  

#### 三、为request配置agent client

##### 1.配置多个agent client  

既然服务器只是通过检查`User-Agent`字段来判断客户端类型的，那么只需要在requst中填上可用的agent client可以骗过服务器。  
为了伪装的更像客户端，可以准备多个可用的agent client，在每次访问时随机地使用一种。  
在setting.py中加入这样的内容  

```python
USER_AGENTS = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
               'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
               'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
               'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0']
```

##### 2.配置中间件  

配置中间件的作用是使每一次request都会使用USER_AGENTS  

```
DOWNLOADER_MIDDLEWARES = {
    'meeting_room.middlewares.RandomUserAgent':543,
}
```

##### 3.编写中间件代码

在`middlewares.py`中加入这样的代码：  

```python
import settings
import random

class RandomUserAgent(object):
  """Randomly rotate user agents based on a list of predefined ones"""
  def __init__(self, agents):
    self.agents = agents
  @classmethod
  def from_crawler(cls, crawler):
    return cls(crawler.settings.getlist('USER_AGENTS'))
  def process_request(self, request, spider):
    request.headers.setdefault('User-Agent', random.choice(self.agents))
```

#### 四、运行效果  
![](/image/scrapy_pass_401.jpg)
