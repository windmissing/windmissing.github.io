---
layout: post
title: "本地搭建ELK系统"
date:   2016-01-09 20:38:30 +0800
category: ELK
tags: [linux, ELK]
---

ELK系统主要由三部分组成，分别是elasticsearch、logstash、kibana。

ELK系统收到推送过来的日志后，首先由logstash解析日志中的字段，分解成一个一个的关键字。elasticsearch将关键字与日志信息关联起来，以一种特定的格式化方式存储数据到硬盘。kibana提供与用户的交互界面，根据用户需求，从elasticsearch中读取信息并在网页上显示。

本文以Redhat为例搭建一套非常简单的ELK系统步：

 - logstash从本地日志文件读取信息

 - elasticsearch存储信息

 - 在中通过kibana显示完整信息

 - 所有工作都在本地完成，即所有服务器和客户端地址都是127.0.0.1

<!-- more -->

#### 一、安装工具
##### 1.安装elasticsearch

```
wget https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.1.tar.gz
tar -xvzf elasticsearch-1.7.1.tar.gz
cp -a elasticsearch-1.7.1 /usr/local
cd /usr/local
ln –s elasticsearch-1.7.1 elasticsearch
```
##### 2.安装logstash

```
wget https://download.elastic.co/logstash/logstash/logstash-1.5.4.tar.gz
tar –xvzf logstash-1.5.4.tar.gz
cp –a logstash-1.5.4 /usr/local
cd /usr/local
ln –s logstash-1.5.4 logstash
```
##### 3.安装kibana

```
wget https://download.elastic.co/kibana/kibana/kibana-4.1.2-linux-x64.tar.gz
tar –xvzf kibana-4.1.2-linux-x64.tar.gz
cp –a kibana-4.1.2-linux-x64 /usr/local
cd /usr/local
ln –s kibana-4.1.2-linux-x64 kibana
```
#### 二、配置logstash

```
cd /usr/local/logstash
mkdir etc
touch central.conf
```
central.conf是logstash的配置文件，文件名随意配置件，文件内容如下：

```
input{
    file {
          path => "/tmp/*.log"
          start_position => beginning
     }
}

output {
    stdout {}
    elasticsearch {
          cluster => "elasticsearch"
          codec => "json"
          protocol => "http"
    }
}
```
启动logstash程序：

```
/usr/local/logstash/bin/logstash  agent --verbose --config /usr/local/logstash/etc/central.conf
```
配置文件将从/tmp/*.log中读到的日志，同时传给elasticsearch和标准输出。我现在现在还没有配置elasticsearch，可以从标准输出窗口中观察。如果有将日志内容输出，可知logstash搭建成功察。

#### 三、配置elasticsearch

由于elasticsearch和logstash是安装在一台机器上，elasticsearch默认配置即可。

```
/usr/local/elasticsearch/bin/elasticsearch -d #以deamon方式启动elasticsearch
```
打开127.0.01:9200看到这样的内容可知elasticsearch搭建成功

```
{
  "status" : 200,
  "name" : "Blaquesmith",
  "cluster_name" : "elasticsearch",
  "version" : {
    "number" : "1.7.1",
    "build_hash" : "b88f43fc40b0bcd7f173a1f9ee2e97816de80b19",
    "build_timestamp" : "2015-07-29T09:54:16Z",
    "build_snapshot" : false,
    "lucene_version" : "4.10.4"
  },
  "tagline" : "You Know, for Search"
}
```
 
#### 四、配置kibana

kibana也不需要配置，直接启动

```
/usr/local/kibana/bin/kibana
```
打开127.0.01:5601即可看到Kibana的页面，选择默认配置，进入，/tmp/*.log中的信息在kibana中显示，可知kibana搭建成功。


#### 五、遇到的问题
1.打开127.0.0.1：9200或127.0.0.1:5601时，提示网页无法打开，但kibana与elasticsearch服务器确实已经启动。

解决方法：代理关掉

2./tmp/*.log是存在的，但是kibana上提示没有数据，logstash的stdout也看不到数据

解决方法：logstash只读取最近一段时间的日志，把日志文件时间更新一下就可以解决

#### 六、参考文章
http://my.oschina.net/lenglingx/blog/504883?fromerr=a2z8OWmY
