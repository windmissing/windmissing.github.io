---
layout: post
title: "linux中内存泄漏的检测（二）"
category: linux
tags: [linux, memory leak]
---

上文介绍了最简单的内存泄漏检测方法，这种方法虽然简单，却有很多现实的问题，导致它不能用于实际的生产中。

这些问题中，我认为最不能接受的就是“使用不方便”。
写一个带计数的申请和释放接口是简单的，但要把所有申请和释放的地方都改成自己定义的接口，那就相当麻烦了。
更麻烦的是，为了检测内存泄漏而使用这些接口，在产品交付时却又要改回来。
也许可以用宏来解决，仍免不了让代码变得难看。

今天就来解决这个问题，动态地决定让程序使用自己的还是系统的内存管理接口。

<!-- more -->

#### 二、定制的malloc/free

不希望修改产品代码，那么用于申请/释放内存的接口还是malloc/free。
又想在接口中增加计数的功能，就要再实现一套用于申请/释放内存的接口。新接口不能和malloc/free重名。这太矛盾了。

如果能自己定制一个malloc/free就好了。

幸好GCC也想到了这一点，给我们提供了这样的编译链接选项来实现这样的功能，那就是wrap。
这是man ld得到的说明：

 > --wrap=symbol

 > Use a wrapper function for symbol.  Any undefined reference to symbol will be resolved to `__wrap_symbol`.  Any undefined reference to `__real_symbol` will be resolved to symbol.

 > This can be used to provide a wrapper for a system function.  The wrapper function should be called `__wrap_symbol`.  If it wishes to call the system function, it should call `__real_symbol`.

 > Here is a trivial example:

>
```c
void * __wrap_malloc (size_t c)
{
    printf ("malloc called with %zu\n", c);
    return __real_malloc (c);
}
```
 > If you link other code with this file using --wrap malloc, then all calls to `malloc` will call the function `__wrap_malloc` instead.  The call to `__real_malloc` in `__wrap_malloc` will call the real "malloc" function.

 > You may wish to provide a `__real_malloc` function as well, so that links without the --wrap option will succeed.  If you do this, you should not put the definition of `__real_malloc` in the same file as `__wrap_malloc`; if you do, the assembler may resolve the call before the linker has a chance to wrap it to `malloc`.

我把这一大坨英文解释一下（英语好的同学可以跳过）：

wrapper在英文中是包装的意思，也就是在已经存在无法修改的符号（通常是系统符号）的外面加一层定制化的包装，这样我们既可以重用原来的代码，又可以加入新的功能。

当你对一个名为`symbol`符号使用wrap功能时，任何要用到`symbol`的地方实际使用的是`__wrap_symbol`符号

考虑到你的`__wrap_symbol`只是为了对`symbol`加一层包装，有可能还是要用到真正的`symbol`，只需要要你的`__wrap_symbol`里调用`__real_symbol`即可，因为任何用到`__real_symbol`的地方实际使用的是真正的`symbol`

也就是说，当你对一个名为`symbol`符号使用wrap功能时，会得到这样的效果：

（1）当你调用`symbol`时实际调用的是`__wrap_symbol`

（2）当你调用`__real_symbol`时实际调用的是`symbol`

（3）可以把对`symbol`包装的操作当在`__wrap_symbol`中，然后再让`__wrap_symbol`调用`__real_wrap`，就相当于在使用`symbol`之前做了自己订制的附加功能。

看上去这个wrap功能正好符合我们的需求，我们来看看具体是怎么使用。

（1）wrap既可以用于变量符号，也可以用于函数符号，但我们现在要用的只是函数符号，准确地说，就是malloc和free这两个符号。

（2）这是一个在链接过程中起作用的选项，它的使用方法是在链接选项中加上`-Wl,--wrap,malloc -Wl,--wrap,free`
（3）实现`__wrap_malloc`函数（`__wrap_free`类似）

```c
void * __wrap_malloc(int size)
{
    count++;
    return __real_malloc(size);
}

void __wrap_free(void *ptr)
{
    count--;
    __real_free(ptr);
}
```
（4）测试

```c
int main()
{
    count = 0;
    int *p1 = (int *)malloc(sizeof(int));
    int *p2 = (int *)malloc(sizeof(int));
    free( p1);
    if(count != 0)
        printf("memory leak!\n");
    return 0;
}
```
（5）运行
```
gcc -o test main.c -Wl,--wrap,malloc -Wl,--wrap,free
```

本文仍将从方便性、全面性、准确性这几个方面来分析这种方法。

- 方便性：

|功能|是否支持|说明
|:---:|:---:|:---:| 
|运行时检查|否|该方法要求运行结束时对运行中产生的打印分析才能知道结果。
|修改是否方便|是|wrap函数实现非常简单，且只需要实现一次，对所有参与链接的文件都有效
|使用是否方便|是|要关掉这一功能，只需要将这个链接选项去掉即可

 - 全面性：

|功能|是否支持|说明
|:---:|:---:|:---:| 
|C接口是否可以统一处理|否|C的每个接口都需要分别写包装函数
|C++接口是否可以统一处理|否|C++的接口却无法处理
|动态库与静态库的内存泄漏是否可以检测到|是|wrap是个链接选项，对所有通过wrap与`__wrap_malloc`和`__wrap_free`链接到一起的文件都起作用，不管是.o、.a或者.so

- 准确性：

|功能|是否支持|说明
|:---:|:---:|:---:| 
|是否会有检测不到的情况|否|这一方法只能用于C，而在C中不会出现申请和释放的大小不一样的情况，所以只要次数一样就不会有问题了
|是否可以定位到行|否|
|是否可以确定泄漏空间的大小|否|

检测方法有了初步改进，但不能满足与此，预知下一步改进，且看下回分解
