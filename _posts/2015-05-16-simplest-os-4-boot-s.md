---
layout: post
title:  "1.最简单的操作系统（四）boot.S"
category: 运行自己的操作系统
tags: [操作系统]
---

一、作用
1.当系统运行到这段代码时，界面上有所显示，以验证这段代码是否正常运行
2.使生成的可执行文件刚好512B大小，且最后2个字节是0xAA55

二、代码说明
代码使用AT&T语法的汇编
作者：WB. YANG

三、单句说明

```
.code16		#使用16位模式汇编
```
CPU在加电自举时，首选进入的是实模式。
在模式下，字长是16位的，因此使用16位模式汇编
详情参考“实模式”
```
.text
```
代码段从此处开始。
这里的.text不是.elf中的.text，而是用于生成.elf中的.test。
参考《运行自己的操作系统 - 0.01 （三）链接脚本》

```
	mov     %cs, %ax     #数据段寄存器和通用段寄存器  
	mov     %ax, %ds  
	mov     %ax, %es  
```
用代码段寄存器来初始化数据段寄存器和通过寄存器，下文其实只用到了通用寄存器。
一般情况下，代码段、数据段、栈段应该分开。不过在这个代码中，把数据都放到了代码段中，它们属于同一段，所以可以使用CS来初始化DS和ES。

```
6	call    DispStr  #调用字符串显示函数，call function to display string
...
8	Dispstr:
...
16	ret
```
这里的call比较简单，不涉及到栈。
相当于先jmp Dispstr，Dispstr执行完了之后又jmp到call的下一条指令

```
jmp    .               #while(1)，无限循环  
```
.表示当前地址。
跳转到当前地址就是无限循环

```
DispStr:
```
这句话不会翻译成一条指令，相当于一个路标，便于阅读和跳转

```
9     mov     $BootMessage, %ax  
10    mov     %ax, %bp        #ES:BP = address of string  
11    mov     $16, %cx        #CX = length of string  
12    mov     $0x1301, %ax    #AH = 13, AL = 01h  
13    mov     $0x00c, %bx     #page number = BH=0, word color = BL = 0Ch  
14    mov     $0, %dl  
15    int     $0x10            #进入中段10h is interrupt number 
```
L9-L15都是为L15做准备工作。
L15调用了BIOS的10号中断，10号中断的作用是显示，其调用方法参考“BIOS中断”

```
BootMessage:.ascii "Hello, OS world!"
```
BootMessage和Dispstr一样，只是一个标签，相当于给这个地址起个名字。
.ascii表示在这个地址上声明并初始化一个字符串

```
.org 510                        #fill 0 in first 510 BYTE  
.word 0xaa55                    #end with 0xaa55 
```
保存所生成的可执行文件大小刚好512字节，并且以0xAA55结尾

四、完整源代码

```
  1 .code16							#使用16位模式汇编
  2 .text							#代码段开始
  3         mov     %cs, %ax		#数据段寄存器和通用段寄存器
  4         mov     %ax, %ds
  5         mov     %ax, %es
  6         call    DispStr         #调用字符串显示函数，call function to display string
  7         jmp    .               #while(1)，无限循环
  8 DispStr:						#字符串显示函数
  9         mov     $BootMessage, %ax
 10         mov     %ax, %bp        #ES:BP = address of string
 11         mov     $16, %cx        #CX = length of string
 12         mov     $0x1301, %ax    #AH = 13, AL = 01h
 13         mov     $0x00c, %bx     #page number = BH=0, word color = BL = 0Ch
 14         mov     $0, %dl
 15         int     $0x10            #进入中段10h is interrupt number
 16         ret						#返回
 17 BootMessage:.ascii "Hello, OS world!"
 18 .org 510                        #fill 0 in first 510 BYTE
 19 .word 0xaa55                    #end with 0xaa55
```
