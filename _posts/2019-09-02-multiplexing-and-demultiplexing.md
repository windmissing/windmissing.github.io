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

![](https://www.tech-invite.com/3m38/img/tinv-38-321-NR-MAC-arch.gif)

<!-- more -->

# 上行与下行

空口协议是gNB与UE之间交互的协议。数据的交互是双向的，既可以从gNB流向UE，也可以从UE流向gNB。

3GPP规定核心网->gNB->UE的数据流向为下行。

![下行](\images\2019\6.png)

上图为下行方向，GNB把数据一层一层封装好发给UE，UE收到数据后一层一层地解析，最后还原出原始数据。

具体对应到MAC层，位于GNB侧的MAC层需要把MAC SDU multiplexing到TB。位于UE侧的MAC层则需要把把MAC SDU从TB demultiplexing出来。

3GPP规定UE->gNB->核心网的数据流向称为上行。

![上行](\images\2019\7.png)

上图为上行方向，MAC层要做的事情正好相反。GNB侧的MAC层的工作是demultiplexing，而UE侧的MAC层的工作是multiplexing.

38.321里只规则了UE侧如果multiplexing和demultiplexing。而没有规定GNB侧该如何工作。因此后面都是从UE的角度来说明multiplexing和demultiplexing的。

# UE multiplexing in UL

从上文可知，只有在上行方向，即UE要向gNB发数据时，MAC层才需要做multiplexing的工作。

![](http://www.techplayon.com/wp-content/uploads/2017/09/NR-RLC-730x312.png)

这个图也是来自网上，忽略SDAP层和PDCP层。仅关注RLC层和MAC层。

通过逻辑信道收到的是RLC PDU，即RLC SDU + RLC header。

整个RLC PDU作为一个MAC SDU。

MAC SDU + MAC sub-header又构成了MAC sub-PDU。

关于PDU与SDU见[TODO]。

由MAC SDU构成的MAC sub-PDU只是一种MAC sub-PDU。还有MAC CE（TODO）、padding也可以与MAC Sub-header一起构成MAC sub-PDU. 以上的这些MAC sub-PDU按照一定的规则放在一起就构成了MAC PDU。详见MAC PDU(TODO).

最终由PHY层的TB来承载这个MAC PDU。

# UE demultiplexing in DL

与UE multiplexing in UL相反，只有在下行方向，即UE从gNB收数据时，MAC层才需要做demultiplexing的工作。

##  从传输信道收数据

PHY层使用TB来承载MAC层的数据。因此PHY层收到TB后，MAC要解析这个TB。

>[338.321 6.1.2]  
> A MAC PDU consists of one or more MAC subPDUs. Each MAC subPDU consists of one of the following:
-	A MAC subheader only (including padding);
-	A MAC subheader and a MAC SDU;
-	A MAC subheader and a MAC CE;
-	A MAC subheader and padding.

MAC层对不同类型的MAC sub-PDU做不同的处理。

`A MAC subheader only`和`A MAC subheader and padding`将会被抛弃。

`A MAC subheader and a MAC CE`包含了MAC层的控制信息。MAC层的操作与MACCE的内容有关。见（TODO）

`A MAC subheader and a MAC SDU`中的MAC SDU被提取出来交给上层RLC。

## demultiplexing

MAC层根据MAC sub-PDU的MAC subheader来区分MAC sub-PDU的类型。

MAC subheader的格式本身也有多种。不管哪种MAC subheader，其bit2 - bit7都是固定的LCID字段。

![](http://windmissing.github.io/images/2019/13.png)

如果这个字段的值为[1, 32]，则说明它是MAC SDU的subheader(见38.321 表6.2.1-2)，且LCID是RLC PDU的logcical channel ID. MAC层根据这个字段把MAC PDU效果正确的logical channel。
