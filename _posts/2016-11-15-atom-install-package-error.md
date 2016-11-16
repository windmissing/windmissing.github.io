---
layout: post
title:  "atom安装package遇到的问题"
category: [opensource]
tags: []
---

#### 问题一：

can't connect to

原因：可能代理的问题

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
有可能只是网速的问题。
