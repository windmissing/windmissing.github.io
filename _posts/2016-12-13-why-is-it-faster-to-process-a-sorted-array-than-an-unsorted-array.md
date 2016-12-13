---
layout: post
title:  "为什么有序数组的执行速度快于无序数组？"
category: [stackoverflow经典问答]
tags: [c++, JAVA, 性能, 分支预测]
---

这是一段神奇的c++代码，不知道为什么，将里面的数组data排序，能够使代码的运行速度快了近6倍。  

```c++
#include <algorithm>
#include <ctime>
#include <iostream>

int main()
{
    // Generate data
    const unsigned arraySize = 32768;
    int data[arraySize];

    for (unsigned c = 0; c < arraySize; ++c)
        data[c] = std::rand() % 256;

    // !!! With this, the next loop runs faster
    std::sort(data, data + arraySize);

    // Test
    clock_t start = clock();
    long long sum = 0;

    for (unsigned i = 0; i < 100000; ++i)
    {
        // Primary loop
        for (unsigned c = 0; c < arraySize; ++c)
        {
            if (data[c] >= 128)
                sum += data[c];
        }
    }

    double elapsedTime = static_cast<double>(clock() - start) / CLOCKS_PER_SEC;

    std::cout << elapsedTime << std::endl;
    std::cout << "sum = " << sum << std::endl;
}
```

 - 没有``这一句，代码的运行时间为11.54秒  
 - 加了这个排序语句，代码的运行时间是1.93秒  

<!-- more -->

一开始，我以为是C++语言或者这个编译器比较特殊，于是我又用JAVA做了实验：  

```java
import java.util.Arrays;
import java.util.Random;

public class Main
{
    public static void main(String[] args)
    {
        // Generate data
        int arraySize = 32768;
        int data[] = new int[arraySize];

        Random rnd = new Random(0);
        for (int c = 0; c < arraySize; ++c)
            data[c] = rnd.nextInt() % 256;

        // !!! With this, the next loop runs faster
        Arrays.sort(data);

        // Test
        long start = System.nanoTime();
        long sum = 0;

        for (int i = 0; i < 100000; ++i)
        {
            // Primary loop
            for (int c = 0; c < arraySize; ++c)
            {
                if (data[c] >= 128)
                    sum += data[c];
            }
        }

        System.out.println((System.nanoTime() - start) / 1000000000.0);
        System.out.println("sum = " + sum);
    }
}
```

其运行结果和C++的类似，只是差别没那么极端。  

---

我最初的理解是，排序的过程把data放进了cache，后来觉得这想法很傻，因为数组是刚刚才生成的。那么  
 - 到底发生了什么？
 - 为什么有序数组的执行速度比无序数组快？
 - 这段代码的运行条件是独立的，它不应该和顺序有关。  
 
#### 回答一：你是分支预测失败的受害者
 
##### 什么是分支预测
 
参考这个铁路枢纽：  
![Image by Mecanismo, via Wikimedia Commons. Used under the CC-By-SA 3.0 license.](http://i.stack.imgur.com/muxnt.jpg)  
关于这个问题，假设现在是19世纪（1800s），那时候远距离通信还没有发明。  
你是一个铁路枢纽的操作员，此时听到火车要来了，但你不知道它要往哪个方向去。你需要让火车停下并询问他们要去的方向，然后调整火车轨道。  
然而火车很重，要强大的惯性，要花费很多时间启动和停下。  
有没有更好的方法？你先预测火车的方法！  
 - 如果你猜对了，它继续运行。  
 - 如果你猜错了，火车司机会把火车停下、倒回，并喊你切换方向。然后启动火车开向另一个方向。

**如果你每次都能猜对**，火车就不会停。
**如果你经常猜错**，火车会花费大量的时间停下、倒回、启动。  

---

再说**if条件语句**：从处理器角度看，它是一个分支指令。  
![](http://i.stack.imgur.com/pyfwC.png)  
假设你是处理器，你看到了这个分支指令，但不你知道选择哪个分支。你会怎么做？  
你需要停止执行，等待这条指令执行完成，然后再继续执行正确的指令。  
现代处理器都非常复杂，它们拥有很的管道，需要花很长时间“启动”和“停下”。  
有没有更好的方法？那就是预测分支的方向。  
 - 如果你猜对了，就继续执行  
 - 如果你猜错了，就要清空管道并回退到分支指令处，然后重新开始执行后面的指令。  
 
**如果你每次都猜对**，执行就不会停止。  
**如果你经常猜错**，就要花大量的时间停下、回滚和重新开始。  

---

这就是分支预测。我承认这个类似不是最恰当的，因为火车可以使用一个旗帜来表示它要前往的方向。但在计算机里，处理器直到最后一刻才能知道分支的方向。  
那么你怎么有策略地猜测，才能使“让火车回退然后走另一条线路”的次数尽量地少呢？你可以查看历史！如果火车99% 都是走左边，那么你猜左边。如果想反，则猜另一方向。如果每条路走3次，你也这么猜。。。
**换句话说，你试图找到一个模式并依据它来做推测。**分支预测大概就是这样工作的。   
大部分应用的分支行为都是很有规律的，因此现代分支预测器能达到90%以上的正确率。但是当遇到分支无法预测又找不到其规律时，分支预测器几乎没有用。  
进一步阅读：[“分支预测器”维基百科](http://en.wikipedia.org/wiki/Branch_predictor)  

---

##### 基于以上信息，犯人就是这条if语句

```c++
if (data[c] >= 128)
    sum += data[c];
```

注意到data的值都分布在[0, 255]。当数据排好序，前面大约一半的数据都不会进入if语句内，而后面的数据都会进入if内。  
这对分支预测器来说是很友好的，因为在大多数情况下，分支会延续与上一次相同的方向。即使是一个简单的饱和计数器也能正确地预测分支方向，除了刚换方向之后的几次之外。  

###### 快速可视化

```
T = branch taken
N = branch not taken

data[] = 0, 1, 2, 3, 4, ... 126, 127, 128, 129, 130, ... 250, 251, 252, ...
branch = N  N  N  N  N  ...   N    N    T    T    T  ...   T    T    T  ...

       = NNNNNNNNNNNN ... NNNNNNNTTTTTTTTT ... TTTTTTTTTT  (easy to predict)
```

但是是如果数据是随机的，分支预测器就几乎没有用了，因为它不能预测随机数据。大概分有50%的误判率。（和随机地猜没有区别）

```
data[] = 226, 185, 125, 158, 198, 144, 217, 79, 202, 118,  14, 150, 177, 182, 133, ...
branch =   T,   T,   N,   T,   T,   T,   T,  N,   T,   N,   N,   T,   T,   T,   N  ...

       = TTNTTTTNTNNTTTN ...   (completely random - hard to predict)
```

---

###### 可以做什么？

如果不能通过优化编译器得到期望的指令，你可以试试一些hack方法，牺牲可读性换来性能。  
把  

```c++
if (data[c] >= 128)
    sum += data[c];
```

改成  

```c++
int t = (data[c] - 128) >> 31;
sum += ~t & data[c];
```

这样就消除了分支而替换成了位操作。  
*注意：这个hack语句与原来的if语句不是完全相同的。但在这个例子中，对来自data[]的所有数据都是有用的。*  

###### Benchmarks Core i7 920 @ 3.5 GHz

C++ - Visual Studio 2010 - x64 Release

```
//  Branch - Random
seconds = 11.777

//  Branch - Sorted
seconds = 2.352

//  Branchless - Random
seconds = 2.564

//  Branchless - Sorted
seconds = 2.587
```

Java - Netbeans 7.1.1 JDK 7 - x64

```
//  Branch - Random
seconds = 10.93293813

//  Branch - Sorted
seconds = 5.643797077

//  Branchless - Random
seconds = 3.113581453

//  Branchless - Sorted
seconds = 3.186068823
```

实验结果：  
 - **使用分支：**有序数据与无序数据的差别很大  
 - **使用hach:**有序数据与无序数据之间没差别
 - 在C++的例子中，对于有序数据，使用hack反而比使用分支慢一点  

通常避免在关键环境中使用依赖数据的分支（就像例子中这样）。  

---  

##### 更新

 - GCC 4.6.1在x64上使用`-O3`或`ftree-vectorize`可以产生“条件转移”。因此有序数据和无序数据的执行效果没有差别 - 都很快。  
 - VC++ 2010对于这种分支不能产生“条件转移”，即使是使用`/0x`。  
 - Intel 11编译器做了一些神奇的改进。它对两个循环做了交换，把不可预测的分支移到了循环外面。因此这但对“无法预测”免疫，而且还比VC++和GCC的效果快一倍。换句话说，ICC发挥test-loop的优势，击败了标准。。。
 - 如果你使用Intel编译没有分支的代码，它只是out-right vectorized it.其结果会和使用分支（loop interchange）一样快。  
 这说明即使是现代的成熟的编译器，在优化代码的能力也可以表现出很大的差别。  

 
 [link](http://stackoverflow.com/questions/11227809/why-is-it-faster-to-process-a-sorted-array-than-an-unsorted-array)
