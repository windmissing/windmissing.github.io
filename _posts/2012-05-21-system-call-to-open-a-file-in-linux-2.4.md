---
layout: post
title:  "Linux2.4打开一个文件的系统调用"
category: [操作系统]
tags: [linux2.6]
---

#### 0.sys_open()
（1）从当前进程的“打开文件表”中找到一个空闲的项get_unused_fs()  
（2）建立文件读写的上下文filp_open()：（见1）  
（3）将上下文安装到文件打开表中  

#### 1.filp_open()：建立文件读写的上下文
（1）获取指向文件名的dentry和vfsmount：open_namei()  
若只是打开，则通过path_init()和path_walk()搜索  
若有不存在就创建的要求，则（见3）  

#### 3.获取指向文件名的dentry和vfsmount，若不存在就创建
（1）找到path_name对应的节点的父dentry  
（2）找到目标文件的dentry  
（3）若不存在，则创建dentry：vfs_create()（见4）  
（4）判断dentry：  
若是一个安装点，则进入所安装的文件系统  
若是一个连接符号，则展开目标结点，go to 3-(1)  
（5）由dentry计算出inode  
（6）对inode各种检查  
（7）如果需要，对文件截尾  
A.切除length之后的内容  
B.修改inode  
C.把inode挂入脏队列  

#### 4.vfs_create()：为文件在创建一个dentry
（1）创建文件在存储设备上的索引节点和内存中的inode：ext2_new_inode()  
（2）把目标文件的文件名和索引节点号写入其所在的目录ext2_add_entry()  
（3）把目标文件的dentry结构和inode结构联系在一起d_instantiate()  
