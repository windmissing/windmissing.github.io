---
layout: post
title:  "valgrind memcheck 读/写已经被释放的内存"
category: linux
tags: [valgrind, memcheck]
---

关于valgrind memcheck请阅读[《valgrind memcheck使用方法及效果》](/linux/2016-02/valgrind-memcheck.html)

在这里，我列举了两种读/写已经被释放的内存的情况

- 读写已经释放的堆内存

- 读写已经释放的栈内存

<!-- more -->

#### 一、读写已经释放的堆内存

##### 测试代码

```c++
#include <iostream>
using namespace std;

int main()
{
    int *p = new int;
    delete p;

    *p = 3;
    return 0;
}
```

##### 编译及运行

```
g++ -g -o deleted1 val-deleted1.cpp
valgrind ./deleted1
```

##### 检测结果

```
==11588== Invalid write of size 4
==11588==    at 0x400796: main (val-deleted.cpp:9)
==11588==  Address 0x5a15040 is 0 bytes inside a block of size 4 free'd
==11588==    at 0x4C2B131: operator delete(void*) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==11588==    by 0x400791: main (val-deleted.cpp:7)
```
##### 检测结果解读

1.“读/写已经被释放的内存”可以被检测出来

2.打印的信息只会提示“释放内存”的代码，不会提示“使用释放的内存”的代码

#### 二、读写已经释放的栈内存

##### 测试代码

```c++
#include <iostream>
using namespace std;

int *func()
{
    int a = 3;
    return &a;
}
int main()
{
    int *p = func();
    cout<<*p<<endl;
    return 0;
}
```

##### 检测结果

```
==28518== Use of uninitialised value of size 8
==28518==    at 0x4EBF4F3: ??? (in /usr/lib64/libstdc++.so.6.0.19)
==28518==    by 0x4EBF635: std::ostreambuf_iterator<char, std::char_traits<char> > std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::_M_insert_int<long>(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib64/libstdc++.so.6.0.19)
==28518==    by 0x4EBFBEC: std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::do_put(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib64/libstdc++.so.6.0.19)
==28518==    by 0x4ECBF7D: std::ostream& std::ostream::_M_insert<long>(long) (in /usr/lib64/libstdc++.so.6.0.19)
==28518==    by 0x400873: main (val-deleted1.cpp:12)
```

##### 检测结果解读

1.valgrind memcheck不能检查“读写已释放的栈内空间”，但编译时会有warning来避免这类问题

2.指向“已释放的栈内空间”的指针会被当成未初始化的指针
