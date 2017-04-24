---
layout: post
title:  "《thinking in JAVA》片断记录 (四)"
category: [读书笔记]
tags: []
---

#### foreach

foreach语法，不必创建int变量去对由访问项构成的序列进行计数，foreach自动产生每一项。

<!-- more -->
---

#### goto

JAVA编译器生成它自己的“汇编代码”，这个代码运行在JAVA虚拟机上，而不是直接运行在CPU硬件上。  
JAVA没有goto，但有一个类似的机制：标签。

---

### 标签

**标签起作用的唯一地方是刚好在迭代语句之前。**  
**在迭代之前设置标签的唯一理由是：有多层迭代存在，想从多层迭代中break或continue。**  
书上的原话讲的有点奇怪。以下是我的理解：  
*break和continue只是结束或继续“当前”循环，当两层及以上的循环嵌套时这两个关键字的使用就会比较繁琐，标签是为了解决这方面的不足。*  
举例：  

```java
label1:
outer-iteration{
    inner-interation {
        //...
        break; // (1)
        //...
        continue; //(2)
        //...
        continue label1; // (3)
        //...
        break label1; // (4)
    }
}
```

（1）结束内部循环，继续外部循环
（2）继续内部循环
（3）转到label1，继续后面的循环
（4）转到label1，结束后面的循环