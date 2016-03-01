---
layout: post
title:  "valgrind memcheck 读/写内存越界"
category: linux
tags: [valgrind, memcheck]
---

关于valgrind memcheck请阅读[《valgrind memcheck使用方法及效果》](/linux/2016-02/valgrind-memcheck.html)

在这里，我列举了三种读/写内存越界的情况

- 试访问栈内数组越界

- 访问堆中数组越界

- 函数传参导致数组长度退化

<!-- more -->

#### 一、试访问栈内数组越界

##### 测试代码

```c++
#include <iostream>
using namespace std;

int main()
{
    int s[5] = {1, 2, 3, 4, 5};
    cout<<s[5]<<endl;
    return 0;
}
```

##### 编译及运行

```
g++ -g -o outrange1 val-outrange1.cpp
valgrind --track-origins=yes ./outrange1
```

##### 检测结果

```
==7850== Use of uninitialised value of size 8
==7850==    at 0x4EBF4F3: ??? (in /usr/lib64/libstdc++.so.6.0.19)
==7850==    by 0x4EBF635: std::ostreambuf_iterator<char, std::char_traits<char> > std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::_M_insert_int<long>(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib64/libstdc++.so.6.0.19)
==7850==    by 0x4EBFBEC: std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::do_put(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib64/libstdc++.so.6.0.19)
==7850==    by 0x4ECBF7D: std::ostream& std::ostream::_M_insert<long>(long) (in /usr/lib64/libstdc++.so.6.0.19)
==7850==    by 0x400879: main (val-outrange1.cpp:7)
```

##### 检测结果解读

1.可以检测出访问栈中数组越界的问题

2.访问栈中数组越界会被当作是访问未初始化空间来处理

#### 二、访问堆中数组越界

###### 测试代码

```c++
#include <iostream>
using namespace std;
#include "string.h"

int main()
{
    int *s = new int[5];
    memset(s, 0, sizeof(s));
    cout<<s[5]<<endl;
    delete []s;
    return 0;
}
```

###### 检测结果

```
==8221== Invalid read of size 4
==8221==    at 0x400954: main (val-outrange1.cpp:9)
==8221==  Address 0x5a15054 is 0 bytes after a block of size 20 alloc'd
==8221==    at 0x4C2A7AA: operator new[](unsigned long) (in /usr/lib64/valgrind/vgpreload_memcheck-amd64-linux.so)
==8221==    by 0x400931: main (val-outrange1.cpp:7)
```

###### 检测结果解读

可以检测访问堆中数组越界的问题

能够指出错误代码的位置

#### 三、函数传参导致数组长度退化

```c++
#include <iostream>
using namespace std;

void print(int *s, int id)
{
    cout<<s[id]<<endl;
}
int main()
{
    int s[5] = {1, 2, 3, 4, 5};
    print(s, 5);
    return 0;
}
```

###### 检测结果

```
==8342== Use of uninitialised value of size 8
==8342==    at 0x4EBF4F3: ??? (in /usr/lib64/libstdc++.so.6.0.19)
==8342==    by 0x4EBF635: std::ostreambuf_iterator<char, std::char_traits<char> > std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::_M_insert_int<long>(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib64/libstdc++.so.6.0.19)
==8342==    by 0x4EBFBEC: std::num_put<char, std::ostreambuf_iterator<char, std::char_traits<char> > >::do_put(std::ostreambuf_iterator<char, std::char_traits<char> >, std::ios_base&, char, long) const (in /usr/lib64/libstdc++.so.6.0.19)
==8342==    by 0x4ECBF7D: std::ostream& std::ostream::_M_insert<long>(long) (in /usr/lib64/libstdc++.so.6.0.19)
==8342==    by 0x400870: print(int*, int) (val-outrange1.cpp:6)
==8342==    by 0x4008BB: main (val-outrange1.cpp:11)
==8342==  Uninitialised value was created by a stack allocation
==8342==    at 0x400880: main (val-outrange1.cpp:9)
```

###### 检测结果解读

堆中数组因为参数传递而退化为指针后，不能检测出访问越界的问题
