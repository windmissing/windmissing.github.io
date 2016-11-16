---
layout: post
title:  "【译】git push报Bad file number"
category: opensource
tags: [git]
---

这个问题通常意味着你不能连接到git服务器。
通常与防火墙或代理服务器有关。

#### 问题现象

当运行remote git命令或SSH时，提示连接超时。

```
$ ssh -vT git@github.com
OpenSSH_5.8p1, OpenSSL 1.0.0d 8 Feb 2011
debug1: Connecting to github.com [207.97.227.239] port 22.
debug1: connect to address 207.97.227.239 port 22: Connection timed out
ssh: connect to host github.com port 22: Connection timed out
ssh: connect to host github.com port 22: Bad file number
```

<!-- more -->

#### 方法一：使用HTTPS

最简单的方法就是完全避免使用SSH。大多数防火墙和代理都会允许HTTPS包，使用HTTPS不会出现这样的问题。
使用这种方法，只须修改[remote URL](https://help.github.com/articles/which-remote-url-should-i-use/)。

```
$ git clone https://github.com/username/reponame.git
Cloning into 'reponame'...
remote: Counting objects: 84, done.
remote: Compressing objects: 100% (45/45), done.
remote: Total 84 (delta 43), reused 78 (delta 37)
Unpacking objects: 100% (84/84), done.
```

#### 方法二：使用不同的网络

如果你能连一个没有防火墙的网络，你可以使用另一个网络来测试SSH到GitHub的连接情况。
如果在另一个网络中一切正常，联系你的网络管理员修改防火墙设置，允许你的SSH连接到GitHub。

#### 方法三：使用基于(over)HTTPS端口的SSH

如果不能使用HTTPS，你的防火墙管理员又拒绝SSH连接，你可以试试基于HTTPS端口的SSH。
大多数防火墙规则可以支持这种方法，但代理服务器可能会有影响。

> 对于GitHub企业级用户，通过基于HTTPS端口的SSH访问GitHub企业版的方法目前还不支持。

使用以下命令测试基于HTTPS端口的SSH是否可行：

```
$ ssh -T -p 443 git@ssh.github.com
Hi username! You've successfully authenticated, but GitHub does not
provide shell access.
```

如果这条命令有效，那就可行。否则，可以参考[follow our troubleshooting guide](https://help.github.com/articles/error-permission-denied-publickey/)

##### 启用基于HTTPS的SSH连接

如果你能通过SSH连接`git@ssh.github.com`的443端口，你可以重写SSH配置，使得所有与GitHub的连接都会使用那个服务器和端口。

编辑`~/.ssh/config`，配置ssh，增加以下内容：

```
Host github.com
Hostname ssh.github.com
Port 443
```

通过以下测试config是否工作

```
$ ssh -T git@github.com
Hi username! You've successfully authenticated, but GitHub does not
provide shell access.
```

---

原文：https://help.github.com/articles/error-bad-file-number/
