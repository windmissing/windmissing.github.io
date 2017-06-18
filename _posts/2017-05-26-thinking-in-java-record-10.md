---
layout: post
title:  "《thinking in JAVA》片断记录 (十)"
category: [读书笔记]
tags: []
---

内部类的对象能访问其外围类对象的所有成员，而不需要任何特殊条件。  
这点与C++的嵌套类的设计非常不同，在C++中只是单纯的名字隐藏机制，与外围对象没有联系，也没有隐含的访问权。  

---

当外围类的对象创建一个内部类的对象时，内部类对象会秘密地捕获一个指向外围类对象的指针。   
当内部类对象需要访问外围类对象的成员时，是通过这个指针访问的。  

---

必须使用外部类的对象来创建内部类的对象。 

```java
public class outter
{
    public class inner{}
    public static void main(String[] args)
    {
        outter o = new outter();
        outter.inner i = dn.new inner();
    }
}
```

---

嵌套类 ！= 内部类
内部类：非静态的内部类
嵌套类：静态的内部类

---

在Outter类的内部创建一个实现Destination接口的内部类Inner，且把它说明为private。  

```java
public interface Destination {
    String readLabel();
}

class Outter {
    private class Inner implements Destination {
        private String label;
        private Inner(String l) {label = l;}
        public String readLabel() {return label;}
    }
    public Destination createInner(String s) {
        return new Inner(s);
    }
}

public class test {
    public static void main(String[] args)
    {
        Outter o = new Outter();
        Destination d = o.createInner("Tasmania");
        d.readLabel();
    }
}
```

效果：  
Inner类只能被Outter类访问，客户端的访问是受到限制的。  
客户端无法知道关于Inner的细节，仅知道它实现了Destination接口。  
客户端只能以接口Destination接口的方法来使用Inner，阻止任何依赖于类型的编码。  

---

```java
public class Outter {
    public void func(boolean b){
        if(b) {
            class Inner {}              //1
            Inner i = new Inner();
        }
        Inner i = new Inner();          //2
    }
}
```