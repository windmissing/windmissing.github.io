---
layout: post
title:  "multiplexing和demultiplexing"
category: [5G]
tags: [MAC]
---

[3GPP 5G MAC overview](http://windmissing.github.io/5g/2019-08/3gpp-5g-mac-overview.html)中提到，MAC层的功能包括multiplexing和demultiplexing.

>[38.321 4.3]
multiplexing of MAC SDUs from one or different logicals channels onto transport blocks(TB) to be delivered to the physical layer on transport channels

将来自一个或不同逻辑信道的MAC SDU复用到传输块（TB）上，以便传输到传输信道上的物理层。

>[38.321 4.3]
demultiplexing of MAC SDUs to one or different logical channels from transport blocks (TB) delivered from the physical layer on transport channels（将MAC SDU从传输信道上的物理层传送的传输块（TB）解复用到一个或不同的逻辑信道）

将MAC SDU从传输信道上的物理层传送的传输块（TB）解复用到一个或不同的逻辑信道

<!-- more -->

# 上行与下行

空口协议是gNB与UE之间交互的协议。数据的交互是双向的，既可以从gNB流向UE，也可以从UE流向gNB。

3GPP规定核心网->gNB->UE的数据流向为下行。

![下行](\images\2019\6.png)

上图为下行方向，位于GNB侧的MAC层需要把MAC SDU multiplexing到TB。位于UE侧的MAC层则需要把把MAC SDU从TB multiplexing出来。

3GPP规定UE->gNB->核心网的数据流向称为上行。

![上行](\images\2019\7.png)

上图为上行方向，MAC层要做的事情正常相反。GNB侧的MAC层的工作是demultiplexing，而UE侧的MAC层的工作是multiplexing.

# multiplexing

##  从逻辑信道收数据
## 组装到TB
## 选择物理信道发出

# demultiplexing

##  从传输信道收数据
## 解TB
## 选择逻辑信道发出
