---
layout: post
title:  "valgrind memcheck 使用未初始化的内存"
category: linux
tags: [valgrind, memcheck]
---

关于valgrind memcheck请阅读[《valgrind memcheck使用方法及效果》](/linux/2016-02/valgrind-memcheck.html)

在这里，我列举了三种使用未初始化内存的情况

- 使用未初始化的栈空间

- 使用未初始化的堆空间

- 间接读取未初始化的内存

<!-- more -->

#### 一、使用未初始化的栈空间

##### 测试代码

```c++
#include <iostream>
using namespace std;
int main()
{
    int a;
    cout<<a+3<<endl;
    return 0;
}
```
##### 编译及运行

```
g++ -g -o uninit1 val-uninit1.cpp
valgrind --track-origins=yes ./uninit1
```

`--track-origins=yes`表示开启“使用未初始化的内存”的检测功能，并打开详细结果。如果没有这句话，默认也会做这方面的检测，但不会打印详细结果。

##### 检测结果

头部的版本信息和尾部的总结将不再赘述。

打印太多，只节选其中一部分。

```
==31549== Use of uninitialised value of size 8
==31549==    at 0x4EBF4F3: ??? (in /usr/lib64/libstdc++.so.6.0.19)
==31549==    by 0x4EBF635: std::ostreambuf_iterator<char, std::char_traits<char> > std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::_M_insert_int<long>(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib64/libstdc++.so.6.0.19)
==31549==    by 0x4EBFBEC: std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::do_put(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib64/libstdc++.so.6.0.19)
==31549==    by 0x4ECBF7D: std::ostream& std::ostream::_M_insert<long>(long) (in /usr/lib64/libstdc++.so.6.0.19)
==31549==    by 0x400859: main (val-uninit1.cpp:6)
==31549==  Uninitialised value was created by a stack allocation
==31549==    at 0x400840: main (val-uninit1.cpp:4)
```

##### 检测结果解读

1.未初始化的栈空间可以被检测出来

2.可以识别出所使用的空间是一个栈空间，参考《检测结果》倒数第二行。

3.能够打印出完整的堆栈信息，尽管在本例中并不需要。

4.能够定位到使用者所在的行。

5.能够计算出未初始化空间的大小，不过貌似是错的，int的大小应该是4。

#### 二、使用未初始化的堆空间

##### 测试代码

```c++
#include <iostream>
using namespace std;
int main()
{
    int *p = new int;
    cout<<*p<<endl;
    delete p;
    return 0;
}
```
##### 检测结果

```
==31942== Use of uninitialised value of size 8
==31942==    at 0x4EBF4F3: ??? (in /usr/lib64/libstdc++.so.6.0.19)
==31942==    by 0x4EBF635: std::ostreambuf_iterator<char, std::char_traits<char> > std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::_M_insert_int<long>(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib64/libstdc++.so.6.0.19)
==31942==    by 0x4EBFBEC: std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::do_put(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib64/libstdc++.so.6.0.19)
==31942==    by 0x4ECBF7D: std::ostream& std::ostream::_M_insert<long>(long) (in /usr/lib64/libstdc++.so.6.0.19)
==31942==    by 0x4008F7: main (val-uninit1.cpp:6)
==31942==  Uninitialised value was created by a heap allocation
==31942==    at 0x4C2A105: operator new(unsigned long) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==31942==    by 0x4008E1: main (val-uninit1.cpp:5)
```

##### 检测结果解读

1.未初始化的堆空间可以被检测出来

2.可以识别出所使用的空间是一个堆空间，参考《检测结果》倒数第三行。

3.能够打印出完整的堆栈信息，尽管在本例中并不需要。

4.能够定位到使用者所在的行。

5.能够计算出未初始化空间的大小，不过貌似是错的，int的大小应该是4。

#### 三、间接读取未初始化的内存

##### 测试代码

```c++
#include <iostream>
using namespace std;
#include "string.h"
int main()
{
    char *p1 = new char[50];
    char *p2 = new char[50];
    memcpy(p1, p2, 50);
    cout<<p1[4]<<endl;
    delete []p1;
    delete []p2;
    return 0;
}
```

在这段代码中有两种使用未初始化的堆空间。

第一次是在L8，把p2指向的数据赋值给p1，但实际上p2的空间是没有初始化的。

第二次是在L9，p1的数据虽然来自于p2，但由于数据来源本身就不对，所以p1的数据其实也不是有意义的内容。

##### 检测结果

```
==32041== Syscall param write(buf) points to uninitialised byte(s)
==32041==    at 0x573B9E0: __write_nocancel (in /usr/lib64/libc-2.17.so)
==32041==    by 0x56CAE72: _IO_file_write@@GLIBC_2.2.5 (in /usr/lib64/libc-2.17.so)
==32041==    by 0x56CC2DB: _IO_do_write@@GLIBC_2.2.5 (in /usr/lib64/libc-2.17.so)
==32041==    by 0x56CC6B2: _IO_file_overflow@@GLIBC_2.2.5 (in /usr/lib64/libc-2.17.so)
==32041==    by 0x56C8B08: putc (in /usr/lib64/libc-2.17.so)
==32041==    by 0x4ECB4D5: std::ostream::put(char) (in /usr/lib64/libstdc++.so.6.0.19)
==32041==    by 0x4ECB721: std::basic_ostream<char, std::char_traits<char> >& std::endl<char, std::char_traits<char> >(std::basic_ostream<char, std::char_traits<char> >&) (in /usr/lib64/libstdc++.so.6.0.19)
==32041==    by 0x4009C2: main (val-uninit1.cpp:9)
==32041==  Address 0x4022000 is not stack'd, malloc'd or (recently) free'd
==32041==  Uninitialised value was created by a heap allocation
==32041==    at 0x4C2A7AA: operator new[](unsigned long) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==32041==    by 0x40097F: main (val-uninit1.cpp:7)
```

##### 检测结果解读

这个分析报告中，只是指出第9行使用了未初始化的空间，而没有指出第8行的问题。

1.以类似于memcpy这样的方式访问未初始化的内存不会被检测出来

2.用未初始化的内存来初始化另一个内存，不会被认为是初始化

