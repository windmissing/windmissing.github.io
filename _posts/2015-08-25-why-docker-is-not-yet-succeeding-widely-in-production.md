---
layout: post
title:  "【译】为什么docker还不能广泛用于产品中"
category: opensource
tags: [docker]
---

源地址：http://sirupsen.com/production-docker/

Jul 2015

Docker’s momentum has been increasing by the week, and from that it’s clearly touching on real problems. However, for many production users today, the pros do not outweigh the cons. Docker has done fantastically well at making containers appeal to developers for development, testing and CI environments—however, it has yet to disrupt production. In light of DockerCon 2015’s “Docker in Production” theme I’d like to discuss publicly the challenges Docker has yet to overcome to see wide adoption for the production use case. None of the issues mentioned here are new; they all exist on GitHub in some form. Most I’ve already discussed in conference talks or with the Docker team. This post is explicitly not to point out what is no longer an issue: For instance the new registry overcomes many shortcomings of the old. Many areas that remain problematic are not mentioned here, but I believe that what follows are the most important issues to address in the short term to enable more organizations to take the leap to running containers in production. The list is heavily biased from my experience of running Docker at Shopify, where we’ve been running the core platform on containers for more than a year at scale. With a technology moving as fast as Docker, it’s impossible to keep everything current. Please reach out if you spot inaccuracies.

这段时间，docker的发展更好了，但是也明显碰到了一些棘手的问题。然而，对于今天的许多产品用户来说，支持者并不比反对者多。docker使得开发、测试、CI（持续集成）环境对开发者们不可见，在一点上，docker确实做得非常好。然而，它已经干扰了生产。基于docker大会2015年的主题“生产中的docker”，我想要公开地讨论一下docker广泛采用的生产用例将要面对的挑战。这些话题都不是新的，都以某种形式在github中出现过了。其中大多数，我已经在“会议讨论”上或者与docker团队讨论过了。这篇文章显然不是为了指出哪一个不再是话题：例如新的registry修复了以前的许多不足。许多地方仍然存在问题，但这里没有提及。但我相信，下面的内容非常重要，可以短期内让更多的组织带头将容器用于生产中。这个列表主要来自于我自身使用docker的经验。我把内核平台放到容器中运行了一年多。通过一项和Docker移动一样快的技术，可以保证所有东西都是实时的。如果发现我的表述不准确，请指出来。

#### Image building

Building container images for large applications is still a challenge. If we are to rely on container images for testing, CI, and emergency deploys, we need to have an image ready in less than a minute. Dockerfiles make this almost impossible for large applications. While easy to use, they sit at an abstraction layer too high to enable complex use-cases:

##### 创建镜像文件

为大型应用创建容器镜像文件仍然是一个挑战。如果我们打算依靠容器镜像文件来做测试、CI和紧急部署，我们需要在一分钟内准备好镜像文件。dockerfile使得这一点几乎不可能。为了方便使用，就会处于一个抽象层比较高的位置，以致于不能处理这些复杂的用例：

Out-of-band caching for particularly heavy-weight and application-specific dependencies
Accessing secrets at build time without committing them to the image
Full control over layers in the final image
Parallelization of building layers

不同频道信息传输为特别重的应用或者特定应用的依赖做高速缓存
在创建镜像文件时，没有允许就进入了镜像文件的私密处
在最终的镜像文件上控制所有的镜像文件层
创建镜像层时的平行处理

Most people do not need these features, but for large applications many of them are prerequisites for fast builds. Configuration management software like Chef and Puppet is widespread, but feel too heavy handed for image building. I bet such systems will be phased out of existence in their current form within the next decade with containers. However, many applications rely on them for provisioning, deployment and orchestration. Dockerfiles cannot realistically capture the complexity now managed by config management, but this complexity needs to be managed somewhere. At Shopify we ended up creating our own system from scratch using the docker commit API. This is painful. I wish this on nobody and I am eager to throw it out, but we had to to unblock ourselves. Few will go to this length to wrangle containers to production.

大多数人不需要使用这些特性，但是对于大型应用，要想做到快速创建，这些是必须的。配置管理工具，如Chef、Puppet，使用广泛，但是对于创建镜像文件来说，太重量级了。我打赌这种系统将会在接下来的十年中淘汰。然而，许多应用需要依靠它们提供支持、部署和协调。dockerfile现在还不能真正地抓住配置管理的复杂性，但这个复杂性需要被管理。在shopify，我们不再通过docker提供的接口创建我们自己的系统。这是很痛苦的。我希望这种痛苦不会发生在别人身上。我想要抛弃这种痛苦，但我必须表露我自己。很少有人会对生产中的容器争论这么久。

What is going to emerge in this space is unclear, and currently it’s not an area where much exploration is being done (one example is dockramp, another packer). The Docker Engine will undergo work in the future to split the building primitives (adding files, setting entrypoints, and so on) from the client (Dockerfile). Work merged for 1.8 will already make this easier, opening the field for experimentation by configuration management vendors, hobbyists, and companies. Given the history of provisioning systems it’s unrealistic to believe a standard will settle for this problem, like it has for the runtime. The horizon for scalable image building is quite unclear. To my knowledge nobody is actively iterating and unfortunately it’s been this way for over a year.

将会出现的是不整洁，现在不是一个做了更多的探索的领域（一个例子是dockeramp，另一种包）。docker引擎将来会把基本体（增加文件、设置入口点等）从客户端分离。版本合并1.8已经让这些更容易了，通过配置管理供应商、爱好者和公司，让这些领域开放。基于提供系统的历史，很想相信用一个标准就可以解决问题，我们更倾向于在运行时解决。创建可计量的镜像文件的观点是很不清晰的。基于我的认识，没有人会积极地迭代，但很不幸，这种方法已经使用了超过一年。

#### Garbage collection

Every major deployment of Docker ends up writing a garbage collector to remove old images from hosts. Various heuristics are used, such as removing images older than x days, and enforcing at most y images present on the host. Spotify recently open-sourced theirs. We wrote our own a long time ago as well. I can understand how it can be tough to design a predictable UI for this, but it’s absolutely needed in core. Most people discover their need by accident when their production boxes scream for space. Eventually you’ll run into the same image for the Docker registry overflowing with large images, however, that problem is on the distribution roadmap.

#### 垃圾回收

每个主要的docker部署的最后一步通常都是写一个垃圾收集器从主机移除旧的镜像文件而告终。这里可以有许多种启发式算法，例如删除X天以前的镜像文件，并且至多主机上有y个镜像文件。Spotify最近把它们的方法开源了。我们以前很长一段时间也自己写。我能理解为垃圾回收设计一个UI是多么困难的事，但它确实需要。大多数人在他们产品的box空间爆满时候才偶然发现他们有这方面的需求。最终，你会运行到同一个镜像文件，因为registry里面充满了很大的镜像文件。这个问题在分布的路线图上。

#### Iteration speed and state of core

Docker Engine has focused on stability in the 1.x releases. Pre-1.5, little work was done to lower the barrier of entry for production uptake. Developing the public mental model of containers is integral to Docker’s success and they’re rightly terrified of damaging it. Iteration speed suffers when each UX change goes through excessive process. As of 1.7, Docker features experimental releases spearheaded by networking and storage plugins. These features are explicitly marked as “not ready for production” and may be pulled out of core or undergo major changes anytime. For companies already betting for Docker this is great news: it allows the core team to iterate faster on new features and not be concerned with breaking backwards compatibility between minor versions in the spirit of best design. It’s still difficult for companies to modify Docker core as it either requires a fork – a slippery slope and a maintenance burden – or getting accepted upstream which for interesting patches is often laborious. As of 1.7, with the announcement of plugins, the strategy for this problem is clear: Make every opinionated component pluggable, finally showing the fruits of the “batteries swappable, but included” philosophy first introduced (although rather vaguely) at DockerCon Europe 2014. At DockerCon in June it was great to hear this articulated under the umbrella of Plumbing as a top priority of the team (most importantly for me personally because plumbing was mascotted by my favorite marine mammal, the walrus). While the future finally looks promising, this remains a pain point today as it has been for the past two years.

####迭代的速度和core的状态

在1.5以前的版本里，Docker非常关注稳定性，却在运行产品时入口的界限方面做的工作比较少。为容器开发一个公共的心智模型会让docker更加成功。他们也担心会毁掉它。每个UX更新经过过多的流程时迭代速度会受到影响。至于1.7，docker以试验性的版本为特色，以网络和存储插件为主。这些特性被显式地打上了“测试版”的标签，可能随时会被从内核或者主要更新中除去。对于已经打算用docker的公司来说是件好事：因为它上内核组在开发新特性上有更快的迭代，而不用关心由于失败回退导致的小版本之间的不兼容。对于公司来说，修改docker核心仍然是困难的，因为这需要一个fork（一个灾难性的下滑和维护的负担），或获取。。。的认可。至于1.7，拥有插件的声明，这一问题的策略很明显：把每一种方案做成一个插件。在七月分的docker会议中，很高兴得知这个有关节的在插件的保护下作为一个高优先级的团队（对我个人来说很有意义，因为插件是我最喜欢的操作）。尽管未来看起来很有前途，这仍然是个痛点，在过去两年一直是。

#### Logging

One example of an area that could’ve profited from change earlier is logging. Hardly a glamorous problem but nonetheless a universal one. There’s currently no great, generic solution. In the wild they’re all over the map: tail log files, log inside the container, log to the host through a mount, log to the host’s syslog, expose them via something like fluentd, log directly to the network from their applications or log to a file and have another process send the logs to Kafka. In 1.6, support for logging drivers was merged into core; however, drivers have to be accepted in core (which is hardly easy). In 1.7, experimental support for out-of-process plugins was merged, but – to my disappointment – it didn’t ship with a logging driver. I believe this is planned for 1.8, but couldn’t find that on official record. At that point, vendors will be able to write their own logging drivers. Sharing within the community will be trivial and no longer will larger applications have to resort to engineering a custom solution.

#### 日志

有一个领域可以从早期的变化中获利，那就是日志。很难有一个问题，但是不是唯一的问题。现在没有很好很通用的解决方案。一般它们都使用地图：尾日志文件，容器内日志，主机日志，主机系统日志的日志，通过fluentd，直接从网络记录应用的日志，或者记入日志到一个文件然后用另一个进程把日志发给kafka。在1.6版本中，对日志驱动的支持被合到了核心版本。然后核心必须接受驱动（通常很不容易）。在1.7版本中，试验性地支持不同进程的插件被合进来了，但是（很遗憾），它并没有合入日志驱动。我相信1.8在计划这个，但官方记录里没有说。就这一点，卖主们会写它们自己的日志驱动。把日志驱动分享到社区只是一件小事，大型的应用不再需要求助工程学来处理一个通常的解决方案。

#### Secrets
In the same category of less than captivating but widespread pickles, we find secrets. Most people migrating to containers rely on configuration management to provision secrets on machines securely; however, continuing down the path of configuration management for secrets in containers is clunky. Another alternative is distributing them with the image, but that poses security risks and makes it difficult to securely recycle images between development, CI, and production. The most pure solution is to access secrets over the network, keeping the filesystem of containers stateless. Until recently nothing container-oriented existed in this space, but recently two compelling secret brokers, Vault and Keywhiz, were open-sourced. At Shopify we developed ejson a year and a half ago to solve this problem to manage asymmetrically encrypted secrets files in JSON; however, it makes some assumptions about the environment it runs in that make it less ideal as a general solution compared to secret brokers (read this post if you’re curious).

#### 私密

在与captivating同一个目录下，我们找到私密。大多数使用容器的人都依赖于对私密的安全的配置管理。然而，持续的深入私密配置管理的路径。另一个替代方案的是把它们与镜像文件区分，但是这会导导致安全风险，使安全镜像文件的循环在开发、CI和产品中产生困难。直到最近，还不存在容器为导向的东西，但最近两个平行的私密破坏-Vault和Keywhiz，都是开源的。在shopify，我们开发了ejson一年半，解决了这个问题，管理非对称的私密脚本文件用JSON。然而，它基于运行在理想化的环境的假设。

#### Filesystems

Docker relies on CoW (Copy on Write) from the filesystem (great LWN series on union filesystems, which enable CoW). This is to make sure that if you have 100 containers running from an image, you don’t need 100 * disk space. Instead, each container creates a CoW layer on top of the image and only uses disk space when it changes a file from the original image. Good container citizens have a minimal impact on the filesystem inside the container, as such changes means the container takes on state, which is a no-no. Such state should be stored on a volume that maps to the host or over the network. Additionally, layering saves space between deployments as images are often similar and have layers in common. The problem with file systems that support CoW on Linux is that they’re all somewhat new. Experience with a handful of them at Shopify on a couple hundreds of hosts under significant load:

#### 文件系统

docker基于文件系统（联合文件系统上的LWN系列支持CoW）的CoW（写时复制）。这使得如果有100个容器来自于同一个镜像文件，你不需要100倍的磁盘空间。相反，每一个容器在镜像文件上创建一个写时复制层，只有当原镜像文件中有文件被改变时在真正地分配空间。好的空间用户对容器内的文件系统的影响很小，像这样的改变意味着容器的状态是no-no。这种状态存储在volume中，指示主机或者网络。另外，层节省了空间，因为部署的镜像文件通常是相似的，或者有相同的层。文件系统在linux上支持CoW的问题是它们比较新。在shopity，有一些棘手的体验：

AUFS. Seen entire partitions lock up where we had to remount it. Sluggish and uses a lot of memory. The code-base is large and difficult to read, which is likely why it hasn’t been accepted into upstream and thus requires a custom kernel.

AUFS。看上去完整，我们不得不增加。市况萧条，花了很多钱。基于代码很大，难以阅读，很可能就是不能被主流接受需要一个核心客户的原因。

BTRFS. Has a learning curve through a new set of tools as du and ls don’t work. As with AUFS, we’ve seen partitions freeze and kernels lock up despite playing cat and mouse with kernel versions to stay up to date. When nearing disk space capacity, BTRFS acts unpredictably, and the same goes if you have 1000s of these CoW layers (subvolumes in BTRFS-terminology). BTRFS uses a lot of memory.

BTRFS。有一个学习曲线，通过一系列新的工具例如du和ls不起作用。相对于AUFS，我们对于内核锁，而不需要为了更新与内核版本玩猫和老鼠的游戏。接近磁盘空间容量时，BTRFS的行为不可预测。这样的1000个CoW层时，行为同样不可预测（BTRFS技术中的子卷）。BTRFS要用很多钱。

OverlayFS. This was merged into the Linux kernel in 3.18, and has been quite stable and fast for us. It uses a lot less memory as it manages to share the page cache between inodes. Unfortunately it requires you run a recent kernel not adopted by most distributions, which often means building your own.

OverlayFS。这个已经被合到linux内核3.18中了，而且非常稳定，效率也很高。由于它能够在i节点间共享页缓存，所以花费要少得多。不幸的是，它要求你必须使用比较新的内核，而且大部分版本中不能使用，所以你通常需要自己去构建一个。

Luckily for Docker, Overlay will soon be ubiquitous, but the default of AUFS is still quite unsafe for production when running a large amount of nodes in our experience. It’s hard to say what to do here though since most distributions don’t ship with a kernel that’s ready for Overlay either (it’s been proposed and rejected as the default for that reason), although this is definitely where the space is heading. It seems we just have to wait.

docker很幸运，overlay很快就会变得通用了，但是，根据我们的经验，AUFS的默认版本对于有大量结点的产品来说，仍然很不安全。很难说这里会做什么，尽管大多数版本不会移植内核（这也是被推荐或者拒绝的原因），尽管很明显有空间。看来我们不得不等待。

#### Reliance on edgy kernel features

Just as Docker relies on the frontier of file systems, it also leverages a large number of recent additions to the kernel, namely namespaces and (not-so-recent, but also not too commonly used) cgroups. These features (especially namespaces) are not yet battle-hardened from wide adoption in the industry. We run into obscure bugs with these once in a while. We run with the network namespace disabled in production because we’ve experienced a fair amount of soft-lockups that we’ve traced to the implementation, but haven’t had the resources to fix upstream. The memory cgroup uses a fair amount of memory, and I’ve heard unreliable reports from the wild. As containers see more and more use, it’s likely the larger companies that will pioneer this stability work.

#### 对内核特性的依赖
正如docker依赖文件系统，它也会影响内核的附加物，也就是命名空间和（不是最近，但是也不是很常用）cgroups。这些特性（尤其是命名空间）还不能被工厂广泛接受。曾经有一次因为这些进入难以理解的bug中。我们在运行产品时禁用网络命名空间，因为我们遇到了许多用于实现的软件锁，但是还没有资源去修复主流。内存cgroup使用大量的内容空间，我从未证实的小道消息听说。

An example of hardening we’ve run into in production would be zombie processes. A container runs in a PID namespace which means that the first process inside the container has pid 1. The init in the container needs to perform the special duty of acknowledging dead children. When a process dies, it doesn’t immediately disappear from the kernel process data structure but rather becomes a zombie process. This ensures that its parent can detect its death via wait(2). However, if a child process is orphaned its parent is set to init. When that process then dies, it’s init’s job to acknowledge the death of the child with wait(2)—otherwise the zombie sticks around forever. This way you can exhaust the kernel process data structure with zombie processes, and from there on you’re on your own. This is a fairly common scenario for process-based master/worker models. If a worker shells out and it takes a long time the master might kill the worker waiting for the shelled command with SIGKILL (unless you’re using process groups and killing the entire group at once which most don’t). The forked process that was shelled out to will then be inherited by init. When it finally finishes, init needs to wait(2) on it. Docker Engine can solve this problem by the Docker Engine acknowledging zombies within the containers with PR_SET_CHILD_SUBREAPER, as described in #11529.

Security
Runtime security is still somewhat of a question mark for containers, and to get it production hardened is a classic chicken and egg security problem. In our case, we don’t rely on containers providing any additional security guarantees. However, many use cases do. For this reason most vendors still run containers in virtual machines, which have battle-tested security. I hope to see VMs die within the next decade as operating system virtualization wins the battle, as someone once said on the Linux mailing list: “I once heard that hypervisors are the living proof of operating system’s incompetence”. Containers provide the perfect middle-ground between virtual machines (hardware level virtualization) and PaaS (application level). I know that more work is being done for the runtime, such as being able to blacklist system calls. Security around images has been cause for concern but Docker is actively working on improving this with libtrust and notary which will be part of the new distribution layer.

Image layers and transportation
The first iteration of Docker took a clever shortcut for image builds, transportation and runtime. Instead of choosing the right tool for each problem, it chose one that worked OK for all cases: filesystem layers. This abstraction leaks all the way down to running the container in production. This is perfectly acceptable minimum viable product pragmatism, but each problem can be solved much more efficiently:

Image builds could be represented as a directed graph of work. This allows figuring out caching and parallelization for fast, predictable builds.
Image transportation instead of using image layers it could perform binary diffing. This is a topic that has been studied for decades. The distribution and runtime layer are getting more and more separated, opening up for this sort of optimization.
Runtime should just do a single CoW layer rather than using the arbitrary image layer abstraction again. If you’re using a union filesystem such as AUFS on the first read you’re traversing a linked list of files to assemble the final file. This is slow and completely unnecessary.
The layer model is a problem for transportation (and for building, as covered earlier). It means that you have to be extremely careful about what is in each layer of your image as otherwise you easily end up transporting 100s of MBs of data for a large application. If you have large links within your own datacenter this is less of a problem, but if you wish to use a registry service such as Docker Hub this is transferred over the open Internet. Image distribution is being worked on actively currently. There’s a lot of incentive for Docker Inc to make this solid, secure and fast. Just as for building, I hope that this will be opened for plugins to allow a great solution to surface. As opposed to the builder this is somewhere people can generally agree on a sane default, with specialized mechanisms such as bittorrent distribution.

Conclusion
Many other topics haven’t been discussed on purpose, such as storage, networking, multi-tenancy, orchestration and service discovery. What Docker needs today is more people going to production with containers alone at scale. Unfortunately, many companies are trying to overcompensate from their current stack by shooting for the stars of a PaaS from the get go. This approach only works if you’re small or planning on doing greenfield deployments with Docker—which rarely run into all the obscurities of production. To see more widespread production usage, we need to tip the pro/con scale in favour of Docker by resolving some of the issues highlighted above.

Docker is putting itself in an exciting place as the interface to PaaS be it discovery, networking or service discovery with applications not having to care about the underlying infrastructure. This is great news, because as Solomon says, the best thing about Docker is that it gets people to agree on something. We’re finally starting to agree on more than just images and the runtime.

All of the topics above I’ve discussed in length with the great people at Docker Inc, and GitHub Issues exist in some capacity for all of them. What I’ve attempted to do here, is simply provide an opinionated view of the most important areas to ramp down the barrier of entry. I’m excited for the future—but we’ve still got a lot of work left to make production more accessible.