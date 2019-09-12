---
layout: post
title:  "3GPP 5G MAC overview"
category: [5G]
tags: [MAC]
---

MAC即Medium Access Control，是3GPP制定的通信协议标准。

空口协议是UE与GNB之间进行交互的协议。MAC位于接入网空口协议第二层。

![](\images\2019\1.png)

*note1:图中有4处IP，其代表含义不同。位于UE和NG最上层的IP代表用户数据包。位置NG协议第二层的IP代码TCP/IP协议。*

*note2:gNB中左右两侧分别是两套协议。这两套协议同一行没有对应关系。*

<!-- more -->

# MAC层的服务

和其它协议模型一样，空口协议中的每一层都要向上提供服务。

![](\images\2019\2.png)

MAC层向RLC层提供服务：

> [38.321 4.3]
> - data transfer（数据传输）
> - radio resource allocation（空口资源分配）

MAC需要PHY提供服务：

> [38.321 4.3]
> - Data transfer service（数据传输服务）
> - Signalling of HARQ feedback（HARQ反馈信号）
> - Signalling of Scheduling Request（SR信号）
> - Measurement (e.g. Channel Quality Indication(CQI))（信道质量的测量）

# MAC层的功能

> [38.321 4.4]
> - mapping between logical channels and transport channels（[逻辑信道与传输信道的映射](http://windmissing.github.io/5g/2019-09/mapping-between-logical-channels-and-transport-channels.html)）
> - multiplexing of MAC SDUs from one or different logicals channels onto transport blocks(TB) to be delivered to the physical layer on transport channels（[将来自一个或不同逻辑信道的MAC SDU复用到传输块（TB）上，以便传输到传输信道上的物理层](http://windmissing.github.io/5g/2019-09/multiplexing-and-demultiplexing.html)）
> - demultiplexing of MAC SDUs to one or different logical channels from transport blocks (TB) delivered from the physical layer on transport channels（[将MAC SDU从传输信道上的物理层传送的传输块（TB）解复用到一个或不同的逻辑信道](http://windmissing.github.io/5g/2019-09/multiplexing-and-demultiplexing.html)）
> - scheduling information reporting（调度信息上报）
> - error correction through HARQ（通过HARQ自动纠错）
> - logical channel prioritisation（按照逻辑信道的优先级传送数据）

## SIR

scheduling information reporting

## ERR correction

error correction through HARQ

## 优先级

logical channel prioritisation
