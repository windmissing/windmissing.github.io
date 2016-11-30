---
layout: post
title:  "atom遇到的问题及解决方法"
category: [opensource]
tags: [atom]
---

#### 问题一：git push不成功，又没有任何错误提示

在atom中push不成功，又没有任何错误提示。  
在git bash中push，提示输入用户名和密码。  
原因是使用了https协议，改成ssh协议可以解决此问题。

<!-- more -->

1.把~/.ssh/id_rsa.pub加到git的工程中  
2.改协议  

```
git remote -v
origin  https://github.com/windmissing/windmissing.github.io.git (fetch)
origin  https://github.com/windmissing/windmissing.github.io.git (push)

git remote rm origin

git remote add origin git@github.com:windmissi
ng/windmissing.github.io.git

git remote -v
origin  git@github.com:windmissing/windmissing.github.io.git (fetch)
origin  git@github.com:windmissing/windmissing.github.io.git (push)
```

#### 问题二：安装package

参考[《atom安装package遇到的问题》](http://windmissing.github.io/opensource/2016-11/atom-install-package-error.html)

#### 问题三、中文不会自动换行

Settings -> Editor  
勾选Soft Wrap

#### 问题四、markdown文件保存后行尾的空格自动消失

markdown文件的行尾增加两个空格表示一行结束需要换行。  
但保存文件后，行尾的空格自动消失，导致不换行。  
Settings -> Packages -> whitespace  
whitespace Settings -> Keep Markdown Line Break Whitespace勾选  
若还不能解决，直接把这个插件禁用掉  

#### 问题五、一些实用的插件

|名字|作用|git repo|
|---|---|---|
|Activate Power Mode|subline的拉动效果|https://github.com/JoelBesada/activate-power-mode.git|
|atom-beautify|代码格式化|https://github.com/Glavin001/atom-beautify.git|
|Atom HTML Preview|实时预览html|
|file icons|使左边的树形目录很好看|
|git plus|更方便地使用git
|markdown-scroll-sync Atom editor package|markdown的预览可以同步滚动|
|minimap|缩略图|

##### python相关

|名字|作用|git repo|
|---|---|---|
|autocomplete python| 自动补全|https://github.com/autocomplete-python/autocomplete-python.git|
|python-tools|
|linter-flake8(或者其他flavor)|
|atom-runner|run various script files inside of Atom| https://github.com/lsegal/atom-runner.git|
|python-autopep8 |自动符合pep8代码规范|
|simplified-chinese-menu|可以让你在atom里直接运行脚本|https://github.com/chinakids/atom-simplified-chinese-menu.git|

