---
layout: post
title:  "Linux2.4文件系统中vfsmount、安装点的dentry、设备的dentry之间的关系"
category: [操作系统]
tags: [linux2.6]
---

#### 1.vfsmount、安装点的dentry、设备的dentry之间的关系
![](http://my.csdn.net/uploads/201205/14/1337003692_2514.gif)  
（1）一个安装点可以安装多个设备  
（2）一个设备可以安装到多个安装点上  

#### 2.vfsmount与vfsmount之间的关系
![](http://my.csdn.net/uploads/201205/14/1337003764_9311.gif)

#### 3.vfsmount与安装点的dentry之间的关系
图太难画，仅写出关系，图见笔记本  
（1）vfsmount->mnt_mountpoint指向安装点的dentry  
（2）安装点的dentry->d_vfsmount指向同一安装点的多个安装结构的队列头  
（3）vfsmount->mnt_clash指向(2)中的队列头  

#### 4.vfsmount与设备的dentry的关系
（1）vfsmount->root指向所安装设备的根目录的dentry  
（2）vfsmount->mnt_sb指向所安装设备的超级块的super_block  
（3）`super_block->s_mounts`指向安装同一设备的vfsmount的队列头  

#### 5.安装点dentry与设备dentry的关系
![](http://my.csdn.net/uploads/201205/14/1337004305_1232.gif)  
（1）它们之间没有直接关系，通过vfsmount连接  
（2）vfsmount->mnt_mountpoint指向安装点的dentry  
（3）vfsmount->mount_root指向所安装设备的dentry  
