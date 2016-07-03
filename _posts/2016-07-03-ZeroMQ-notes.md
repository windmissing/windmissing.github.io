---
layout: post
title:  "ZeroMQ笔记"
category: [opensource]
tags: [opensource, ZeroMQ]
---
 
 zeroMQ是一个用于简化多线程问题、多核问题的开源项目
 
#### 问题背景  
在如何充分利用多核提高程序并行化方面有一些经典的问题：  
  - 同步问题  
  - 加锁过度  
  - 原子操作  
  - 多级流水线乱序执行  
  - 优先级反转  
  - 锁竞争  
而在解决这些问题上，传统方法有一些不足：  
 - 维护困难  
 - 不容易扩展  
 - 多核心利用率低  
 - 无锁算法对使用场景有要求  
因此需要一些新的方法来解决这些多核问题，而ZeroMQ提供了他们的解决方案。  

<!-- more -->

#### ZeroMQ的解决方案

ZeroMQ解决方案的核心思想就是用消息代替锁   
 - 线程间产共享数据，而是使用消息传递数据  
   - 支持各种大小的消息  
   - 大消息使用零拷贝  
 - 应用是一个个消息驱动的任务  
   - 进程内线程间通信：inproc  
   - 主机内进程间通信：IPC  
   - 网络内进程间通信：TCP  
   - 多播组内通信：PGM  
 - 无等待  
 - 易扩展  
 - 一个socket可以与多个socket相连  
 - 收发消息队列  
 - TCP自动重连  
 - HWM flow control  

#### ZeroMQ的主要模块及关系

![](http://loongson.blog.chinaunix.net/attachment/201303/31/22312037_1364724942uQqB.png)

 - main thread向用户层提供API  
 - listener创建与管理一个或多个session/engine  
 - main thread与session之间使用管道传递消息  
 - engine与真实的网络通信  
 - session与engine共同管理连接  

#### ZeroMQ提供的性能优化

减少内存分配：对于大的消息，仅传递指针     
批处理过程：多条消息压缩成一条消息发送   
Lock Free算法  
并发模型：线程之间通过异步消息通信   

---
后面的没听懂了

#### 关于socket

#### 关于pattern
