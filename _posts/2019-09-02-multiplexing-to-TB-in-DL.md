---
layout: post
title:  "复用MAC SDU到TB"
category: [5G]
tags: [MAC]
---

[3GPP 5G MAC overview](http://windmissing.github.io/5g/2019-08/3gpp-5g-mac-overview.html)中提到，MAC层的第二个功能是

>[38.321 4.3] multiplexing of MAC SDUs from one or different logicals channels onto transport blocks(TB) to be delivered to the physical layer on transport channels

即将来自一个或不同逻辑信道的MAC SDU复用到传输块（TB）上，以便传输到传输信道上的物理层。

<!-- more -->

## 组装TB

从逻辑信道收数据
组装到TB
选择物理信道发出
