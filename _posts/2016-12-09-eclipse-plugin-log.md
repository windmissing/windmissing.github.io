---
layout: post
title:  "eclipse插件开发 - 打log"
category: [编程语言]
tags: [eclipse, plugin, log]
---

eclipse插件在开发过程中可以通过`System.out.println(message)`打log，测试时通过Console查看log。  
插件到加载到真实环境中后，这些log就看不到了。

<!-- more -->

#### 解决方法

```
IProject project = null;    
ILog log = Activator.getDefault().getLog();
Status status = new Status(IStatus.ERROR, Activator.PLUGIN_ID, IStatus.ERROR, message, null);
log.log(status);
```

然后到使用插件的eclipse的workspace下查看log  

workspace/.metadata/.log