---
layout: post 
title:  "基于scrapy的爬虫小练习 - 获取CSDN某个用户的所有文章"
categories: spider
tags: [python, spider, scrapy]
---

#### 一、主要流程
根据[《基于pyspider的爬虫小练习 - 获取CSDN某个用户的所有文章》](/spider/2016-01/pyspider-fetch-csdn-articles.html)的经验，可知要获取CSDN某用户的所有文章，主要有几下这几个工作

1.由起始链接得到list链接

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
    
#### 三、由起始链接得到list链接
    
(1)回调函数
对起始链接处理的回调函数是parse
def parse(self, response):
        pass
(2)提取“尾页”按钮的链接
与pyspider使用selector不同，scrapy使用的是xpath，但获取方法类似
点击“尾页” -> 右键 -> inspect -> copy -> xpath
得到的xpath是这样的：//*[@id="papelist"]/a[7]
因为要的是它的链接，所以
list_link = response.xpath('//*[@id="papelist"]/a[7]/@href').extract()
(3)提取list数
list_count = int(list_link[0].split("/")[-1])
(4)构造list链接
 print list_count
        for count in range(list_count+1):
            url = "http://blog.csdn.net/mishifangxiangdefeng/article/list/" + str(count)
(5)处理每个list，处理list的回调函数为self.article_page
yield scrapy.Request(url, callback=self.article_page)

3.构造文章链接
（1）回调函数为self.article_page
（2）提取页面里的所有链接
for url in response.xpath('//a/@href').extract():
（3）对链接进行过滤，只选择指向文章的链接
if re.match(".*/mishifangxiangdefeng/article/details/\d*$", url, re.U):
（4）由于这里url不带基址，直接爬取会报错，所以要先获取基址，拼接出一个完整的地址
 base_url = get_base_url(response)
url = urljoin_rfc(base_url, url)
yield scrapy.Request(url, callback=self.detail_page)

3.构造存储文章信息的item类
import scrapy

class csdn_article(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    reader = scrapy.Field()
    comments = scrapy.Field()
    atype = scrapy.Field()
    contents1 = scrapy.Field()

4.存储文章信息及内容

四、踩过的那些坑
1.
由于这里url不带基址，直接爬取会报错，所以要先获取基址，拼接出一个完整的地址
 base_url = get_base_url(response)
url = urljoin_rfc(base_url, url)
yield scrapy.Request(url, callback=self.detail_page)
2.中文编码
五、参考链接
http://scrapy-chs.readthedocs.org/zh_CN/latest/intro/tutorial.html
