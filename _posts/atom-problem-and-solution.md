---
layout: post
title:  "atom遇到的问题及解决方法"
category: [opensource]
tags: [atom]
---

#### 问题一：安装package

参考[《atom安装package遇到的问题》](http://windmissing.github.io/opensource/2016-11/atom-install-package-error.html)

#### 问题二：git push不成功，又没有任何错误提示

在atom中push不成功，又没有任何错误提示。  
在git bash中push，提示输入用户名和密码。  
原因是使用了https协议，应改成ssh协议(要先把~/.ssh/id_rsa.pub加到git的工程中)。

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