---
layout: post
title:  "redis配置文件样例(一)"
category: opensource
tags: [redis, cofiguration, 翻译]
---

原文链接：https://raw.githubusercontent.com/antirez/redis/2.8/redis.conf

----------
注意，要想让redis使用这个配置文件，redis启动时必须把这个文件的路径作为第一个参数：
```
./redis-server /path/to/redis.conf
```
----------
注意，如果需要设置内存大小，可以设置的大小为1K到5G的范围，说明形式如下：
```
# 1k => 1000 bytes
# 1kb => 1024 bytes
# 1m => 1000000 bytes
# 1mb => 1024*1024 bytes
# 1g => 1000000000 bytes
# 1gb => 1024*1024*1024 bytes
```
配置文件大小写不敏感，因此1GB 1Gb 或1gB都是一样的

----------
文件包含
==
配置文件可以包含一个或多个头文件。在某些情况下这很有用，你可以对所有redis服务器使用一个标准模版，又在某些配置上针对每个服务器作一个订制化的设置。被包含的文件可以再包含其它文件，因此广泛使用。
注意，“include”选项不会被来自admin或Redis Sentinel的“CONFIG REWRITE”重写掉。如果多个文件对同选项作了设置。redis总是使用最后一次的设置，因此你最好把"include"放在文件的开始处，以避免在运行时被后面的文件重写。
如果相反，你希望使用"include"来覆盖这些配置选项，最好把它放在文章的结尾。
```
# include /path/to/local.conf
# include /path/to/other.conf
```
----------

常规选项
====
默认情况下，redis不作为守护进程来运行。如果需要作为守护进程来运行，使用"yes"。
注意，如果作为守护进程运行，Redis会在路径/var/run/redis.pid上写一个进程文件
```
daemonize no
```
----------
当以守护进程运行时，redis会默认把进程文件写到/var/run/redis.pid。你可以在这里定义习惯的进程文件路径。
```
pidfile /var/run/redis.pid
```
----------
监听某个特定的端口并接受连接请求，默认端口号为6379。
如果端口号定义为0，redis将不监听TCP套接字。
```
port 6379
```
---------
TCP 监听工作储备
在每秒有多个请求的应用场景中，你需要一个大的工作储备，以避免出现较慢的客户端的连接问题。注意，linux内核会悄悄地把这个值缩小到
/proc/sys/net/core/somaxconn，因此请确认somaxconn和 tcp_max_syn_backlog的值都提升了，才能达到想到的目的。
```
tcp-backlog 511
```
----------
默认情况下，redis会监听来自服务器上所有可用网络接口的连接请求。也可以只听监听来自一个或几个接口的连接请求，使用"bind"配置指令，并跟上一个或多个IP地址。
例子：
```
# bind 192.168.1.100 10.0.0.1
# bind 127.0.0.1
```
----------
定义用于监听连接请求的UNIT套接字的路径。这一项没有默认值。如果没有定义路径，redis不会监听unix套接字。
```
# unixsocket /tmp/redis.sock
# unixsocketperm 700
```
----------
当某个客户端空闲了N秒时，就关闭和它的连接。（0表示这个功能不启用）。
```
timeout 0
```
----------
TCP保活
如果保活时间非0，redis服务器会使用SO_KEEPALIVE向没有通信的客户端发送TCP ACK。它的作用体现在以下两点：
1）发现挂掉的客户端。
2）从处于困境的网络设备的角度，让它们感觉到连接。

> 原文： Take the connection alive from the point of view of network equipment in the middle.

在linux上，这个值（以秒为单位）说明发送ACK的周期。
注意：关闭连接需要双倍的时间
在其它内核中，这个周期取决于内核的配置。
这个选项的推荐值为60秒。
```
tcp-keepalive 0
```
----------
说明服务器的信息显示级别，可以是以下中之一：
debug：有很多信息，对开发或测试有用。
verbose：有许多不太有用的信息，但比debug级别的信息要少
notice：适量的信息，你可以在产品中需要的信息
warning：只有非常重要、关键的信息
```
loglevel notice
```
----------
说明日志文件的名字。空字符串则redis把日志打印到标准输出。注意：如果你把日志设置为标准输出却作为守护进程启动，日志会被发送到/dev/null
```
logfile ""
```
----------
想要记录系统日志，只需只syslog-enable设置为yes，并有选择地更新其它系统日志相关的参数来满足你的需求。
```
# syslog-enabled no
```
----------
说明系统日志的标识
```
# syslog-ident redis
```
----------
说明系统日志的设备。
必须是USER或者LOCAL0到LOCAL7
```
# syslog-facility local0
```
----------
设置数据库的个数。默认的数据库是DB 0。你可以使用`SELECT <dbid>`来选择不同的数据库。dbid是0到databases-1之间的数字。
```
databases 16
```
----------
快照
==
把数据库存储到硬盘上：
```
save <秒数> <变化数>
```
如果过了给定秒数且针对当前数据库的写操作的次数达到了设置的变化数，这个数据库会被保存到硬盘上。
下面例子中的配置，当以下情况发生时会保存。
过了900秒（15分钟），至少一个键发生了变化
过了300秒（5分钟），到少10个键发生了变化
过了60秒，到少10000个键发生了变化
把所有save行都注释掉，就可以完全关闭保存功能。
也可以删掉所有前面配置的保存点，只需加一行save并使用空字符串作为参数，如下：```#   save ""```
```
save 900 1
save 300 10
save 60 10000
```
----------
默认情况下，当RDB快照启动（达到至少其中一个保存点），redis会停止写操作，最新的背景保存会失败。
用户必须能够意识到（虽然有点难）这一点，数据有可能没有被保存到硬盘上，否则有可能某些灾难发生了却没有人注意到。
如果背景保存进程再次启动，redis会自动地允许所有的写操作。
然而，如果你很好地监视你的redis服务器和持久化功能，你想到关掉这一特性，redis会继续像往常一样工作，即使你的硬盘出现了一些问题。
```
stop-writes-on-bgsave-error yes
```
----------
当清掉.rdb数据库时，是否压缩字符串对象。
默认情况下是yes，因此大多数情况下这样是好的。
> 原文： If you want to save some CPU in the saving child set it to 'no'

但是，如果你有可压缩的值或键，数据库很有可能会变得很大。
```
rdbcompression yes
```
----------
从RDB的版本5开始，文件结尾会有CRC64校验。
这使得能够更好地应对异常情况，但在保存和加载RDB文件时会损失一点性能（大概10%），所以你可以关掉它，得到更好的性能。
```
rdbchecksum yes
```
----------
用于清数据库的文件名
```
dbfilename dump.rdb
```
----------
工作路径
数据库会被写到这个路径下，定义文件名使用上面这个配置指令“dbfilename”。
仅追加文件（AOF）也会被创建到这个路径。
注意：你在这里定义的必须是路径，不是文件名
```
dir ./
```
