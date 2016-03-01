---
layout: post
title:  "valgrind memcheck 内存泄漏"
category: linux
tags: [valgrind, memcheck]
---

关于valgrind memcheck请阅读[《valgrind memcheck使用方法及效果》](/linux/2016-02/valgrind-memcheck.html)

在这里，我列举了两种内存泄漏的情况

- 申请堆内存后没有释放

- 申请子类空间释放父类空间

<!-- more -->

#### 一、申请堆内存后没有释放

###### 测试代码

```c++
#include <iostream>
using namespace std;

int main()
{
    int *p = new int;
    return 0;
}
```

###### 编译及运行

```
g++ -g -o memleak1 val-memleak1.cpp
valgrind --leak-check=full ./memleak1
```

###### 检测结果

```
==8544== 4 bytes in 1 blocks are definitely lost in loss record 1 of 1
==8544==    at 0x4C2A105: operator new(unsigned long) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==8544==    by 0x400741: main (in /home/vagrant/git_hub/windmissing.github.io/_posts/memleak1)
```

###### 检测结果解读

1.内存泄漏可以被检测出来

2.检测结果会给出详细的堆栈信息及行号

3.检测结果会给出泄漏存内的大小

#### 二、申请子类空间释放父类空间

###### 测试代码

```c++
#include <iostream>
using namespace std;

void test2()
{
    int *p = new int;
    char *p2 = (char *)p;
    delete p2;
}

class father
{
    int *p;
public:
    father(){p = new int;}
    ~father(){delete p;}
};

class son : public father
{
    int *p2;
public:
    son(){p2 = new int;}
    ~son(){delete p2;}
};

void test3()
{
    father *p = new son;
    delete p;
};
int main()
{
    father *p = new son;
    delete p;
    return 0;
}
```

###### 检测结果

```
==8659== 4 bytes in 1 blocks are definitely lost in loss record 1 of 1
==8659==    at 0x4C2A105: operator new(unsigned long) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==8659==    by 0x400A00: son::son() (in /home/vagrant/git_hub/windmissing.github.io/_posts/memleak1)
==8659==    by 0x400909: main (in /home/vagrant/git_hub/windmissing.github.io/_posts/memleak1)
```

###### 检测结果解读

1.内存泄漏可以被检测出来

2.检测结果会给出详细的堆栈信息及行号

3.检测结果会给出泄漏存内的大小
