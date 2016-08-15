---
layout: post
title:  "C语言开源项目-tinyhttpd"
category: [opensource]
tags: []
---

> tinyhttpd 是一个不到 500 行的超轻量型 Http Server，用来学习非常不错，可以帮助我们真正理解服务器程序的本质。

<!-- more -->

#### main

```
                           |<--------------------^
                           V                     |
start ----> start_up_port ---> accept ---> create_thread ---> accept_request ---> end
```

start_up_port：开启指定（或随机）的端口，并将端口与httpd服务绑定。指定端口开始监听http请求。  
accept：指定端口监听到http请求  
create_thread:创建一个线程执行accept_request来处理请求

#### start_up_port --->accept

一套标准的socket->bind->listen->connect->accept流程

socket：生成一个socket文件描符    
bind：绑定了服务器要监听的ip/port  
listen：对这对ip/port进行监听  
connect：客户端请求连接  
accept：服务器调用accept()接受客户端连接请求，并分配新的ip/port与客户端通信，之前的ip/port继续监听  

#### accept_request

```
          start
            |
        get_line：读取请求的字符串
            |
        获取method：字符串中的第一个参数
       /    |     \
POST方法  GET方法  其它方法
   |        |          |
cgi = 1     |         end
    \       /
     获取url：字符串第二个参数
          |
method==GET && url中包含'?'
   /           \
  否           是
  |             |
  |          url从？截断
  |          query_string指令url？以后的部分
  |          cgi = 1
  \         /
格式化 url 到 path：path表示浏览器请求的服务文件路径，若path为文件夹，默认在path后加上index.html
       |
       判断cgi的值
      /          \
为0（无参的GET）  为1（POST或有参的GET）
      |                         |
serve_file：                 execute_cgi
输出服务器文件到浏览器       执行 cgi 脚本
      |                         |
     end                       end
```

#### serve_file

用于处理无参的GET方法的请求。  
处理方法是把文件的内容输出到浏览器。  
文件的地址就是解析出来的url  

```
  start
    |
把剩下的数据扔掉
    |
headers：构造消息头，并send
    |
cat：读取文件内容，并send
    |
   end
```

#### execute_cgi

用于处理POST方法或带参数的GET方法。   
由于需要执行CGI脚本，因此会新建一个进程。  

```
            start
           /     \
    GET方法       POST方法
       |             |
把剩下的数据扔掉  剩下的数据， 提取Content-Length，其余扔掉
        \            /
      建立管道cgi_output
            |
      建立管道cgi_input
            |
      新建一个进程
            |
      把 HTTP 200  状态码写到套接字
        /          \
    父进程       子进程
      |             |
    配置管理     配置管理
      |             |
      |          配置cgi运行环境
      |                |
把数据写到input--->从STDIN读数据
      |                   |
      |            执行CGI文件（文件路径为path）
      |                   |
从cgi_output读取<---执行结果输出到STDOUT
      |                   |
    send                 end
      |
     end
```
