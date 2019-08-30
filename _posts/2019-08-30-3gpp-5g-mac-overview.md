---
layout: post
title:  "3GPP 5G MAC overview"
category: [5G]
tags: [MAC]
---

MAC即Medium Access Control，是3GPP制定的通信协议标准。

MAC位于接入网空口协议第二层。

![](\images\2019\1.png)
> note1:图中有4处IP，其代表含义不同。位于UE和NG最上层的IP代表用户数据包。位置NG协议第二层的IP代码TCP/IP协议。
>
> note2:gNB中左右两侧分别是两套协议。这两套协议同一行没有对应关系。

空口协议中，每一层向上提供服务。

![](\images\2019\2.png)

MAC层向RLC层提供服务：

- data transfer
- radio resource allocation

MAC需要PHY提供服务：

- Data transfer service
- Signalling of HARQ feedback
- Signalling of Scheduling Request
- Measurement (e.g. Channel Quality Indication(CQI))

<!-- more -->

# MAC层有什么功能

## 逻辑信道与物理信道的mapping

什么是逻辑信道，RLC使用
什么是物理信道，L1使用
为什么要映射
怎么映射

## 组装TB

从逻辑信道收数据
组装到TB
选择物理信道发出

## 拆分TB

从物理信道收到TB
根据逻辑信道分开
分别在逻辑信道发出去

## SIR

scheduling information reporting

## ERR correction

error correction through HARQ

## 优先级

logical channel prioritisation
