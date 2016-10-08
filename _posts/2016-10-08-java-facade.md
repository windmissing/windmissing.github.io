---
layout: post
title:  "JAVA设计模之外观模式"
category: [设计模式]
tags: []
---

> Facade（外观）模式为子系统中的各类（或结构与方法）提供一个简明一致的界面，隐藏子系统的复杂性，使子系统更加容易使用。

#### 使用facade以前  

假设有五个类：propressor， compiler， assembler， linker, ar。分别负责gcc的五个步骤：预编译、编译、汇编、链接、打包（参考[《linux g++ 链接》](http://windmissing.github.io/compile/2016-07/linux-g++-linking.html)）。    
这五个步骤各自分工完成各自的工作，但它们之前又存在耦合。比如预编译、编译、汇编、链接这四个步骤就是有顺序关系的。它们必须被依次执行，才能得到正确的结果。  
然而使用者并不关心它们之间是怎么合作的，他们只希望使用一个gcc命令就能得到最终的可执行文件。  

<!-- more -->

```java
public class user {
    private target generateTarget(file source)
    {
        propressor cpp;
        compiler cc1;
        assembler as;
        linker ld;
        
        target i = cpp.propressing(source);
        target s = cc1.compilation(i);
        target o = as.assembly(s);
        target out = ld.linking(o);
        return out;
    }
    
    public void main(String[] args) {
        target exe = generateTarget(args[1]);
    }
}
```

有时候，用户只是想生成静态库和动态库。

```java
public class user {
    private target generateStaticLib(file source)
    {
        propressor cpp;
        compiler cc1;
        assembler as;
        ar ar;
        
        target i = cpp.propressing(source);
        target s = cc1.compilation(i);
        target o = as.assembly(s);
        target a = ar.ar(o);
        return a;
    }
    private target generateDynamicLib(file source)
    {
        propressor cpp;
        compiler cc1;
        assembler as;
        linker ld;
        
        target i = cpp.propressing(source);
        target s = cc1.compilation(i);
        target o = as.assembly(s);
        target so = ld.linkingWithPic(o);
        return so;
    }
    
    public void main(String[] args) {
        target lib1 = generateStaticLib(args[1]);
        target lib2 = generateDynamicLib(args[2]);
    }
}
```

#### 引入facade以后

如果你对gcc编译链接的过程有一定的了解，一定能很容易地读懂这几个函数。  
但是并不是每一个写user的人都很清楚这个几步骤的使用方式。  
即使知道这些步骤，要求每个user都写一遍也是件烦琐的事情。  
想像一下，如果没有gcc命令，你想要 通过源代码生成可执行文件或者库，就不得不依次敲下cpp、cc1、as、ld、ar这几个命令去生成。你一定宁愿花几分钟写个脚本，把这几个命令装到一起，统一执行。  
装饰器的作用有点类似于这个脚本。gcc过程中的几个子系统，用法比较复杂，因此把常用的几个种用法封装成接口，以简化用户的使用。而对于特殊情况，也可以直接使用子系统。  

```java
public class gcc {
    public target generateTarget(file source)
    {
        propressor cpp;
        compiler cc1;
        assembler as;
        linker ld;
        
        target i = cpp.propressing(source);
        target s = cc1.compilation(i);
        target o = as.assembly(s);
        target out = ld.linking(o);
        return out;
    }
    public target generateStaticLib(file source)
    {
        propressor cpp;
        compiler cc1;
        assembler as;
        ar ar;
        
        target i = cpp.propressing(source);
        target s = cc1.compilation(i);
        target o = as.assembly(s);
        target a = ar.ar(o);
        return a;
    }
    public target generateDynamicLib(file source)
    {
        propressor cpp;
        compiler cc1;
        assembler as;
        linker ld;
        
        target i = cpp.propressing(source);
        target s = cc1.compilation(i);
        target o = as.assembly(s);
        target so = ld.linkingWithPic(o);
        return so;
    }
}

public class user {
    public static void main(String[] args) { 
        gcc g;
        target out = g.generateTarget(args[1]);
        target lib1 = generateStaticLib(args[2]);
        target lib2 = generateDynamicLib(args[3]);
        target i = cpp.propressing(source);
    }
}
```

#### 用后感

一个外观模式写完了，现在分析一下它起到的作用。  

 - 1.外观gcc为复杂的子系统propressor， compiler， assembler， linker, ar提供了简单的接口。用户不需要理解子系统之间的关系就可以理解gcc提供的功能。  
 - 2.这几个子系统的功能相关，耦合性比较高，子系统之间的关系发生变化的可能性比较大，但所提供功能变化的可能性不大。当子系统之间发生了变化，而功能未变时，只需要修改外观gcc即可，用户代码不需要修改。  
 - 3.对于特殊情况，也可以直接使用子系统，保持了原来的灵活性。  

在有些情况下，它能起到积极的作用，有些情况可能会带来相反的效果。每一种模式都有它的适用场景。  

 - 1.多个类为同一个功能服务，它们之间耦合较高，使用复杂。  
 - 2.多个类之间的关系经常发生变化。  
 - 3.多个类互相配合使用的方法中，有些常用搭配。  
 - 4.用户通常不关心几个类之间的配合。
