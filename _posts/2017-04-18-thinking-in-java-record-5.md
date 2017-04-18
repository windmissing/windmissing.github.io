---
layout: post
title:  "《thinking in JAVA》片断记录 (五)"
category: [读书笔记]
tags: []
---

#### this关键字

如果为this添加了参数列表，那么就有了不同的含义。这将产生对符合此参数列表的某个构造器的明确调用。

```java
public class Flower {
    Flower(String ss)
    {
        // ...
    }
    Flower(int petals)
    {
        // ...
    }
    Flower(String s, int petals)
    {
        this(petals);  //Flower(int petals)
//!        this(s);    //只能调用一个
    }
}
```

---

#### 析构函数与finalize()方法

**不要把finalize()方法当作析构函数来用**

||析构函数|finalize()|
|---|---|---|
|是否一定执行|对象销毁时一定执行|对象销毁不一定是通过GC，只有通过GC销毁对象时执行|
|执行哪些内容|包含内存回收及其它销毁前要做的清理工作|只用于回收内存，不包括其它（业务相关）|
|什么时候执行|对象生成周期结束时|GC要销毁对象时，GC不会在对象生命周期结束时马上销毁它|

```
C++（析构函数） = JAVA（内存清理 + 其它清理）  
                        |           |
                        GC完成    明确调用某个JAVA方法，不能使用finalize()
```

既然finalize()只能用于清理内存，而清理内存又由GC自动完成，那么**finalize()有什么用？**  

1. 以非JAVA方式申请的内存，需要通过finalize()来释放  
2. 检测对象是否被释放  

