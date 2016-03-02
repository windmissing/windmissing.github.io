---
layout: post
title:  "valgrind memcheck src和dst的重叠"
category: linux
tags: [valgrind, memcheck]
---

关于valgrind memcheck请阅读[《valgrind memcheck使用方法及效果》](/linux/2016-02/valgrind-memcheck.html)

在这里，我列举了两种src和dst的重叠的情况

- memcmp

- memcpy

<!-- more -->

#### 一、memcmp

##### 测试代码

```c++
#include <iostream>
using namespace std;

#include "string.h"

int main()
{
    char ch[10] = "abcdefghi";
    char *p1 = ch;
    char *p2 = ch + 3;
    memcmp(p1, p2, 5);
    return 0;
}
```

##### 编译及运行

```
g++ -g -o overlap1 val-overlap1.cpp
valgrind ./overlap1
```

##### 检测结果

```
==29405== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 2 from 2)
```

##### 检测结果解读

对于不涉及到写的情况，src和dst重叠不算是问题

#### 二、memcpy

##### 测试代码

```c++
==29520== Source and destination overlap in memcpy(0x5a15045, 0x5a15040, 8)
==29520==    at 0x4C2E7BC: __GI_memcpy (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==29520==    by 0x40086F: main (val-overlap1.cpp:10)
```

##### 检测结果

```
==29520== Source and destination overlap in memcpy(0x5a15045, 0x5a15040, 8)
==29520==    at 0x4C2E7BC: __GI_memcpy (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==29520==    by 0x40086F: main (val-overlap1.cpp:10)
```

##### 检测结果解读

涉及到写操作的src与dst重叠问题是可以检测出来
