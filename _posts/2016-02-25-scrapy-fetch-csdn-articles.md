---
layout: post
title:  "基于scrapy的爬虫小练习 - 获取CSDN某个用户的所有文章"
categories: spider
tags: [python, spider, scrapy]
---

#### 一、主要流程

根据[《基于pyspider的爬虫小练习 - 获取CSDN某个用户的所有文章》](/spider/2016-01/pyspider-fetch-csdn-articles.html)的经验可知，一个用户的所有文章不会都在主页中显示，而是在主页上分了许多页（list），每一页有21篇文章。那么要获取该用户的所有文章，主要有几下这几个工作：

1.由起始链接得到每一页(list)的链接

2.由list链接得到每个list的文章链接

3.从文章链接提取文章信息

4.将文章信息存储到文件

<!-- more -->

#### 二、准备工作

1.项目创建

参考[《基于scrapy的爬虫小练习 - 准备工作》](/linux/2016-02/scrapy-prepare.html)

2.项目设置，这些配置已经在第1步中已经默认生成，这里再检查一下

打开 项目根目录/csdn/spiders/read-csdn-article.py，阅读ReadCsdnArticleSpider函数

（1）项目名，运行的时候会用到

```
name = "read_csdn_article"
```
（2）爬取范围（可选）

```
 allowed_domains = ["blog.csdn.net"]
```
（3）起始链接，默认项目中是用()，但建议改成()，不然后面可能会有错误

```
start_urls = [
    'http://blog.csdn.net/mishifangxiangdefeng',
    ]
```
3.设置代理，把这段代码加入到文件中可以设置代理的地址、端口号、用户名和密码

```python
# Start your middleware class
class ProxyMiddleware(object):
  # overwrite process request
  def process_request(self, request, spider):
    # Set the location of the proxy
    request.meta['proxy'] = "http://local_proxy:8080"

    # Use the following lines if your proxy requires authentication
    proxy_user_pass = "USERNAME:PASSWORD"
    # setup basic authentication for the proxy
    encoded_user_pass = base64.encodestring(proxy_user_pass)
    request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
```

#### 三、由起始链接得到每一页（list）链接

##### 1.从起始链接得到的信息

在设置好项目的`start_urls`之后，运行项目，框架就会自动地爬取`start_urls`中的网页。所有爬取到的结果都会通过一个回调函数返回给开发人员。

这个回调函数就是`parse`。每一个`start_url`对应一次回调，结果存储在参数`response`中。

框架提供了一个空的`parse`函数，这个需要由开发人员根据自己的需求补充。

```python
def parse(self, response):
        pass
```

##### 2.从`response`中提取“尾页”按钮的超链接

`response`中存储了这个页面所有元素的信息，我们现在所需要的仅仅是其中“尾页”按钮的信息。可以通过CSS样式过滤出我们所要的。

与pyspider使用selector不同，scrapy使用的是xpath，但使用方法是类似的。

（1）用chrome打开目标页面，找到“尾页”按钮

（2）点击“尾页” -> 右键 -> inspect -> copy -> xpath

“尾页”按钮的xpath就存在于剪贴版中了：`//*[@id="papelist"]/a[7]`

有了它，就可以获取“尾页”按钮的所有信息了，但我们这里所需要的只是它的超链接

```python
list_link = response.xpath('//*[@id="papelist"]/a[7]/@href').extract()
```

##### 3.从超链接中提取总页数

```python
list_count = int(list_link[0].split("/")[-1])
print list_count
```

##### 4.构造每一页(list)的链接

```python
for count in range(list_count+1):
    url = "http://blog.csdn.net/mishifangxiangdefeng/article/list/" + str(count)
```

##### 5.为每个list设置回调函数

有了每一页的链接，接下来就是把这些链接当成是新的起点，进一步地爬取了信息了。

爬取的过程直接交给框架，爬到的结果仍然通过回调函数的方式交给开发者。但这一次，使用哪个回调函数来处理list页面就要由开发者自己设置了。
这里将list的回调函数设置为`self.article_page`

```python
yield scrapy.Request(url, callback=self.article_page)
```

#### 四、由list链接得到每个list是的所有文章的链接

直接进入`self.article_page`函数，list页面的所有信息都存储在参数`response`中，仍然用xpath提取文章链接，过程与“三”类似。

（1）提取页面里的所有链接

```python
for url in response.xpath('//a/@href').extract():
```

（2）对链接进行过滤，只选择指向文章的链接

```python
if re.match(".*/mishifangxiangdefeng/article/details/\d*$", url, re.U):
```

（3）由于这里url不带基址，不能直接用于进一步爬取，否则会报错。

那么先获取基址，与所求得的url一起，拼接出一个完整的地址。

```python
 base_url = get_base_url(response)
url = urljoin_rfc(base_url, url)
```

（4）设置进一步爬取链接的回调函数

```python
yield scrapy.Request(url, callback=self.detail_page)
```

#### 五、构造存储文章信息的item类

现在所有文章的信息都已经存在于self.detail_page的参数response中了，下一步就是解析成一个一个的字段，然后写到文件中。

先别急。解析出来的字段要先存到内存的结构体中，然后才能写文件，所以要先构造用于存储文章信息的结构体。

关于这个结构体，scrapy已经提供了空的模板，将字段填充进去即可。

另外还需要加一个把类转换为字符串的函数

```python
import scrapy

class csdn_article(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    reader = scrapy.Field()
    comments = scrapy.Field()
    contents1 = scrapy.Field()
    contents2 = scrapy.Field()

    def getString(self) :
       str = "url: " + self['url'] + "\n"
       str += "title: " + self['title'] + '\n'
       str += "time: " + self['time'] + '\n'
       str += 'reader: ' + self['reader'] + '\n'
       str += 'comments: ' + self['comments'] + '\n'
       str +=  self['contents1'] + '\n'
       str +=  '\n'.join(self['contents2']) + '\n'
       return str
```

#### 六.存储文章信息及内容

文章的所有信息已经存储在self.detail_page的参数response中了，现在要把感兴趣的信息使用xpath解析出来，填到item中，然后写文件。

（1）申请一个空的item对象

```python
item = csdn_article()
```

（2）使用xpath解析出感兴趣的信息

为什么contents有两个呢？因为csdn的文章可以使用markdown和网页这两种不同的编辑器。使用不编辑器写出来的文章CSS样式也不同。无法判断某一篇文章使用的是哪种，所以就把两种方式的内容都获取出来了。

```python
item = csdn_article()
item["url"] = response.url
item["title"] = response.xpath('//*[@id="article_details"]/div[1]/h1/span/a/text()').extract()[0].replace("\r\n", '').replace(' ','')
prefix = self.div_or_div2(response)
item["time"] = response.xpath(prefix + 'span[1]/text()').extract()[0]
item["reader"] = response.xpath(prefix + 'span[2]/text()').extract()[0]
item["comments"] = response.xpath(prefix + 'span[3]/text()').extract()[0]
item["contents1"] = self.get_contents1(response)
item["contents2"] = self.get_contents2(response)

yield item
```

（3）构造文件名，写文件

```python
 filename = item["title"] + ".csdn"
 with codecs.open(filename, 'w', 'utf-8') as f:
      f.write(item.getString())
```

#### 七、踩过的那些坑

##### 1.完整url
由于这里url不带基址，直接爬取会报错，所以要先获取基址，拼接出一个完整的地址

```python
 base_url = get_base_url(response)
url = urljoin_rfc(base_url, url)
yield scrapy.Request(url, callback=self.detail_page)
```

##### 2.中文编码
网页是的中文编辑一般是gb2312，而写文件所使用的编码一般是utf-8。

如果不加转换，直接将gb2312写入文件，文件将无法阅读，所有在写文件时一定要特别指明，是用utf-8编码写文件

```python
with codecs.open(filename, 'w', 'utf-8') as f:
```

##### 3.同一内容的xpath不同

有的页面有label，有的页面没有，导致time, reader, comments的xpath不同。
例如time，没有label时，time的xpath为`//*[@id="article_details"]/div[2]/div/span[1]`
有label时，label的xpath为`//*[@id="article_details"]/div[2]/div[1]/span`，而time的xpath为`//*[@id="article_details"]/div[2]/div[2]/span[1]`
因此先要判断label是否存在

```python
def is_label_exist(self, response):
    article_1 = response.xpath('//*[@id="article_details"]/div[2]/div/span[1]').extract()[0]
    if re.match(r'/d',article_1):
        return False
    else:
        return True
```
根据不同情况构造不同的path

```python
def div_or_div2(self, response):
    if self.is_label_exist(response):
        return '//*[@id="article_details"]/div[2]/div[2]/'
    else:
        return '//*[@id="article_details"]/div[2]/div/'
```

##### 4.获取contents2得到的list

不同于上前获取到的list，在前面获取到的list中实际只用第一项，所以会取下标[0]
contents2得到的list每一项都要用到

```python
def get_contents2(self, response):
    ret = response.xpath('//*[@id="article_content"]/div/p/text()').extract()
    if type(ret) == type((1,)):
        return ret[0]
    else:
        return ret
```
而在用的时候直接把list转换为字符串

```python
str +=  '\n'.join(self['contents2']) + '\n'
```

#### 八、附完整代码

```python
import scrapy
import re
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
import pickle
import codecs
import json

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

class DmozSpider(scrapy.Spider):
    name = "dmoz"
#    allowed_domains = ["csdn.net"]
    start_urls = [
        "http://blog.csdn.net/mishifangxiangdefeng",
    ]

    def parse(self, response):
        list_text = response.xpath('//*[@id="papelist"]/a[7]/@href').extract()
        print list_text
        list_count = int(list_text[0].split("/")[-1])
        print list_count
        for count in range(list_count+1):
            url = "http://blog.csdn.net/mishifangxiangdefeng/article/list/" + str(count)
            yield scrapy.Request(url, callback=self.article_page)


    def article_page(self, response):
        for url in response.xpath('//a/@href').extract():
            base_url = get_base_url(response)
            if re.match(".*/mishifangxiangdefeng/article/details/\d*$", url, re.U):
                url = urljoin_rfc(base_url, url)
                yield scrapy.Request(url, callback=self.detail_page)

    def div_or_div2(self, response):
      if self.is_label_exist(response):
        return '//*[@id="article_details"]/div[2]/div[2]/'
      else:
        return '//*[@id="article_details"]/div[2]/div/'

    def is_label_exist(self, response):
        article_1 = response.xpath('//*[@id="article_details"]/div[2]/div/span[1]').extract()[0]
        if re.match(r'/d',article_1):
            return False
        else:
            return True

    def get_contents1(self, response):
       for i in range(9):
           xpath = '//*[@id="article_content"]/p[%d]/text()' % (i)
           if response.xpath(xpath).extract():
               ret += response.xpath(xpath).extract()[0]
        return ret

    def get_contents2(self, response):
        ret = response.xpath('//*[@id="article_content"]/div/p/text()').extract()
        if type(ret) == type((1,)):
            return ret[0]
        else:
            return ret

    def detail_page(self, response):
        item = csdn_article()
        item["url"] = response.url
        item["title"] = response.xpath('//*[@id="article_details"]/div[1]/h1/span/a/text()').extract()[0].replace("\r\n", '').replace(' ','')
        prefix = self.div_or_div2(response)
        item["time"] = response.xpath(prefix + 'span[1]/text()').extract()[0]
        item["reader"] = response.xpath(prefix + 'span[2]/text()').extract()[0]
        item["comments"] = response.xpath(prefix + 'span[3]/text()').extract()[0]
        item["contents1"] = self.get_contents1(response)
        item["contents2"] = self.get_contents2(response)

        yield item
        filename = item["title"] + ".csdn"
        with codecs.open(filename, 'w', 'utf-8') as f:
             f.write(item.getString())

import scrapy

class csdn_article(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    reader = scrapy.Field()
    comments = scrapy.Field()
    atype = scrapy.Field()
    contents1 = scrapy.Field()
    contents2 = scrapy.Field()

    def getString(self) :
        str = "url: " + self['url'] + "\n"
        str += "title: " + self['title'] + '\n'
        str += "time: " + self['time'] + '\n'
        str += 'reader: ' + self['reader'] + '\n'
        str += 'comments: ' + self['comments'] + '\n'
        str +=  self['contents1'] + '\n'
        str +=  '\n'.join(self['contents2']) + '\n'
        return str
```

#### 九、参考链接

http://scrapy-chs.readthedocs.org/zh_CN/latest/intro/tutorial.html
