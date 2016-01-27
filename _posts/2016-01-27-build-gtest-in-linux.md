---
layout: post 
title:  "在linux上搭建gtest"
categories: linux
tags: [linux, gtest, UT]
---

#### 1.获取gtest源代码

```
wget https://googletest.googlecode.com/files/gtest-1.7.0.zip
```

#### 2.编译gtest源代码

```
unzip gtest-1.7.0.zip
cd gtest-1.7.0
./configure --prefix=/opt/gtest
make
```
<!-- more -->

#### 3.安装gtest

```
sudo mkdir /opt/gtest /opt/gtest/include /opt/gtest/lib
sudo cp -a include/gtest/ /opt/gtest/include
sudo cp -a lib/.libs/* /opt/gtest/lib
rm /opt/gtest/lib/libgtest.la
rm /opt/gtest/lib/libgtest_main.la
sudo cp -a lib/libgtest.la /opt/gtest/lib
sudo cp -a lib/libgtest_main.la /opt/gtest/lib
vim /etc/ld.so.conf.d/gtest.conf，写入/opt/gtest/lib，执行ldconfig
```

#### 4.准备测试代码

在任意一个位置新建一个代码目录，把以下这几个文件放入

##### main.cpp

```
#include<iostream>
using namespace std;

#include <limits.h>
#include "gtest/gtest.h"

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

```
##### func.cpp

```
#include<iostream>
using namespace std;
#include "func.h"

int func(int a, int b)
{
	return a+b;
}
```

##### func.h

```
int func(int a, int b);
```
##### funcTest.cpp

```
#include<iostream>
using namespace std;

#include <limits.h>
#include "gtest/gtest.h"
#include "func.h"

TEST(AdditionTest,twoValues){
	EXPECT_EQ(3,func(1, 2));
}

```
##### makefile

```
CXX = g++
CXXFLAGS = -g -L/opt/gtest/lib -lgtest -lgtest_main -lpthread
INCS = -I./ -I../../include -I/opt/gtest/include
OBJS = func.o funcTest.o

testAll: $(OBJS)
		$(CXX) $(CXXFLAGS) $(INCS) -o testAll  main.cpp $(OBJS) $(INCS)

.cpp.o:
		$(CXX) $(CXXFLAGS) -c $< -o $@ $(INCS)

clean:
		rm testAll *.o 

```
#### 5.运行效果：

make

./testAll

```
[==========] Running 1 test from 1 test case.
[----------] Global test environment set-up.
[----------] 1 test from AdditionTest
[ RUN      ] AdditionTest.twoValues
[       OK ] AdditionTest.twoValues (0 ms)
[----------] 1 test from AdditionTest (0 ms total)

[----------] Global test environment tear-down
[==========] 1 test from 1 test case ran. (0 ms total)
[  PASSED  ] 1 test.

```


参考资料：

http://www.yolinux.com/TUTORIALS/Cpp-GoogleTest.html#INSTALLATION
