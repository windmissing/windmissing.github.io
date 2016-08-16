---
layout: post
title:  "scrapy源码学习 - 启动一个crawl命令"
category: [opensource]
tags: [source code, python, spider]
---

scrapy提供很多种子程序，其中crawl用于启动scrapy项目的一个爬虫。

```
scrapy crawl 爬虫名
```
今天的主题是，当用户输完这个命令以后，到启动爬虫之前，代码是怎么走的。  

<!-- more -->

#### cmdline.py

scrapy所有子程序的入口函数都在这里。因此，对crawl的处理也是从这个文件开始的。  
入口函数非常简单，主要行为都在execute()中。  

```
          引用
exectute ------> ScrapyCommand
                 --------------
                 + crawler_process
                 + run()
                     /\
                    ----
                     |继
                     |承
    -----------------------------------
    |                 |               |
    |                 |               |
crawl_command   ohter commands    other commands
```

0.一些检查和配置  
1.获取该工程支持的所有命令，得到一个`命令名(String)->命令对象(ScrapyCommand)`的字典cmds。  
2.解析命令行，得到命令的名字cmdname  
3.根据命令的名字得到相应的命令对象cmd  
4.为cmd创建一个crawler_process（**不明白为什么要写在这里面，这不应该是cmd里面的事情吗？**）  
5.让命令对象cmd run起来  

#### commands/__init__.py

ScrapyCommand只是一个基类。不同的命令对应不同的具体的类。基类提供一些公共的行为。run行为则由各个子类重载。  
**不明白为什么每个子类的命令都叫Command?**  
crawl命令对应的子在在crawl.py中

#### crawl.py

crawl.py中的Command重载了ScrapyCommand中的部分行为，其中最重要的是run。  
run()的执行也很短：  
1.参数检查  
2.self.crawler_process.crawl  
3.self.crawler.start

#### crawler.py

crawler_prcess是Command从ScrapyCommand继承过来的。是CrawlerProcess的对象。

```
                                                 CrawlerRunner
                                                 -------------
                                                 + crawl
                                                       /\
          引用                                        ----
exectute ------> ScrapyCommand                         |继
                 --------------                        |承
                 + crawler_process ------------> CrawlerPorcess
                 + run()                         --------------
                     /\                          +start
                    ----
                     |继
                     |承
    -----------------------------------
    |                 |               |
    |                 |               |
crawl_command   ohter commands    other commands
```
上文中调用了CrawlerProcess对象的两个函数，一个继承自父类CrawlerRunner，另一个由子类自己实现。  
其中CrawlerRunner.crawl()完成了主要的爬虫工作。  
而CrawlerPorcess.start()似乎是善后工作。  
这两个函数具体做了什么，请看下集。
