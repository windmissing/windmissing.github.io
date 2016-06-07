---
layout: post
title:  "【转载】「Chris Richardson 微服务系列」服务发现的可行方案以及实践案例"
category: cloud
tags: [cloud, micro-service, 微服务, 服务发现]
---

[原文链接](http://blog.daocloud.io/microservices-4/)，支持原创

> 编者的话｜本文来自 Nginx 官方博客，是微服务系列的第四篇文章。第一篇介绍了微服务架构的模式，讨论了使用微服务架构的优缺点；第二篇和第三篇描述了微服务架构内部的通讯机制。这篇文章中，我们将会探讨服务发现。

**作者介绍**：Chris Richardson，是世界著名的软件大师，经典技术著作《POJOS IN ACTION》一书的作者，也是 cloudfoundry.com 最初的创始人，Chris Richardson 与 Martin Fowler、Sam Newman、Adrian Cockcroft 等并称为世界十大软件架构师。

![0516_richardson_服務](http://blog.daocloud.io/wp-content/uploads/2016/05/0516_richardson_%E6%9C%8D%E5%8B%99.jpg)

<!-- more -->

#### Chris Richardson 微服务系列全 7 篇：

1. [微服务架构的优势与不足](http://blog.daocloud.io/microservices-1/)

2. [使用 API 网关构建微服务](http://blog.daocloud.io/microservices-2/)

3. [微服务架构中的进程间通信](http://blog.daocloud.io/microservices-3/)

4. [服务发现的可行方案以及实践案例](http://blog.daocloud.io/microservices-4/)

5. 微服务的事件驱动数据管理

6. 选择微服务部署策略

7. 将单体应用改造为微服务

**Chris Richardson 所著所有文章已独家授权 DaoCloud 翻译并刊载。**

### 本期内容：  
#### 为什么要使用服务发现?

假设我们写的代码会调用 REST API 或者 Thrift API 的服务。为了完成一次请求，代码需要知道服务实例的网络位置（IP 地址和端口）。运行在物理硬件上的传统应用中，服务实例的网络位置是相对固定的；代码能从一个偶尔更新的配置文件中读取网络位置。

对于基于云端的、现代化的微服务应用而言，这却是一大难题，正如下图所示。

![Richardson-microservices-part4-1_difficult-service-discovery](http://blog.daocloud.io/wp-content/uploads/2016/05/Richardson-microservices-part4-1_difficult-service-discovery-1004x1024.png)

服务实例的网络位置都是动态分配的。由于扩展、失败和升级，服务实例会经常动态改变，因此，客户端代码需要使用更加复杂的服务发现机制。

服务发现有两大模式：客户端发现模式和服务端发现模式。我们先来了解客客户端发现模式。

#### 客户端发现模式
使用客户端发现模式时，客户端决定相应服务实例的网络位置，并且对请求实现负载均衡。客户端查询服务注册表，后者是一个可用服务实例的数据库；然后使用负载均衡算法从中选择一个实力，并发出请求。

客户端从服务注册服务中查询，其中是所有可用服务实例的库。客户端使用负载均衡算法从多个服务实例中选择出一个，然后发出请求。

下图显示了这种模式的架构：

![Richardson-microservices-part4-2_client-side-pattern](http://blog.daocloud.io/wp-content/uploads/2016/05/Richardson-microservices-part4-2_client-side-pattern-1024x967.png)

服务实例的网络位置在启动时被记录到服务注册表，等实例终止时被删除。服务实例的注册信息通常使用心跳机制来定期刷新。

Netflix OSS 是客户端发现模式的绝佳范例。Netflix Eureka 是一个服务注册表，为服务实例注册管理和查询可用实例提供了 REST API 接口。Netflix Ribbon 是 IPC 客户端，与 Eureka 一起实现对请求的负载均衡。我们会在后面深入讨论 Eureka。

客户端发现模式优缺点兼有。这一模式相对直接，除了服务注册外，其它部分无需变动。此外，由于客户端知晓可用的服务实例，能针对特定应用实现智能负载均衡，比如使用哈希一致性。这种模式的一大缺点就是客户端与服务注册绑定，要针对服务端用到的每个编程语言和框架，实现客户端的服务发现逻辑。

分析过客户端发现后，我们来了解服务端发现。

#### 服务端发现模式
另外一种服务发现的模式是服务端发现模式，下图展现了这种模式的架构：

![Richardson-microservices-part4-3_server-side-pattern](http://blog.daocloud.io/wp-content/uploads/2016/05/Richardson-microservices-part4-3_server-side-pattern-1024x631.png)

客户端通过负载均衡器向某个服务提出请求，负载均衡器查询服务注册表，并将请求转发到可用的服务实例。如同客户端发现，服务实例在服务注册表中注册或注销。

AWS Elastic Load Balancer（ELB）是服务端发现路由的例子，ELB 通常均衡来自互联网的外部流量，也可用来负载均衡 VPC（Virtual private cloud）的内部流量。客户端使用 DNS 通过 ELB 发出请求（HTTP 或 TCP），ELB 在已注册的 EC2 实例或 ECS 容器之间负载均衡。这里并没有单独的服务注册表，相反，EC2 实例和 ECS 容器注册在 ELB。

HTTP 服务器与类似 NGINX PLUS 和 NGINX 这样的负载均衡起也能用作服务端的发现均衡器。Graham Jenson 的 [Scalable Architecture DR CoN: Docker, Registrator, Consul, Consul Template and Nginx](https://www.airpair.com/scalable-architecture-with-docker-consul-and-nginx) 一文就描述如何使用 Consul Template 来动态配置 NGINX 反向代理。Consul Template 定期从 Consul Template 注册表中的配置数据中生成配置文件；文件发生更改即运行任意命令。在这篇文章中，Consul Template 生成 nginx.conf 文件，用于配置反向代理，然后运行命令，告诉 NGINX 重新加载配置文件。在更复杂的实现中，需要使用 HTTP API 或 DNS 来动态配置 NGINX Plus。

Kubernetes 和 Marathon 这样的部署环境会在每个集群上运行一个代理，将代理用作服务端发现的负载均衡器。客户端使用主机 IP 地址和分配的端口通过代理将请求路由出去，向服务发送请求。代理将请求透明地转发到集群中可用的服务实例。

服务端发现模式兼具优缺点。它最大的优点是客户端无需关注发现的细节，只需要简单地向负载均衡器发送请求，这减少了编程语言框架需要完成的发现逻辑。并且如上文所述，某些部署环境免费提供这一功能。这种模式也有缺点。除非负载均衡器由部署环境提供，否则会成为一个需要配置和管理的高可用系统组件。

#### 服务注册表
服务注册表是服务发现的核心部分，是包含服务实例的网络地址的数据库。服务注册表需要高可用而且随时更新。客户端能够缓存从服务注册表中获取的网络地址，然而，这些信息最终会过时，客户端也就无法发现服务实例。因此，服务注册表会包含若干服务端，使用复制协议保持一致性。

如前所述，Netflix Eureka 是服务注册表的上好案例，为注册和请求服务实例提供了 REST API。服务实例使用 POST 请求来注册网络地址，每三十秒使用 PUT 请求来刷新注册信息。注册信息也能通过 HTTP DELETE 请求或者实例超时来被移除。以此类推，客户端能够使用 HTTP GET 请求来检索已注册的服务实例。

Netflix 通过在每个 AWS EC2 域运行一个或者多个 Eureka 服务实现高可用性。每个 Eureka 服务器都运行在拥有弹性 IP 地址的 EC2 实例上。DNS TEXT 记录被用来保存 Eureka 集群配置，后者包括可用域和 Eureka 服务器的网络地址列表。Eureka 服务在启动时会查询 DNS 去获取 Eureka 集群配置，确定同伴位置，以及给自己分配一个未被使用的弹性 IP 地址。

Eureka 客户端，包括服务和服务客户端，查询 DNS 去发现 Eureka 服务的网络地址。客户端首选同一域内的 Eureka 服务。然而，如果没有可用服务，客户端会使用其它可用域中的 Eureka 服务。

其它的服务注册表包括：

 - etcd – 高可用、分布式、一致性的键值存储，用于共享配置和服务发现。Kubernetes 和 Cloud Foundry 是两个使用 etcd 的著名项目。
 - consul – 发现和配置的服务，提供 API 实现客户端注册和发现服务。Consul 通过健康检查来判断服务的可用性。
 - Apache ZooKeeper – 被分布式应用广泛使用的高性能协调服务。Apache ZooKeeper 最初是 Hadoop 的子项目，现在已成为顶级项目。
 
此外，如前所强调，像 Kubernetes、Marathon 和 AWS 并没有明确的服务注册，相反，服务注册已经内置在基础设施中。

了解了服务注册的概念后，现在了解服务实例如何在注册表中注册。

#### 服务注册的方式
如前所述，服务实例必须在注册表中注册和注销。注册和注销有两种不同的方法。方法一是服务实例自己注册，也叫自注册模式（self-registration pattern）；另一种是采用管理服务实例注册的其它系统组件，即第三方注册模式。

#### 自注册方式
当使用自注册模式时，服务实例负责在服务注册表中注册和注销。另外，如果需要的话，一个服务实例也要发送心跳来保证注册信息不会过时。下图描述了这种架构：

![Richardson-microservices-part4-4_self-registration-pattern](http://blog.daocloud.io/wp-content/uploads/2016/05/Richardson-microservices-part4-4_self-registration-pattern-1024x893.png)

Netflix OSS Eureka 客户端是非常好的案例，它负责处理服务实例的注册和注销。Spring Cloud 能够执行包括服务发现在内的各种模式，使得利用 Eureka 自动注册服务实例更简单，只需要给 Java 配置类注释 @EnableEurekaClient。

自注册模式优缺点兼备。它相对简单，无需其它系统组件。然而，它的主要缺点是把服务实例和服务注册表耦合，必须在每个编程语言和框架内实现注册代码。

另一个方案将服务与服务注册表解耦合，被称作第三方注册模式。

#### 第三方注册模式
使用第三方注册模式，服务实例则不需要向服务注册表注册；相反，被称为服务注册器的另一个系统模块会处理。服务注册器会通过查询部署环境或订阅事件的方式来跟踪运行实例的更改。一旦侦测到有新的可用服务实例，会向注册表注册此服务。服务管理器也负责注销终止的服务实例。下面是这种模式的架构图。

![Richardson-microservices-part4-5_third-party-pattern](http://blog.daocloud.io/wp-content/uploads/2016/05/Richardson-microservices-part4-5_third-party-pattern-1024x593.png)

Registrator 是一个开源的服务注册项目，它能够自动注册和注销被部署为 Docker 容器的服务实例。Registrator 支持包括 etcd 和 Consul 在内的多种服务注册表。

NetflixOSS Prana 是另一个服务注册器，主要面向非 JVM 语言开发的服务，是一款与服务实例一起运行的并行应用。Prana 使用 Netflix Eureka 来注册和注销服务实例。

服务注册器是部署环境的内置组件。由 Autoscaling Group 创建的 EC2 实例能够自动向 ELB 注册。Kubernetes 服务自动注册并能够被发现。

第三方注册模式也是优缺点兼具。在第三方注册模式中，服务与服务注册表解耦合，无需为每个编程语言和框架实现服务注册逻辑；相反，服务实例通过一个专有服务以中心化的方式进行管理。它的不足之处在于，除非该服务内置于部署环境，否则需要配置和管理一个高可用的系统组件。

#### 总结
在微服务应用中，服务实例的运行环境会动态变化，实例网络地址也是如此。因此，客户端为了访问服务必须使用服务发现机制。

服务注册表是服务发现的关键部分。服务注册表是可用服务实例的数据库，提供管理 API 和查询 API。服务实例使用管理 API 来实现注册和注销，系统组件使用查询 API 来发现可用的服务实例。

服务发现有两种主要模式：客户端发现和服务端发现。在使用客户端服务发现的系统中，客户端查询服务注册表，选择可用的服务实例，然后发出请求。在使用服务端发现的系统中，客户端通过路由转发请求，路由器查询服务注册表并转发请求到可用的实例。

服务实例的注册和注销也有两种方式。一种是服务实例自己注册到服务注册表中，即自注册模式；另一种则是由其它系统组件处理注册和注销，也就是第三方注册模式。

在一些部署环境中，需要使用 Netflix Eureka、etcd、Apache Zookeeper 等服务发现来设置自己的服务发现基础设施。而另一些部署环境则内置了服务发现。例如，Kubernetes 和 Marathon 处理服务实例的注册和注销，它们也在每个集群主机上运行代理，这个代理具有服务端发现路由的功能。

HTTP 反向代理和 NGINX 这样的负载均衡器能够用做服务器端的服务发现均衡器。服务注册表能够将路由信息推送到 NGINX，激活配置更新，譬如使用 Cosul Template。NGINX Plus 支持额外的动态配置机制，能够通过 DNS 从注册表中获取服务实例的信息，并为远程配置提供 API。

英文原文：https://www.nginx.com/blog/service-discovery-in-a-microservices-architecture/
