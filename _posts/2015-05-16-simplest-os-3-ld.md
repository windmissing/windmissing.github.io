---
layout: post
title:  "1.最简单的操作系统（三）链接脚本"
category: 运行自己的操作系统
tags: [操作系统]
---


一、什么是链接脚本
[链接器脚本](http://blog.sina.com.cn/s/blog_62b1ea5d0100lxib.html)

二、wind_x86.ld的作用
将程序入口设置为内存的0x7C00处。

三、脚本中的地址是什么地址
![这里写图片描述](http://img.blog.csdn.net/20150516121157914)

四、为什么地址要选在0x7C00
内存的某些部分固定用来做固定的用途，随意选择一个地方开始容易引起冲突，于是人们约定程序入口都从0x7C00开始。
BISO把第一个扇区load起来之后会自动跳转到0x7C00处。

五、单句分析

```
. = 0x7C00
```
跳过前面的地址，从0x7C00处开始有内容

```
.text:
```
这里的.text段是指.elf中的段。
后面{}中的内容用于生成.elf文件中的.text段。
.elf中可以有各种段，其中.text是代码码的意思，详情可参考“ELF目标文件”

```
*(.text)
```
这里的.text段是指源代码中的段。
源代码中.text段中的内容都用于生成.elf中的.text段

六、完整源代码

```
1 SECTIONS  
2 {  
3     . = 0x7c00;  
4     .text :  
5     {  
6         *(.text) /*program will be loeaded to 0x7c00*/  
7     } = 0  
8 }
```
