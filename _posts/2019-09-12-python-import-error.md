---
layout: post
title:  "间接调用虚函数"
category: [编程语言]
tags: [python]
---

# 问题现象：

pycharm运行python报错如下：

```
ImportError: No module named 'lxml'
```
但实际上lxml已经安装了，

```
Requirement already satisfied: lxml in c:\users\yinahe\appdata\local\programs\python\python35\lib\site-packages (4.4.1)
```

<!-- more -->

# 解决方法

pycharm -> file -> settings -> project -> project interpreter

![](\images\2019\14.png)

看到package列表里确实没有lxml。

![](\images\2019\15.png)

发现project Interpreter的路径与lxml的路径不同。怀疑是因为系统里装了两个python导致。

从project interpreter的下拉菜单中选择了与lxml相同路径的interpreter。

![](\images\2019\16.png)

package列表中多了很多内容，lxml也在其中，

点击apply，问题解决
