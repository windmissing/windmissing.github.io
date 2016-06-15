---
layout: post 
title:  "scrapy - 通过中间件设置代理"
categories: spider
tags: [python, spider, scrapy, proxy, middleware]
---

#### 一、下载器中间件(Downloader Middleware)

官方定义：下载器中间件是介于Scrapy的request/response处理的钩子框架。 是用于全局修改Scrapy request和response的一个轻量、底层的系统。  
作用：设置了downloader middleware之后，所有的request和response都会使用downloader middleware中定义的规则。  
例如设置代理，那么所有的Request都会基于这个代理来发送请求  

<!-- more -->

#### 二、配置proxy中间件

打开setting.py文件  
找到`DOWNLOADER_MIDDLEWARES`这一项，把注释打开  

```python
DOWNLOADER_MIDDLEWARES = {
    'fetch_csdn_articles.middlewares.MyCustomDownloaderMiddleware': 543,
}
```
这里有一个中间件配置的例子，其中`fetch_csdn_articles`是工程名，`middlewares`是这个中间件实现代码所在的文件名，`MyCustomDownloaderMiddleware`是中间件的名字，也是实现中间件代码的类名  
由于这里是针对proxy的中间件，所以修改中间件的名字为`ProxyMiddleware`  

#### 三、编写proxy中间件

创建文件`middlewares.py`，与setting中的第二项对应  

```
touch middlewares.py
```

`ProxyMiddleware`类，与setting中的第三项对应

写入内容  

```python
# Start your middleware class
class ProxyMiddleware(object):
  # overwrite process request
  def process_request(self, request, spider):
    # Set the location of the proxy
    request.meta['proxy'] = "http://PROXY_IP:PORT"

    # Use the following lines if your proxy requires authentication
    proxy_user_pass = "USERNAME:PASSWORD"
    # setup basic authentication for the proxy
    encoded_user_pass = base64.encodestring(proxy_user_pass)
    request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
```
