---
layout: post
title:  "1.最简单的操作系统（二）makefile"
category: 运行自己的操作系统
tags: []
---

#### 一、目的

1.把源代码（boot.S）经过编译链接等过程，变成一个可执行文件（boot.bin）  
2.生成一个镜像文件（boot.img），用于系统启动。系统启动可以从软件上启动，也可以从硬盘上启动，这里选择的是软件  
3.把可执行文件（boot.bin）放到镜像文件（boot.img）中正确的位置，确保系统启动后能运行这个可执行文件  

#### 二、单句分析

```
all:boot.img
```
每个makefile都必须有这样一句话“all:最终目标”，  
makefile中所有过程的最终目的就是生成这个最终目标。  
与生成最终目标无关的过程不会被执行  
最终目标是否生成说明makefile是否执行成功。  
详情可参考“makefile的用法”  

```
boot.o:boot.S
	$(CC) -c boot.S
```
生成目标文件。目标文件的格式与.elf类似。  
这是编译过程中的最后一步，一个主要的作用是将汇编中的符号提取和分类，用于链接过程使用。  
详情可参考“编译原理”  

```
boot.elf:boot.o
	$(LD) boot.o -o boot.elf -e c -T$(LDFILE)
```
链接。主要步骤为符号解析、重定位。作用是将符号与它的定义（地址）关联起来。  
为什么要使用自定义的ld文件，见[运行自己的操作系统 -0.01 （三）链接脚本](http://blog.csdn.net/mishifangxiangdefeng/article/details/45766503)  
详情可参考“链接”  

```
boot.bin:boot.elf
    @$(OBJCOPY) -R .pdr -R .comment -R .note -S -O binary boot.elf boot.bin
```
将.elf格式的可执行文件转换为.bin格式的可执行文件。
可参考[Linux命令学习手册-objcopy命令 ](http://blog.chinaunix.net/uid-9525959-id-2001841.html)  

```
boot.img:boot.bin
	#用 boot.bin 生成镜像文件第一个扇区
	@dd if=boot.bin of=boot.img bs=512 count=1   	
	# 在 bin 生成的镜像文件后补上空白，最后成为合适大小的软盘镜像
	@dd if=/dev/zero of=boot.img skip=1 seek=1 bs=512 count=2879
```
boot.bin的大小刚好为512个字节，即一个扇区。  
用于boot.bin填充boot.img的第一个扇区，后面则全部填为0  
dd命令可参考[Linux 下用 dd 命令生成一个指定大小的虚拟块设备文件](http://blog.csdn.net/mishifangxiangdefeng/article/details/45507847)  

#### 三、完整源码

```
  1 CC=g++
  2 Ld=ld
  3 LDFILE=wind_x86.ld
  4 OBJCOPY=objcopy
  5 
  6 all:boot.img
  7 
  8 #Step 1:g++ call as, boot.S -> boot.o
  9 boot.o:boot.S
 10     $(CC) -c boot.S
 11 
 12 #Step 2:ld call link script, boot.o -> boot.elf
 13 boot.elf:boot.o
 14     $(LD) boot.o -o boot.elf -e c -T$(LDFILE)
 15 
 16 #Step 3:objcopy remove the useless section(such as .pdr, .commemnt, .node) i    n boot.efl, 
 17 #		strip all signal information, the output is boot.bin
 18 boot.bin:boot.elf
 19     @$(OBJCOPY) -R .pdr -R .comment -R .note -S -O binary boot.elf boot.bin
 20 
 21 #Step 4:generate bootable software image
 22 boot.img:boot.bin
		 #用 boot.bin 生成镜像文件第一个扇区
 23 	@dd if=boot.bin of=boot.img bs=512 count=1   	
 24 	# 在 bin 生成的镜像文件后补上空白，最后成为合适大小的软盘镜像
 25 	@dd if=/dev/zero of=boot.img skip=1 seek=1 bs=512 count=2879
 26
 27 clean:
 28 	@rm -rf boot.o boot.elf boot.bin boot.img
```