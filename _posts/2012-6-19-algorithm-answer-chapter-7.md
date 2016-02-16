---
layout: post
title: "第7章 快速排序"
category: 算法导论
tags: [算法, 算法导论, 快速排序]
---

# 一、概念

快速排序是基于分治模式的，选择一个数作为主元，经过一遍扫描，所有小于主元的数放在主元的左边，大于主元的数放在主元的右边，这样就划分成了两组数据。然后对两组数分别进行快排。

快排的运行时间与划分是否对称有关，关键是如何选择主元。

最坏情况下，时间复杂度是O(n^2)，最好情况下，时间是O(nlgn)

<!-- more -->

# 二、程序

[头文件](https://github.com/windmissing/exerciseForAlgorithmSecond/blob/master/include/chapter7/quickSort.h)

[算法过程](https://github.com/windmissing/exerciseForAlgorithmSecond/blob/master/src/chapter7/quickSort.cpp)

[测试](https://github.com/windmissing/exerciseForAlgorithmSecond/blob/master/tst/chapter7/quickSortTest.cpp)


# 三、练习

### 7.1 快速排序的描述

##### 7.1-1

A = {13 19 9 5 12 8 7 4 21 2 6 11}

==> A = {9 5 8 7 4 2 6 11 21 13 19 12}

==> A = {5 4 2 6 9 8 7 11 21 13 19 12}

==> A = {2 4 5 6 9 8 7 11 21 13 19 12}

==> A = {2 4 5 6 9 8 7 11 21 13 19 12}

==> A = {2 4 5 6 7 8 9 11 21 13 19 12}

==> A = {2 4 5 6 7 8 9 11 21 13 19 12}

==> A = {2 4 5 6 7 8 9 11 12 13 19 21}

==> A = {2 4 5 6 7 8 9 11 12 13 19 21}

==> A = {2 4 5 6 7 8 9 11 12 13 19 21}

##### 7.1-2

返回r

##### 7.1-2

修改PARTITION(A, p, r)，增加对A[i]==x时的处理。对于A[i]==x的数据，一半放在x左边，一半放在x右边

[算法过程](https://github.com/windmissing/exerciseForAlgorithmSecond/blob/master/src/chapter7/Exercise7_1_2.cpp)

[测试](https://github.com/windmissing/exerciseForAlgorithmSecond/blob/master/tst/chapter7/Exercise7_1_2Test.cpp)

##### 7.1-3

PARTITION()的具体过程如下：

(1)x<-A[r]，O(1)

(2)遍历数组，O(n)

(3)exchange，O(1)

因此运行时间为O(n)

#####7.1-4

修改PARTITION(A, p, r)，把L4改为do if A[j] >= x
  

### 7.2 快速排序的性能

##### 7.2-1

见《算法导论》7.4.1。

我的方法：

```
T(n)   = T(n-1) + O(n)
T(n-1) = T(n-2) + O(n-1)
  ……   = ……   + ……
T(2)   = T(1)   + O(2)
------------------------
T(n)   = T(1)   + O(n) + O(n-1) + …… + O(2)
= O(n^2)
```
##### 7.2-2

O(n^2)

##### 7.2-3

当数组A包含不同元素且按降序排序时，每次划分会划分成n-1个元素和1个元素这两个区域，即最坏情况。因此时间为O(n^2)

##### 7.2-4

基本有序的数列用快排效率较低

##### 7.2-5

若第一层的元素个数是n，那么会划分成n(1-a)个元素和na个元素这两个区域。0<a<=1/2 ==> na<=n(1-a)，因此只考虑n(1-a)。第t层元素个数为na^(t-1)。当na^(t-1)=1时划分结束。解得t=-lgn/lg(1-a)+1，大约是-lgn/lg(1-a)。

##### 7.2-6

可参考http://blog.163.com/kevinlee_2010/blog/static/16982082020112585946451/，
不过我没看懂
  
  

### 7.3 快速排序的随机化版本

##### 7.3-1

随机化不是为了提高最坏情况的性能，而是使最坏情况尽量少出现

##### 7.3-2

最坏情况下，n个元素每次都划分成n-1和1个，1个不用再划分，所以O(n)次

最好情况下，每次从中间划分，递推式N(n)=1+2*N(n/2)=O(n)
  

### 7.4 快速排序的分析

##### 7.4-1

没有找到关于这几个符号的定义

##### 7.4-2

见《算法导论》P88最佳情况划分

##### 7.4-3

令f(q) = q^2 + (n-q-1)^2
       = 2q^2 + 2(1-n)q + (n-1)^2

这是一个关于q的抛物线，且开口向上。因此q的取值离对称轴越远，f(q)的值就越大。

对称轴为q = -b/2a = (n-1)/2

当q=0或q=n-1时取得最大值

##### 7.4-4

见《算法导论》P7.4.2

##### 7.4-5

[算法过程](https://github.com/windmissing/exerciseForAlgorithmSecond/blob/master/src/chapter7/Exercise7_4_5.cpp)

# 四、思考题

### 7-1 Hoare划分的正确性

a）  

A = {13 19 9 5 12 8 7 4 11 2 6 21}    

==> A = {6 19 9 5 12 8 7 4 11 2 13 21}    

==> A = {6 2 9 5 12 8 7 4 11 19 13 21}    

==> A = {4 2 9 5 12 8 7 6 11 19 13 21}    

==> A = {4 2 5 9 12 8 7 6 11 19 13 21}    

==> A = {2 4 5 9 12 8 7 6 11 19 13 21}    

==> A = {2 4 5 6 12 8 7 9 11 19 13 21}    

==> A = {2 4 5 6 7 8 12 9 11 19 13 21}    

==> A = {2 4 5 6 7 8 9 12 11 19 13 21}    

==> A = {2 4 5 6 7 8 9 12 11 13 19 21} 
 
b)自己写的，很乱，凑合看吧

主要证明以下几点：

（1）do repeat j<-j-1 until A[j]<=x

这个repeat中，第一次执行L6时p<=j<=r，最后一次执行L6时p<=j<=r

证明：

1.第一次执行L6时p<=j<=r。为了区分，j'=j-1，L6中的j用j'表示。

第一次进入while循环时，j=r+1，j'=r，满足p<=j<=r。

若不是第一次进入while循环，j<=r且j>p。因为如果j=p，在上一次while循环中L9的if不能通过，已经return了。因此p<=j<r-1，满足p<=j<=r。

2.最后一次执行L6时p<=j<=r，即要证明在A[p..r]中存在j'满足j'<=j且A[j]<=x

若第一次进入while循环，j'=p满足条件

若不是第一次进入while循环，在上一次while循环中交换过去的那个元素满足条件

（2）do repeat i<i+1 until A[i]>=x

这个repeat中，第一次执行L8时p<=i<=r，最后一次执行L8时p<=i<=r

证明：证明方法与（1）类似

c)根据b可知返回值p<=j<=r，这里只需证明j!=r

若A[r]>x,L5和L6的循环不会在j=r时停止，因此返回值j!=r

若A[r]<=x，只有在第一次进入while循环时，L5和L6的循环在j=r时停止。因为是第一次进入while循环，A[i]=A[p]=x，L7和L8的循环会在i=p时停止。显然会第二次进入while循环，此时j<r，因此返回值j!=r

d)题目写错了，应该是A[p..j]中的每个元素都小于或等于A[j+1..r]中的每个元素

结束时，A[p..i-1]中的元素都小于x，A[j+1..r]中的元素都大于x，命题得证

e)

```c++
int Hoare_Partition(int *A, int p, int r)    
{    
    int x = A[p], i = p - 1, j = r + 1;    
    while(true)    
    {    
        do{j--;}    
        while(A[j] > x);    
        do{i++;}    
        while(A[i] < x);    
        if(i < j)    
            swap(A[i], A[j]);    
        else return j;    
        Print(A, 12);    
    }    
}    
void Hoare_QuickSort(int  *A, int p, int r)    
{    
    if(p < r)    
    {    
        int q = Hoare_Partition(A, p, r);    
        Hoare_QuickSort(A, p, q-1);    
        Hoare_QuickSort(A, q+1, r);    
    }    
} 
```

### 7-2 对快速排序算法的另一种分析 

a)

```
               1 + 2 + …… + n       n + 1
    E[Xi] = -------------------- = -------
	                n                 2
```
                    
b)后面几题表示完全看不懂


### 7-3 Stooge排序

```c++
void Stooge_Sort(int *A, int i, int j)  
{  
    if(A[i] > A[j])  
        swap(A[i], A[j]);  
    if(i + 1 >= j)  
        return;  
    k = (j - i + 1) / 3;  
    Stooge_Sort(A, i, j-k);  
    Stooge_Sort(A, i+k, j);  
    Stooge_Sort(A, i, j-k);  
}
```
以下内容转http://blog.csdn.net/zhanglei8893

a）对于数组A[i...j]，STOOGE-SORT算法将这个数组划分成均等的3份，分别用A, B, C表示。

第6-8步类似于冒泡排序的思想。它进行了两趟：

第一趟的第6-7步将最大的1/3部分交换到C

第二趟的第8步将除C外的最大的1/3部分交换到B

剩余的1/3位于A，这样的话整个数组A[i...j]就有序了。

b）比较容易写出STOOGE-SORT最坏情况下的运行时间的递归式

T(n) = 2T(2n/3)+Θ(1)

由主定律可以求得T(n)=n^2.71

c）各种排序算法在最坏情况下的运行时间分别为：

插入排序、快速排序：Θ(n^2)

堆排序、合并排序：Θ(nlgn)

相比于经典的排序算法，STOOGE-SORT算法具有非常差的性能，这几位终生教授只能说是浪得虚名了^_^
  

### 7-4 快速排序中的堆栈深度

a)

```c++
void QuickSort2(int *A, int p, int r)
{
	while(p < r)
	{
		int q = Partition(A, int p, r);
		QuickSort2(A, p, q-1);
		p = q + 1;
	}
}
```

b) A = {1, 2, 3, 4, 5, 6}
c)

```c++
void QuickSort3(int *A, int p, int r)
{
	while(p < r)
	{
		int q = Partition(A, int p, r);
		if(r-q > q-p)
		{
			QuickSort3(A, p, q-1);
			p = q + 1;
		}
		else
		{
			QuickSort3(A, q+1, r);
			r = q - 1;
		}
	}
}
```

### 7-5 “三数取中”划分

a)n个数任意取三个不同的数的取法共有C(3,n)种

若要x=A'[i]，必须在A'[1..i-1]中取一个数，在A'[i+1..n]中取一个数取法共(i-1)*(n-i)

```
      (i-1) * (n-i)     6 * (i-1) * (n-i)
pi = --------------- = -------------------
         C(3,n)         n * (n-1) * (n-2)
```

b)在一般实现中，pi=1/n。

n->正无穷时，极限为0。

在这种实现中，当i=(n+1)/2时，

```
      3(n-1)
pi = ---------，当n->正无穷时，极限为0
      2n(n-2)
```

c)遇到这种数学题就没办法了，哎，以前数学没学好

d)不会求

[附自己写的程序](https://github.com/windmissing/exerciseForAlgorithmSecond/blob/master/src/chapter7/Exercise7_5.cpp)


### 7-6 对区间的模糊排序

见[算法导论7-6对区间的模糊排序](http://blog.csdn.net/mishifangxiangdefeng/article/details/7681109)
