---
layout: post
title: "基于scrapy的爬虫小练习 - 准备工作"
category: spider
tags: [spider, scrapy]
---

#### 一、准备工作

##### 1、什么是Scrapy？

（1）一个用python实现的开源项目

（2）爬虫框架

##### 2.安装 

Red hat直接使用yum安装

```
yum install scrapy
```

<!-- more -->

#### 二、创建scrapy工程

##### 1.创建工程目录

```
scrapy startproject csdn
```
![](/image/scrapy-prepare-1.png)

##### 2.发生了什么？

![](/image/scrapy-prepare-2.png)

```
csdn # 工程根目录
  | ----   scrapy.cfg
  | ----   csdn
             | ---- __init__.py
             | ---- items.py
             | ---- pipelines.py
             | ---- seetings.py
             | ---- spiders # 在这个文件夹里添加源代码
                       | ---- __init__.py
```

#### 三、创建一个爬虫项目

##### 1.在工程根目录创建一个爬虫项目

```
scrapy genspider read_csdn_article blog.csdn.net
```
其中`read_csdn_article`是项目的名字，`blog.csdn.net`是爬取的范围

![](/image/scrapy-prepare-3.png)

##### 2.发生了什么？

在csdn/spider下多了一个文件dmoz_spider.py

```python
# -*- coding: utf-8 -*-
import scrapy


class ReadCsdnArticleSpider(scrapy.Spider):
    name = "read_csdn_article"
    allowed_domains = ["blog.csdn.net"]
    start_urls = (
        'http://www.blog.csdn.net/',
    )

    def parse(self, response):
        pass
```
    
#### 四、运行爬虫项目

##### 1.修改起始页面

scrapy默认把爬取范围自动加上`http://www.`这样的头，就成了爬虫的起始页面了，但这个页面并不我们的目标，要把start_urls设置成真正想爬取的网页

```python
start_urls = (
         'http://blog.csdn.net/mishifangxiangdefeng',
     )
```

##### 2.进入项目根目录，执行

```
scrapy crawl read_csdn_article
```
当然，什么也没有爬到，因为到目前为止还只是一个框架，没有实际的内容

![](/image/scrapy-prepare-4.png)

#### 五、参考链接

http://scrapy-chs.readthedocs.org/zh_CN/latest/intro/tutorial.html
