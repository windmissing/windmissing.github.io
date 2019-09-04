---
layout: post
title:  "MAC层逻辑信道与传输信道的映射"
category: [5G]
tags: [MAC]
---

[3GPP 5G MAC overview](http://windmissing.github.io/5g/2019-08/3gpp-5g-mac-overview.html)中提到，MAC层位于接入网空口协议第二层，它的其中一个功能就是

>[38.321 4.3]mapping between logical channels and transport channels

即逻辑信道与传输信道的映射。

![](\images\2019\3.png)

这简单的一句话涉及到许多问题：

什么是逻辑信道？有哪些逻辑信道？

什么是传输信道？有哪些传输信道？

逻辑信道与传输信道之间是怎样映射的？

为什么需要逻辑信道向传输信道的映射？

<!-- more -->

# 什么是逻辑信道？有哪些逻辑信道？

[3GPP 5G MAC overview](http://windmissing.github.io/5g/2019-08/3gpp-5g-mac-overview.html)中提到，MAC层需要为RLC层提供服务。MAC层为RLC层提供的其中一个服务就是Data transfer service（数据传输服务）。

MAC层为RLC层提供的数据传输服务是基于逻辑信道的。

![](\images\2019\4.png)

> [38.321 4.5.3]
> To accommodate different kinds of data transfer services, multiple types of logical channels are defined i.e. each supporting transfer of a particular type of information.
> Each logical channel type is defined by what type of information is transferred.

为了适应不同种类的数据传输服务，定义了多种类型的逻辑信道，即每种逻辑信道都支持特定类型信息的传输。

每种逻辑信道类型由传输的信息类型定义。

# 什么是传输信道？有哪些传输信道？

[3GPP 5G MAC overview](http://windmissing.github.io/5g/2019-08/3gpp-5g-mac-overview.html)中提到，PHY层需要为MAC层提供服务。其中一个服务就是Data transfer service（数据传输服务）。

MAC层为RLC层提供的数据传输服务是基于传输信道的。

![](\images\2019\5.png)

# 逻辑信道与传输信道之间是怎样映射的？

盗用网上的一张图来说明它们之间的映射关系：

![](http://www.sharetechnote.com/html/5G/image/NR_ChannelMap_MAC_01.png)

图左边列了三张表格，这三张表都是3GPP协议上的原图。此处忽略表1.

表2和表3分别是上/下行方向上逻辑信道与传输信道的映射关系。表格上画'X'代表这个逻辑信道可以映射到这个传输信道上。

这两张表有些抽象，作者又在右边很直接地画出了它们之间的映射关系。红色代表下行，蓝色代表上行。

根据图上所示，可以有以下总结：

- 逻辑信道PCCH和BCCH都有专门的传输信道与之对应。

- 逻辑信道CCCH、DCCH、DTCH区分上行和下行。其上、下行分别对应传输信道的DL-SCH、UL-SCH。

- BCCH也可以使用DL-SCH

# 为什么需要逻辑信道向传输信道的映射？
