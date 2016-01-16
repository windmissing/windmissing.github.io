---
layout: post
title: "linux中内存泄漏的检测（二）定制化的malloc/free"
category: linux
tags: [linux, memory leak]
---

[《linux中内存泄漏的检测（一）最简单的方法》](memory-leak-in-linux-1.html)介绍了最简单的内存泄漏检测方法，这种方法虽然简单，却有很多现实的问题，导致它不能用于实际的生产中。

直接使用这种方法肯定是不现实的，因为：

（1）把整个工程里所有调用malloc/free的地方都改成my_malloc/my_free，代码改动很大。

（2）通常动态库和静态库的代码是没有权限修改的。

今天就来解决这个问题，动态地决定让程序使用自己的还是系统的内存管理接口。

<!-- more -->

#### wrap选项

不希望修改产品代码，那么用于申请/释放内存的接口还是malloc/free。
又想在接口中增加计数的功能，就要再实现一套用于申请/释放内存的接口。新接口不能和malloc/free重名。这太矛盾了。

如果能自己定制一个malloc/free就好了。

幸好GCC也想到了这一点，给我们提供了wrap选项。
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

#### 定制自己的malloc/free
看上去这个wrap功能正好符合我们的需求，我们来看看具体是怎么使用。

（1）wrap既可以用于变量符号，也可以用于函数符号，但我们现在要用的只是函数符号，准确地说，就是malloc和free这两个符号。

（2）这是一个在链接过程中起作用的选项，在链接选项中加上`-Wl,--wrap,malloc -Wl,--wrap,free`
（3）`__wrap_malloc/__wrap_free`函数实现

```c
void * __wrap_malloc(int size)
{
    malloc_count++;
    return __real_malloc(size);
}

void __wrap_free(void *ptr)
{
    free_count++;
    __real_free(ptr);
}
```
（4）测试

```c
int main()
{
    malloc_count = 0;
    free_count = 0;
    int *p1 = (int *)malloc(sizeof(int));
    int *p2 = (int *)malloc(sizeof(int));
    free( p1);
    if(malloc_count != free_count)
        printf("memory leak!\n");
    return 0;
}
```
（5）运行
```
gcc -o test main.c -Wl,--wrap,malloc -Wl,--wrap,free
```

#### 分析 

 - 优点

（1）使用方便 — 不需要改产品代码，只需要修改编译选项即可完成。

（2）范围全面 — wrap是个链接选项，对所有通过__wrap_malloc和__wrap_free链接到一起的文件都起作用，不论是静态库还是动态库。

 - 缺点

（1）该方法要求运行结束时对运行中产生的打印分析才能知道结果。

（2）只对C语言适用，不能应用于C++

（3）只能检测是否泄漏，却没有具体信息，比如泄漏了多少空间

（4）不能说明是哪一行代码引起了泄漏

#### 改进

检测方法有了初步改进，但不能满足与此，预知下一步改进，且看下回分解

[linux中内存泄漏的检测（一）最简单的方法](memory-leak-in-linux-1.html)

[linux中内存泄漏的检测（二）定制化的malloc/free](memory-leak-in-linux-2.html)

[linux中内存泄漏的检测（三）定制化的new/delete](memory-leak-in-linux-3.html)

[linux中内存泄漏的检测（四）记录泄漏的大小](memory-leak-in-linux-4.html)

[linux中内存泄漏的检测（五）定制内存泄漏的代码](memory-leak-in-linux-5.html)