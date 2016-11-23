---
layout: post
title:  "atom安装package遇到的问题"
category: [opensource]
tags: [atom]
---

#### 问题一：

```
connect ETIMEDOUT 54.197.251.22:443
```

<!-- more -->

原因：可能代理的问题
客户端和浏览器走的代理不同。
如果只对浏览器设置了代码，浏览器可以访问，但客户端还是不行。
设置客户端代理的方法：

```
cmd
netsh winhttp import proxy source=ie
```

#### 问题二：

```
gyp info it worked if it ends with ok
gyp info using node-gyp@3.4.0
gyp info using node@4.4.5 | win32 | ia32
gyp http GET https://atom.io/download/atom-shell/v1.3.6/iojs-v1.3.6.tar.gz
gyp http 200 https://atom.io/download/atom-shell/v1.3.6/iojs-v1.3.6.tar.gz
gyp WARN install got an error, rolling back install
gyp ERR! install error
gyp ERR! stack Error: EPERM: operation not permitted, open
```

有可能是墙的问题。
有可能只是网速的问题，过会再试。
也可以选择离线安装。

#### 问题三：离线安装package

进入atom package的安装目录，例如我的目录是~/.atom/package  
使用git clone从git hub上下载插件的整个工程，并进入工程目录，例如：

```
git clone https://github.com/webBoxio/atom-html-preview.git
cd atom-html-preview
```

`apm install`或者`npm install`


