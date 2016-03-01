---
layout: post
title:  "valgrind memcheck 使用malloc/new/new[]和free/delete/delete[]不匹配"
category: linux
tags: [valgrind, memcheck]
---

关于valgrind memcheck请阅读[《valgrind memcheck使用方法及效果》](/linux/2016-02/valgrind-memcheck.html)

在这里，我列举了三种不匹配的情况

- malloc/delete或new/free

- new/delete[]或new[]/delete

<!-- more -->

#### 一、malloc/delete或new/free

```c++
#include <iostream>
using namespace std;
#include "unistd.h"
#include "stdlib.h"


int main()
{
    int *p1 = new int;
    free(p1);

    int *p2 = (int *)malloc(sizeof(int));
    delete p2;
}
```

###### 编译及运行

```
g++ -g -o mismatch1 val-mismatch1.cpp 
valgrind  ./mismatch1
```

###### 检测结果

```
==8885== Mismatched free() / delete / delete []
==8885==    at 0x4C2AD17: free (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==8885==    by 0x400821: main (val-mismatch1.cpp:9)
==8885==  Address 0x5a15040 is 0 bytes inside a block of size 4 alloc'd
==8885==    at 0x4C2A105: operator new(unsigned long) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==8885==    by 0x400811: main (val-mismatch1.cpp:8)
==8885== 
==8885== Mismatched free() / delete / delete []
==8885==    at 0x4C2B131: operator delete(void*) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==8885==    by 0x40083B: main (val-mismatch1.cpp:12)
==8885==  Address 0x5a15090 is 0 bytes inside a block of size 4 alloc'd
==8885==    at 0x4C29BFD: malloc (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==8885==    by 0x40082B: main (val-mismatch1.cpp:11)
```

###### 检测结果解读

1.可以检测出malloc/delete或new/free

2.申请和释放代码的详细堆栈信息都会给出

#### 二、new/delete[]或new[]/delete

###### 测试代码

```c++
#include <iostream>
using namespace std;

int main()
{
    int *p1 = new int[5];
    delete p1;

    int *p2 = new int;
    delete []p2;

    return 0;
}
```

###### 检测结果

```
==9167== Mismatched free() / delete / delete []
==9167==    at 0x4C2B131: operator delete(void*) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==9167==    by 0x400821: main (val-mismatch1.cpp:7)
==9167==  Address 0x5a15040 is 0 bytes inside a block of size 20 alloc'd
==9167==    at 0x4C2A7AA: operator new[](unsigned long) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==9167==    by 0x400811: main (val-mismatch1.cpp:6)
==9167== 
==9167== Mismatched free() / delete / delete []
==9167==    at 0x4C2B5E1: operator delete[](void*) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==9167==    by 0x400842: main (val-mismatch1.cpp:10)
==9167==  Address 0x5a150a0 is 0 bytes inside a block of size 4 alloc'd
==9167==    at 0x4C2A105: operator new(unsigned long) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==9167==    by 0x40082B: main (val-mismatch1.cpp:9)
```

###### 检测结果解读

1.可以检测出new/delete[]或new[]/delete

2.申请和释放代码的详细堆栈信息都会给出
