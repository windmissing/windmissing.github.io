---
layout: post
title:  "网新恒天2011.9.21招聘会笔试题"
category: 面试笔试
tags: [笔试]
---

1、下列哪种数据类型不能用作switch的表达式变量（）

A、byte         B、char         C、long       D、enum

> 答：C

> switch括号中的表达式只能是整形、字符型或者是枚举型表达式；限制4个字节，所以比int大的不行；只能是byte, char, short, int或者是相应的枚举类型！

<!-- more -->

2、在图采用邻接表存储时，求最小生成树的 Prim 算法的时间复杂度为（）。

A、 O(n)     B、O(n+e)        C、 O(n2)       D、O(n3)

> 答：C

> 《算法导论》上说：“使用二叉堆优化Prim算法的时间复杂度为O((V + E) log(V)) = O(E log(V))，对于稀疏图相对于朴素算法的优化是巨大的，然而100行左右的二叉堆优化Prim相对于40行左右的并查集优化Kruskal，无论是在效率上，还是编程复杂度上并不具备多大的优势。另外，我们还可以用更高级的堆来进一步优化时间界，比如使用斐波那契堆优化后的时间界为O(E + V log(V))，但编程复杂度也会变得更高。”

> 时间复杂度，比B高，比C低，我认为选C比较好


3、在图采用邻接矩阵存储时，求最小生成树的 Prim 算法的时间复杂度为（）。

A、 O(n)   B、 O(n+e)        C、 O(n2)       D、O(n3)

> 答：C


4、树的后根遍历序列等同于该树对应的二叉树的（）.

A、先序序列         B、中序序列       C、后序序列

> 答：B


5、“Abc汉字”的长度为（）

A、5          B、6        C、7      D、8

> 答：D


6、下面程序的输出结果为（）

```c++
unsigned int a=1;  
cout<<a*-2<<endl;  
```

A、-4      B、4       C、4294967294         D、4294967295

> 答：C

> 考查的是unsigned int和int在一起混合运算，int转化为unsigned int

> -2的补码就是2^32-2，即是4294967294 ，乘以1的结果还是这个数字。


7、下面程序的输出结果为（）

```c++
void fn(int *b)  
{  
    cout<<(*b)++;  
}  
int main(void)  
{  
    int a=7;  
    fn(&a);  
    cout<<a;  
    return 0;  
} 
```
A、77      B、78       C、89        D、undefined

> 答：B


8、下面程序的输出结果为（）

```c++
#pragma pack(8)   
union A  
{  
    char a[13];  
    int b;  
};  
int main(void)  
{  
    cout<<sizeof(A)<<endl;  
    return 0;  
}   
```
A、4      B、8       C、16        D、12

> 答：C

> 计算类的大小见类的sizeof


9、下面程序的输出结果为（）

```c++
class A  
{  
public:  
    A(int a)  
    {  
        printf("%d ",a);  
    }  
};  
A a(1);  
int main(void)  
{  
    printf("main ");  
    A c(2);  
    static A b(3);  
    return 0;  
}  
```
A、1  main 2 3      B、1  main 3 2       C、main 1  2 3         D、main  1 3 2 

> 答：A


10、下面程序的输出结果为（）

```c++
struct Test  
{  
    unsigned short int a:5;  
    unsigned short int b:5;  
    unsigned short int c:6;  
};  
int main(void)  
{  
    Test test;  
    test.a=16;  
    test.b=4;  
    test.c=0;  
    int i=*(short*)&test;  
    printf("%d\n",i);  
    return 0;  
}  
```
A、6         B、144            C、5            D、95

> 答：B

> 1、程序中':'的作用，如 unsigned short int a:5;表示变量a占了5个bit的空间，这样的话结构体所占的变量空间为5+5+6，暂且表示为000000|00000|00000，对应c|b|a

> 2、在主程序中对结构体初始化a=16,b=4,c=0,转换为二进制放到上面的空间，000000|00100|10000同样对应a|b|c

> 3、后面一句int i=*(short*)&test;取结构体test的地址空间，就是上面的000000|00100|10000，转换成short型，也就是144


11、n个结点的线索二叉树上含有的线索数为（）

A、2n      B、n－l       C、n＋l         D、n

> 答：C


12、（）的遍历仍需要栈的支持.

A、前序线索树     B、中序线索树      C、后序线索树 

> 答：C


13、二叉树在线索后，仍不能有效求解的问题是（）。

A、前（先）序线索二叉树中求前（先）序后继

B、中序线索二叉树中求中序后继

C、中序线索二叉树中求中序前驱

D、后序线索二叉树中求后序后继

> 答：D


14、求解最短路径的Floyd算法的时间复杂度为（）。

A、O（n）    B、 O（n+c）     C、O（n*n）     D、O（n*n*n）

> 答：D


*部分答案参考http://blog.csdn.net/hackbuteer1/article/details/6802113*
