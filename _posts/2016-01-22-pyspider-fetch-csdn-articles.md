---
layout: post 
title:  "基于pyspider的爬虫小练习 - 获取CSDN某个用户的所有文章"
categories: spider
tags: [python, spider, pyspider]
---

#### 一、获取首页中所有关于文章的链接

针对首页的回调函数在`index_page`中实现，这个函数的的行为是分解出首页中所有带超链接的pyquery对象

```python
@config(age=10 * 24 * 60 * 60)
def index_page(self, response):
    for each in response.doc('a[href^="http"]').items():
        self.crawl(each.attr.href, callback=self.detail_page)
```

但不是所有的超链接都是我们需要的指向文章的超链接，这里需要用正则表达式把需要的对象过滤出来。

<!-- more -->

观察这些超链接，发现指向文章的超链接都是以`http://blog.csdn.net/mishifangxiangdefeng/article/details/`开关后面跟若干位数字

在python的正则表达式中，`\d`表示数字，`*`表示任意数量的任意字符，`$`表示结束符

```python
import re
def artical_page(self, response):
    for each in response.doc('a[href^="http"]').items():
        if re.match("http://blog.csdn.net/mishifangxiangdefeng/article/details/\d*\d$", each.attr.href, re.U):
            self.crawl(each.attr.href, callback=self.detail_page)
```
使用[《spider/pyspider基础》](spider-pyspider-basic.md)中的调试方法进行单步调试，可以看到类似这样的画面

![](http://img.my.csdn.net/uploads/201601/22/1453445988_9084.png)

#### 二、根据文章的链接获取文章的信息

针对步骤一中的文章链接处理的回调函数是`detail_page`

```python
@config(priority=2)
def detail_page(self, response):
    return {
        "url": response.url,
        "title": response.doc('title').text(),
    }
```
        
这里只提取了页面中的链接地址和标题，我们需要更多的信息

选择其中一个页面，使用chrome浏览器打开这个页面

选择想要获取的内容，例如时间，点击右键，inspect

![](http://img.my.csdn.net/uploads/201601/22/1453446071_2269.png)

点击高亮的那一行，右键-> copy -> copy selector

![](http://img.my.csdn.net/uploads/201601/22/1453446207_6733.png)

被复制到剪贴板中的是这样的内容，这就是目标的CSS样式

```css
#article_details > div.article_manage.clearfix > div > span.link_postdate，
```
在`detail_page`中`"title": response.doc('title').text()`,下面加上这样一句，再次单步调试，调试结果如图

```python
"time": response.doc('#article_details > div.article_manage.clearfix > div > span.link_postdate').text(),
```

![](http://img.my.csdn.net/uploads/201601/22/1453446530_4195.png)

可见时间已经正确地取到了，接下来依次获取其它内容。

```python
@config(priority=2)
def detail_page(self, response):
    return {
        "url": response.url,
        "title": response.doc('title').text(),
        "time": response.doc('#article_details > div.article_manage.clearfix > div > span.link_postdate').text(),
        "reader": response.doc('#article_details > div.article_manage.clearfix > div > span.link_view').text(),
        "comments": response.doc('#article_details > div.article_manage.clearfix > div > span.link_comments').text(),
        "type": response.doc('#article_details > div.category.clearfix > div.category_r > label > span').text(),
        "contents1": response.doc('#article_content > p').text(),
        "contents2": response.doc('#article_content > div').text(),
    }
```
代码中关于文章的contents属性有两种格式，这是因为CSDN支持普通编辑模式与markdown编辑模式，这两种的CSS样式是不同的。

#### 三、翻页

使用同样的方法选取“下一页”按钮的样式，发现每一次都是不同的，所以我们换一种方法

获取样式、使用doc解析，其最终目的都是为了获取得按钮指向的地址，所以也不管什么样式了，直接构造每一个list页面的地址

观察发现list页面的地址格式如下`http://blog.csdn.net/mishifangxiangdefeng/article/list/n`，其中n是一个数字，表示第几页。

通过“尾页”按钮计算出总页数为19

```python
list_text = response.doc('#papelist > a:nth-child(9)').attr.href
list_count = int(filter(str.isdigit, list_text))
```
构造每一页的地址

```python
url = "http://blog.csdn.net/mishifangxiangdefeng/article/list/" + str(count)
```
调用爬取函数同时设置回调函数`self.crawl(url, callback=self.artical_page)`，这里的`artical_page`就是上一步中的`detail_page`

#### 四、源代码

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-01-19 13:25:59
# Project: test

from pyspider.libs.base_handler import *
import re

class Handler(BaseHandler):
    crawl_config = {
            "proxy":"local_proxy:8080",
    }

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl('http://blog.csdn.net/mishifangxiangdefeng', callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
#        self.artical_page(response)
        self.list_page(response)

    def artical_page(self, response):
        for each in response.doc('a[href^="http"]').items():
            if re.match("http://blog.csdn.net/mishifangxiangdefeng/article/details/\d*\d$", each.attr.href, re.U):
                self.crawl(each.attr.href, callback=self.detail_page)

    def list_page(self, response):
        list_text = response.doc('#papelist > a:nth-child(9)').attr.href
        list_count = int(filter(str.isdigit, list_text))
        for count in range(list_count+1):
            url = "http://blog.csdn.net/mishifangxiangdefeng/article/list/" + str(count)
            print url
            self.crawl(url, callback=self.artical_page)


    @config(priority=2)
    def detail_page(self, response):
        return {
            "url": response.url,
            "title": response.doc('title').text(),
            "time": response.doc('#article_details > div.article_manage.clearfix > div > span.link_postdate').text(),
            "reader": response.doc('#article_details > div.article_manage.clearfix > div > span.link_view').text(),
            "comments": response.doc('#article_details > div.article_manage.clearfix > div > span.link_comments').text(),
            "type": response.doc('#article_details > div.category.clearfix > div.category_r > label > span').text(),
            "contents1": response.doc('#article_content > p').text(),
            "contents2": response.doc('#article_content > div').text(),

        }
```
