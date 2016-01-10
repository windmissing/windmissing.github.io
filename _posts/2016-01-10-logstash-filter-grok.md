---
layout: post
title: "logstash grok解析"
category: ELK
tags: [linux, ELK, grok]
---

在<a href="/elk/2016-01/set-up-ELK-locally.html">《本地搭建ELK系统》</a>中，在本地搭建了一个非常简单的ELK系统。其中logstash从本地日志文件中读取信息并交给elasticsearch。

然而直接把原始未加工的日志交给elasticsearch没有什么意义。

logstash还有一个重要的工作就是解析日志。把解析出来的关键字与日志本身共同交给elasticsearch，elasticsearch才能很好地建立日志索引。

logstash支持多种解析器，grok是其中一种。

<!-- more -->

使用grok filter需要在logstash的配置文件中加上这样的内容：

```
filter {
    grok {
        match => { "message" => "grok_pattern" }
    }
}
```
这段代码中除了`grok_pattern`以外都是logstash的关键字。`grok_pattern`部分需要使用者填充自己的解析方式。

`grok_pattern`由零个或多个`%{SYNTAX:SEMANTIC}`组成，其中SYNTAX是表达式的名字，是由grok提供的，例如数字表达式的名字是NUMBER，IP地址表达式的名字是IP。SEMANTIC表示解析出来的这个字符的名字，由自己定义，例如IP字段的名字可以是client。

对于下面这条日志：
 > 55.3.244.1 GET /index.html 15824 0.043

可以这样解析：

```
filter {
    grok {
        match=>{ "message"=>"%{IP:client} %{WORD:method} %{URIPATHPARAM:request} %{NUMBER:bytes} %{NUMBER:duration}" }
    }
}
```
将会得到这样的结果

	* client: 55.3.244.1
	* method: GET
	* request: /index.html
	* bytes: 15824
	* duration: 0.043

grok提供了哪些SYNTAX？可以查看文件grok-patterns，它默认放在路径/usr/local/logstash/vendor/bundle/jruby/1.9/gems/logstash-patterns-core-0.3.0/patterns下。

假设现在要匹配一个正则表达式为regexp的字符串，而grok预定义的SYNTAX都不满足，也可以自己定义一个SYNTAX

自定义SYNTAX 方式有两种：

（1）匿名SYNTAX

将`%{SYNTAX:SEMANTIC}` 写为`(?<SEMANTIC>regexp)`

（2）命名SYNTAX

 - 在dir下创建一个文件，文件名随意

 - 将想要增加的SYNTAX写入： `SYNTAX_NAME regexp`

 - 使用方法和使用默认SYNTAX相同
