---
layout: post
title:  "emacs常用快捷键"
category: editor
tags: [emacs, editor]
---

C = ctrl, M = alt

#### 文件操作

||||
|---|---|---|
|打开文件|C-x, C-f|
|保存文件|C-x，C-s|
|保存所有文件|C-x, s|!保存所有文件

#### 窗口操作

||||
|---|---|---|
|关闭当前窗口|C-x, 0|
|关闭所有其它窗口|C-x，1|
|在上方打开一个窗口|C-x, 2|
|在左边打开一个窗口|C-x, 3|
|切换窗口   | C-x o  |

#### 阅读文件

||||
---|---|---
跳转到某一行  | M-g, M-g, 行号  |   |
跳转到行开头  | C-a  |   |
跳转到行尾	  | C-e  |   |
新增书签  | Ctrl +x r m  |   |
跳转到书签  | Ctrl + x r b  |   |
删除书签  | Ctrl + x r d  |   |
设置搜索时过滤某些文件夹  | Alt + x, set variables, grep find ignore directories  | 这是一次性生效的。	如果要永久生效，set variable改成customize variables。保存时会提示永久生效的配置会写到哪个配置文件。也可以直接改那个配置文件

#### 编辑文件

||||
---|---|---
复制|M-w|
替换|M-%|		
粘贴|M-y|
删除到行尾|C-k|
删除整行   | C-K  |
  撤消 | Ctrl + x, u	  |

#### git操作

|||
|---|---|
|打开git控制台|A+x, git status|
|查询可以使用的操作   | ？  |
|add files|a|
|commit with comments|ci|
|commit --amend   | ca  |
|save comments and commit|C-c, C-c|
|stage   | s  |
