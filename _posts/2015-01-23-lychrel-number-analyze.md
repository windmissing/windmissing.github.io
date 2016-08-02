---
layout: post
title:  "LychrelNumber题目分析"
category: [dojo]
tags: [big number]
---

#### 题目：
Software Competition: Lychrel Number
A Lychrel number is a natural number that cannot form a palindrome through the iterative process of repeatedly reversing its digits and adding the resulting numbers.   
Following numbers can’t form a palindrome after 10000 times of reversing and adding:  
196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887, 978, 986

#### 定义：
这些定义将在下面的说明和伪代码中使用  

|类型	|表示	|定义	|含义	|说明或者举例|
|---|---|---|---|---|
|符号	|《	||数学上的属于符号|数学上的属于符号打不出来，用这个书名号代替|
|符号	|!《	||数学上的不属于符号	|同上|
|符号	|n	|n 《 N	|任意正整数	|0， 1， 2， 3， ……|
|操作	|r(n)	||求逆序数	|r(123) = 321|
|集合	|REVERSE	|REVERSE = { n | r(n) = n }	|如果正整数满足它与它的逆序数的相等的条件，就属于这个逆序数集合	{1, 22, 343, 56765} 《 REVERSE|
|操作	|f(n)	|f(n) = n + r(n)	|把一个数与它的逆序数相加的操作	|f(1) = 2, f(15) = 66|
|操作	|[f(n)]^x	||对一个数作x次f(n)的操作	|[f(n)]^2 = f(f(n)), [f(n)]^0 = n|
|集合	|LYCHREL	|LYCHREL = { n | [f(n)]^x  !《 REVERSE, 且x《N}	|对一个数作x次f(n)的操作后不能成为一个与自己逆序数相等的数，那么就称lychrel数。<br>x的取值越大，REVERSE中的数就越少，在本题中，x至少为10000|{196, 295, 394} 《 LYCHREL|
根据定义知，本题要求LYCHREL中的数，越多越好

#### 算法1：简单暴力
根据定义计算，伪代码如下：

```
bool IS_LYCHRED
     WHILE n !《 REVERSE
          n = f(n)
          COUNT_INCREASE
          IF COUNT_OVERFLOW
               return true
     return false
END IS_LYCHRED
```

##### 存在的问题：
对于普通的计算没有问题，可是本题要求x>=1W，每次计算都有可能有一次进位，循环1W次后的位数有可能是1W位，必须寻找一种方法来存储的使用这么大的数字

#### 算法2：字符串
最容易想到的方法就是字符串存储，把一长串的数字看作是一长串的文本，1W的数字也只是一个有1W个字符的字符串，存储的问题就解决掉了。  
稍加处理也可以像整数一样使用，  
根据上文可知，这个字符串要支持r(n)、+以及==这三种操作，其中只有+稍微复杂一点，伪代码如下：  

```
STRING FUNC_ADD(string A, string B)
     TRAVERSE_EVERY_CHAR(A, B)
          char_a = A(i)
          char_b = B(i)
          int_a = CHANGE_CHAR_TO_INT(char_a)
          int_b = CHANGE_CHAR_TO_INT(char_b)
          int_out(i) = int_a + int_b
          DEAL_WITH_CARRY(int_out)
          char_out(i) = CHANGE_INT_TO_CHAR(int_out(i))
     RETURN string_out
END FUNC_ADD
```

#### 算法3：数组
仔细观察算法2，发现其复杂在于char与int之间的转换。  
我们之所以选择字符串代替整型，是因为字符串能存储超长位。  
字符串的本质是字符组成的数组。它有两方面特性：数组和字符。  
字符串之所以能存储超长位，是利用了它是数组的特性，因为数组的长度可以是很大的。  
而导致我们处理麻烦的却是字符串的字符的特征，因为它不能直接表示一个数字。  

分析到这里，解决方法就很明显了，我们可以把字符串换成另一种数据结构。它即能保持数组的特性，它的每一个元素也能直接表示一个数字，也就是整型数组。  
伪代码如下：  

```
ARRAY FUNC_ADD(ARRAY A, ARRAY B)
     TRAVERSE_EVERY_ELEMENT(A, B)
          out(i) = A(i) + B(i)
          DEAL_WITH_CARRY(out)
     RETURN string_out
END FUNC_ADD
```
走到这一步，已经可以求出LYCHREL了，至于能求多少个，可以从空间限制和时间限制一两方面去考虑。  

##### 空间限制：
主要限制在于数组能开多少，为了节省空间，可以使用byte型的数组。  
程序空间按8M算，每一个数组分配8K的空间也是足够的。  
8KB = 8192B， 一个数组可以支持的数据范围是[0, 10^8192)，也是现在代码支持的计算范围。  
那么一个数做[f(n)]^10000后会有多大呢？根据加法特点，每一次f(n)最多进位1次，一个10^a级别的数，做[f(n)]^10000后，最多是10^(a+4)量级  
因此该算法能求出[0, 10^8188)范围内的LYCHREL  
##### 时间限制：  
在计算时间上，没有做严格统计，但是数字越大，所需要的计算时间越长，几秒钟甚至几分钟才能计算一个数  

分析可知，空间限制几乎可以忽略，而时间限制却是计算LYCHREL的瓶颈。因此后面的算法都是针对提升时间效率所作的改进。  
每一次改进能提升的效率没有做统计，只有理论上的估计。且不同的配置的机器结果也不同。  
最终算法在我本地测试后，求1000以内的LYCHREL数，总时间平均约5秒。  

#### 算法4：多位的数组
算法的主体在算法1中用伪代码表示，假设n是一个len位的十进制数  
根据这个伪代码计算一下时间复杂度，while多少次是一个概率问题，计算比较复杂，因此这里只计算每个while内部的时间复杂度。  
每个while循环可以简单归纳为以下几个步骤  

```
1	求n2 = r(n1)	O(len)
2	判断n1 == n2	O(len)
3	求n3 = r(n1)	O(len)
4	计算n4 = n1 + n3	O(len)
```
每个while循环的复杂度是O(4len)  
线性的时间复杂度看似已经很小了，但还是有优化的空间。  
观察步骤1和3，是相同的操作，可以把n2存储下来，求n3的过程就可以省掉了，不过这不是里的重点。  
观察步骤2和4，其实它们的复杂度并不直接与len相关，而是和数组的长度size相关，因为数组的一项表示大数的一位len==size，所以才看上去是O(len)，实际上是O(size)  
如果数组的一项不只表示一位呢？比如byte可以表示[0,99)，那么len=size*2了，步骤2，4的复杂度为O(size) = O(len/2)  
如果再进一步，用数组的每一项是个long long，可以表示20位，那么复杂度就降到O(len/20)了  
经过这样两种优化，理论上while内部的复杂度可以从O(4len)下降到O(len)了  

#### 算法5：根据推论剪枝
再来关注while循环本身，假设计算一个数要循环x次，那么计算这个数的复杂度是O(x * len)  
每个数对应的x不同，对于非LYCHREL数，x<10000，对于LYCHREL数，x=10000  
假设1000以内的LYCHRE数所占百分比为p，非LYCHREL数平均循环y1次while循环，LYCHREL数平均循环y2次（y2=10000），  
时间复杂度为O(len*(y1*(1-p)+y2*p))，写清楚点就是len * [y1 * (1-p) + y2*p]  
不管对于哪种数，len和p是定值，如果减少y1和y2就是很大的优化了。  

再看集合LYCHREL，它其实是一个封闭集合，  
性质：对于任意x ,y，有y =[f(x)]^a，那么x和y的性质相同，要么都属于LYCHREL，要么都不属于LYCHREL  
推论：对于任意x, y, z，有[f(x)]^a = z，[f(y)]^b = z，那么x、y、z的性质相同，要么都属于LYCHREL，要么都不属于LYCHREL  
这个推论是剪枝的基础。  

这是一种空间换时间的处理，因为空间充足，而时间是严重的瓶颈，因此牺牲一部分空间来存储中间计算结果，当下次再用到以前算过的结果时，直接从记录中去取，从而达到节省时间的目的。  
目前的WHILE循环退出条件是该数是REVERSE，这里再加一个条件，判断这个数是不是被计算过，如果被计算过，就直接从表中读取结果，WHILE就可以结束了  
这里提到保存结果的表，既然有使用，就应该有维护。  
每当一个数，被认定为是或者不是LYCHREL时，再对这个数本身做记录已经没有意义了。要记录的是在判断它的过程中产生的一些中间数的属性。  

根据不太精确的统计，1000以内的数中，大约有90%以上的数，可以通过这种方式提前结束循环。  

#### 算法8：细节优化
还有一些其它的常数级别的优化，效率提升效果几乎可以忽略不计。但是为了实现这些优化而使代码更复杂也是得不偿失的，因此不推荐。  
