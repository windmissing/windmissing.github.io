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

UE肯定不能随便向GNB发数据的，它的行为需要GNB的认可，GNB同意了（给UE发UL grant），UE才能根据UL　grant的要求发数据。
![](\images\2019\8.png)

multiplexing发生在收到UL grant之后，发送UL data之前。它要求MAC层从上层（RLC）的逻辑信道取数据，把多个逻辑信道的数据复用到一个TB中。

## 选择逻辑信道

> [5.4.3.1.2]Selection of logical channels  
> The MAC entity shall, when a new transmission is performed:  
1>	select the logical channels for each UL grant that satisfy all the following conditions:  
...

为了避免一开始就卷入比较复杂的细节中，就把conditions的具体内容省略了，详见[TODO]。

简单来说，根据上图可知，UE一定是在收到某个SR之后，才能根据这个SR提供的信道发送上行数据。SR里面包含了gNB对上行数据的逻辑信道的要求，包括SCS、Serving Cell、grant type、duration等。只有满足这些要求的逻辑信道的数据才能基于这次的Grant发送。

## 复用到TB

![](http://www.techplayon.com/wp-content/uploads/2017/09/NR-RLC-730x312.png)

这个图也是来自网上，忽略SDAP层和PDCP层。仅关注RLC层和MAC层。

通过逻辑信道收到的是RLC PDU，即加过RLC SDU + RLC header。RLCPDU即MAC SDU。MAC SDU + MAC header又构成了MAC PDU。关于PDU与SDU见[TODO]。


# UE demultiplexing in DL

##  从传输信道收数据
## 解TB
## 选择逻辑信道发出
