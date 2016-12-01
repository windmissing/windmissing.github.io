---
layout: post
title:  "windows mysql安装及遇到的问题"
category: [back-end]
tags: [mysql]
---

#### 安装

##### 下载

##### 安装

把下载文件解压，放到特定的位置，例如C:/Program Files/MySQL/   
设置环境变量，path后加;C:/Program Files/MySQL/MySQL 5.6/bin  
重启  
把根目录下的my-***.ini改名为my.ini，编辑文件。  

```
basedir = C:/Program Files/MySQL/MySQL 5.6/
datadir = C:/Program Files/MySQL/MySQL 5.6/data/
```

##### 安装和启动服务

以管理员身份打开cmd   

```
C:/WINDOWS/SYSTEM32/cmd.exe
```

```
mysqld -install  ::安装服务
::mysqld -remove  ::卸载服务
net start mysql  ::启动服务
::net stop mysql  ::停止服务
```

##### 使用SQL

```
mysql -u root
mysql> update mysql.user set password=PASSWORD('mypassword') where user='root'
mysql> flush privileges
```

#### 遇到问题

1.SQL文件夹要有读权限  
2.要用admin权限打开cmd  
3..ini的名字要改  
4.如果没有data，不要自己创建，从别的版本里拷过来  
5.字符集不匹配，使用下面的命令更改字符集

```
show variables like %character_set%
alter database xxxxx character set utf8;
```

#### 参考链接

http://www.cnblogs.com/live41/p/3971518.html  
http://stackoverflow.com/questions/34448628/after-install-mysql-doesn-start-windows10-source-install
