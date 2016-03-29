---
layout: post
title:  "redis的字符串"
category: 从开源项目学设计
tags: [open source, redis, string]
---

字符串是一种非常基础又非常重要的数据结构，对于redis这样的键-值数据库来说更是如此。

在redis中，所有的键都是字符串。redis的值可以是多种类型，除了字符串以外，还可以是列表、集合等。但字符串作为值也是非常常用的。

在redis中把字符串作为值存储的功能非常强大。除了能存储我们一般意义中的可打印字符串，还可以存储图片、结构体之类的任意的二进制流。

作为数据库，redis也非常关心它的效率。redis会经常对它的键和值作增加、删除、修改等操作，这也要求它所使用的字符串也是非常高效的。

我们知道，C语言已经为字符串提供的丰富的接口供我们直接使用。但redis的字符串没那么简单，它在C语言字符串的基础上增加新了需求。如果由你来为Redis设计字符串，你会怎么做呢？

<!-- more -->

#### 一、需求

##### 1.效率

###### （1）计算字符串的长度

C语言字符串：在C语言中已经有了求字符串长度的函数，即strlen。但它的时间复杂库为O(n)。

redis的需求：求字符串长度是Redis中常见的操作。O(n)的复杂库不足以满足redis对性能的要求，需求改进。

###### （2）字符串追加

C语言字符串：在C语言中一个字符串的长度是固定的，每次想要追加内容都需要重新分配一次内存。

redis的需求：减少重新内存的次数，以提升效率。

#### 2.功能

###### （1）二进制安全

C语言字符串：在C语言中字符串是以`\0`作为结束标志的。这是基于“字符串内容中不会有`\0`”为假设前提的。如果字符串中存储的全部都是字符，这样的假设没有问题。

redis的需求：redis的字符串不仅仅会存储我们一般意义中的可打印字符串，还可以存储图片、结构体之类的任意的二进制流。这就要求redis的字符串不能对其存储的内容作任何假设。

#### 3.方便

###### （1）重用C语言函数

C语言字符串：C语言对字符串提供了大量的接口，因此使用C语言字符串非常方便。

redis的需求：C语言字符串的功能显然不能满足redis的需求，因此势必会创建一个供redis使用的新的数据结构。新的数据结构必然对应新的算法。但新的算法大部分与C语言已经提供的接口相似。如何才能在新的数据结构上尽可能地重用C语言的接口是一个问题。

###### （2）兼容`\0`
redis要同时兼容二进制流和字符串，这两者的区别在于结束方式。二进制流以长度标识内容的结束，而字符串使用的是\0。

若sds仍以\0为结束，那么二进制流文件会出错。
若sds不以\0为结束，那么对字符串使用C语言函数时会出错。

如何能以优雅的方式兼容好这两种字符串也是一个问题。

#### redis的字符串

##### redis字符串的组成

redis字符串的组成   | 头header  | 字符串本身    | 结束符 
---                 |---        | ---           | ---
结构类型            | sdshdr    | sds           | char
结构体定义          | 以sdshdr为例：<br>`struct __attribute__((__packed__)) sdshdr64 {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`uint64_t len; /* used */`<br>&nbsp;&nbsp;&nbsp;&nbsp;`uint64_t alloc; /* excluding the header and null terminator */`<br>&nbsp;&nbsp;&nbsp;&nbsp;`unsigned char flags; /* 3 lsb of type, 5 unused bits */`<br>&nbsp;&nbsp;&nbsp;&nbsp;`char buf[];`<br>`};`    | typedef char *sds; |
结构存储的内容      | 字符串的内存占用信息，如字符串本身所占用的空间及实际使用的空间，以及其它管理信息 | 字符串实际需要存储的内容 | `\0`
大小                | 固定大小，sizeof(sdshdr)  | 由头部分的alloc指定 | 1

##### sds的创建

仍以sdshdr64为例，以下是简化后的代码：

```c
sds sdsnewlen(const void *init, size_t initlen) {
    void *sh;
    sds s;

    ...
    
    int hdrlen = sizeof(struct sdshdr64);
    sh = s_malloc(hdrlen+initlen+1);
    if (!init)
        memset(sh, 0, hdrlen+initlen+1);
    if (sh == NULL) return NULL;
    s = (char*)sh+hdrlen;

    ...
    
    struct sdshdr64 *sh = (void*)((s)-(sizeof(struct sdshdr64)));
    sh->len = initlen;
    sh->alloc = initlen;

    if (initlen && init)
        memcpy(s, init, initlen);
    s[initlen] = '\0';
    return s;
}
```

虽然创建一个redis字符串时一次为三个部分都申请了空间了，但实际上返回并使用的是sds那一部分。

##### 求长度

```c
static inline size_t sdslen(const sds s) {
    return ((struct sdshdr64 *)(s-(sizeof(struct sdshdr64))))->len;
}
```
这是一种取巧的方法。因为已知redis字符串的三个部分是按顺序放在一起的。那么已经sds的地址和header的大小，就可以向上推出header的地址，从而算出header->alloc。

##### 追加

为了避免每次追加都要重新分配空间，Redis采用预分配的策略。即每次因为追加而分配内存时，实际追加的内存比需要追加的内存大一些。

```c
sds sdsMakeRoomFor(sds s, size_t addlen) {
    void *sh, *newsh;
    size_t avail = sdsavail(s);
    size_t len, newlen;
    int hdrlen;

    /* Return ASAP if there is enough space left. */
    if (avail >= addlen) return s;

    len = sdslen(s);
    sh = (char*)s-sizeof(struct sdshdr64);
    newlen = (len+addlen);
    if (newlen < SDS_MAX_PREALLOC)
        newlen *= 2;
    else
        newlen += SDS_MAX_PREALLOC;

    hdrlen = sizeof(struct sdshdr64);

    newsh = s_realloc(sh, hdrlen+newlen+1);
    if (newsh == NULL) return NULL;
    s = (char*)newsh+hdrlen;

    。。。
    
    sdssetalloc(s, newlen);
    return s;
}
```

##### 二进制安全

在sdshdr结构体中加入len字段后，不仅可以快速地求字符串的长度，还顺便解决了二进制安全的问题。因为有了len字段来启记录字符串的长度，就不用假设字符串以\0结尾了。

##### 重用C语言函数

虽然redis的字符串由三部分组成一个整体，但它交给用户的只是中间的那一部分。中间的sds实际就是char *。所有对char *操作的函数也都可以用于sds。

但是sds还有一个header，有些字符串操作会对header的内容有影响，只有这一部分需求重写。

例如strcat

```c
sds sdscatlen(sds s, const void *t, size_t len) {
    size_t curlen = sdslen(s);

    s = sdsMakeRoomFor(s,len);
    if (s == NULL) return NULL;
    memcpy(s+curlen, t, len);
    sdssetlen(s, curlen+len);
    s[curlen+len] = '\0';
    return s;
}

sds sdscat(sds s, const char *t) {
    return sdscatlen(s, t, strlen(t));
}
```

##### 兼容`\0`

redis的做法是仍旧在每个字符的最后，也就是buf[len]的位置加上一个\0。这样可以照顾到字符串。

但是redis又不把这个\0算到redis的长度里面去，这样又可以照顾到二进流。

这就是redis字符串第三部分存在的意义。
