---
layout: post
title:  "swift - function 与closure的同异"
category: [ios, 编程语言]
tags: [ios, swift]
---


|  | function | closure
---|---|---
参数之间以`,`相隔 | Y | Y
有内参与名外参名 | Y | Y
自动定义外参名 | Y | N
参数支持var, inout关键字 | Y | Y
参数支持可变个数 | Y | Y
设置参数默认值 | Y | N
capture from enclosing scope | Y | Y
泛型 | Y | N
trailing closure语法 | N | Y
就地定义和赋值 | N | Y
根据内容推导参数和返回值 | N | Y
速度参数，如$0 | N | Y
对于只条一句的情况，可以推导出return | N | Y
