---
layout: post
title:  "git使用技巧"
category: [opensource]
tags: [git]
---

#### 在git比较中使用BC

This tip is to use BC as difftool in git command.

Add the following configuration in gitconfig file in your git tool installation directory, such as "C:\Program Files (x86)\Git\etc". Replace original diff setting if existing.

<!-- more -->

```
[diff]
tool = bc
[difftool]
prompt = false
[difftool "bc"]
cmd = \"C:/apps/bc/BCompare.exe\" \"$LOCAL\" \"$REMOTE\"

[merge]
tool = bc
[mergetool]
prompt = false
[mergetool "bc"]
cmd = \"C:/apps/bc/BCompare.exe\" \"$LOCAL\" \"$REMOTE\" \"$BASE\" \"$MERGED\"
```

Command "git difftool " and "git mergetool" can be used to use BCompare to diff and merge.

#### get remote branch that you only want

You can follow those steps witch remote repository:
1.	$git remote add admin git@esmz01.emea.nsn-net.net:admin-ftw15/admin.git
2.	$git fetch admin remote_branch_name   //get remote branch to local
3.	$git checkout –b local_branch_name admin/remote_branch_name
4.	$git remote remove origin

If you use $git branch –a, you can find it has only one remote branch name.

#### 生成RSA

```
ssh-keygen -t rsa -C "xxxxx@xxx.com"
```

#### Git学习网站

需翻墙：  
http://pcottle.github.io/learnGitBranching/?NODEMO&defaultTab=remote&command=levels
