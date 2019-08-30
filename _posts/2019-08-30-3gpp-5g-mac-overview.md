---
layout: post
title:  "3GPP 5G MAC overview"
category: [5G]
tags: [MAC]
---

# 什么是MAC层

## MAC层与空口协议

MAC即Medium Access Control，是3GPP制定的通信协议标准。

位于接入网空口协议第二层。

![](\images\2019\1.png)

## MAC层与RLC和L1之间

对上 。。。

对下。。。

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
