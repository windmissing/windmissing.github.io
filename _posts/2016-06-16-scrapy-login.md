---
layout: post 
title:  "scrapy - 模拟登陆"
categories: spider
tags: [python, spider, scrapy, login, 401]
---

#### 一、问题描述

在访问有些网页时会得到401错误，很有可能是因为访问这个网页需要提供用户名和密码。  
这就要求我们在访问页面的request中添加一些额外的信息。  
幸运的是，Scrapy已经做好的大部分工作。

<!-- more -->

#### 二、在request中附加信息  
1.删掉start_urls及其中的内容  

```python
#start_urls = [
#    'http://blog.csdn.net/mishifangxiangdefeng',
#    ]
```
2.加入这个函数

```python
return [
    FormRequest('https://passport.csdn.net/account/login?ref=toolbar',
                formdata={})
    ]
```
其中`https://passport.csdn.net/account/login?ref=toolbar`替换成start_urls中的目标网页的登陆页面  
formdata中填入附加信息

#### 三、附加信息怎么填
##### 附加信息是怎么
这几步可参考这里：[2.如何获取agent client](/spider/2016-06/scrapy-solve-401-by-agent-client.html#2如何获取agent-client)  
- 打开chrome
- 右键->inspect->network  
- 打开要登录的页面  
- 填入登陆信息，然后登陆  
- 打开登陆过程中产生的消息，依次查看
- 找到消息中带`form data`的消息（通常是第一条）  
![](/image/scrapy-login-form-data.jpg)
- 这里内容就是要填入form data的附加信息，包括用户名和密码，有时还有其它内容  

##### formdata的格式  
formdata是python中的dict类型，本例中的情况应该这样填  

```python
formdata = {'username' : 'myname', 'password' : 'mypass', 'remeberme' : '1'}
```
