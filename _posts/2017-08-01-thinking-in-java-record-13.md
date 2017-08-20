---
layout: post
title:  "《thinking in JAVA》片断记录 (十三)"
category: [读书笔记]
tags: []
---

JAVA中的String对象是不可变的。（*C++没有不可变对象的概念*）。  
优点：使代码易于编写与阅读  
缺点：一定的效率问题。  

---

由于String对象不可变，String对象的拼接会导致大量的中间对象。  
JVM对此做了优化，通过自动引入StringBuilder的方法优化了这个过程。  
但是对于大量字符串拼接的情况，仍建议显式地使用StringBuilder。  

---

```java
public class InfiniteRecursion {
    public String toString() {
        return "InfiniteRecursion address: " + this + "\n";
    }
}
```
这样写会导致异常。  
这个函数的原意是输出对象的地址。  
但由于this与字符串相加，由于String对`operator +`的重载，这里的this变成了this.toString()，于是出现了无限递归。  
这里this应该改为`super.toString()`

---

格式化输出：

```java
printf();
System.out.format();
System.out.printf();
Formatter f = new Formatter(System.out); f.format();
```

通过相当简洁的语法，Formatter提供了对空格与对齐的强大控制能力。  

---

数字0转换这boolean时为true。  

---

在其它语言中，'\\'表示“我想要在正则表达式中插入一个普通的（字面上的）反斜线，请不要给它任何特殊的意义”  
在JAVA中，'\\'的意思是“我要插入一个正则表达式的反斜线，所以其后的字符具有特殊的意义”  
如果要插入一个普通的反斜线，要这样写'\\\\'  

---

一些正则表达式相关的对象及其接口

##### String对象

原字符串.split(正则表达式字符串)：将字符串从正则表达式匹配的地方切开，返回Array<String>  
原字符串.matches(正则表达式字符串)：判断原字符串是否符号正则表达式，返回boolean  
原字符串.replaceAll(正则表达式字符串，替换后的字符串)  

##### Pattern对象

Pattern p = Pattern.compile(正则表达式字符串); ：生成一个正则表达式对象  
p.split(原字符串)：将原字符串断开成字符串对象数组  

##### Matcher对象

Matcher m = p.matcher(原字符串);:生成一个正则表达式匹配结果对象  
m.find() ：搜索匹配结果  
m.reset（原字符串）:就用于另一个字符串  

---

#### 扫描输出

##### 普通方法

```java
BufferedReader input = new BufferedReader(new StringReader("aaa\nbbb"));
String content = input.readLine();
```
StringReader对象 -> BufferedReader对象 -> readLine  

##### scanner

```java
Scanner stdin = new Scanner(SimpleRead.input);
String content = std.next();
```

任何类型的输入对象 -> Scanner对象 -> next/nextInt/nextDouble/nextLine/...  

Scanner的Next是根据定界符（空白字符）对输入进行分词的。  
可以通过正则表达式指定定界符。  

##### scanner结合正则表达式

```java
Scanner scanner = new Scanner(原字符串)
while(scanner.hasNext(正则表达式字符串))
{
    scanner.next(正则表达式字符串); //找到下一个匹配的部分
    MatchResult match = scanner.match(); //获得获取的结果
}
```

这里Scanner仍然根据定界符进行分词。  
如果正则表达式中包含定界符，将永远匹配失败。  