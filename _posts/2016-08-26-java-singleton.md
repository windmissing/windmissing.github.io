---
layout: post
title:  "【转】JAVA设计模式之单例模式"
category: [设计模式]
tags: [java, singleton, thread-safety]
---

java中单例模式是一种常见的设计模式，单例模式的写法有好几种，这里主要介绍三种：懒汉式单例、饿汉式单例、登记式单例。  
　　单例模式有以下特点：  
　　1、单例类只能有一个实例。  
　　2、单例类必须自己创建自己的唯一实例。  
　　3、单例类必须给所有其他对象提供这一实例。  
　　单例模式确保某个类只有一个实例，而且自行实例化并向整个系统提供这个实例。在计算机系统中，线程池、缓存、日志对象、对话框、打印机、显卡的驱动程序对象常被设计成单例。这些应用都或多或少具有资源管理器的功能。每台计算机可以有若干个打印机，但只能有一个Printer Spooler，以避免两个打印作业同时输出到打印机中。每台计算机可以有若干通信端口，系统应当集中管理这些通信端口，以避免一个通信端口同时被两个请求同时调用。总之，选择单例模式就是为了避免不一致状态，避免政出多头。  

<!-- more -->

#### 一、懒汉式单例

```java
//懒汉式单例类.在第一次调用的时候实例化自己   
public class Singleton {  
    private Singleton() {}  
    private static Singleton single=null;  
    //静态工厂方法   
    public static Singleton getInstance() {  
         if (single == null) {    
             single = new Singleton();  
         }    
        return single;  
    }  
}  
```
Singleton通过将构造方法限定为private避免了类在外部被实例化，在同一个虚拟机范围内，Singleton的唯一实例只能通过getInstance()方法访问。  
*事实上，通过Java反射机制是能够实例化构造方法为private的类的，那基本上会使所有的Java单例实现失效。此问题在此处不做讨论，姑且掩耳盗铃地认为反射机制不存在。*  

但是以上懒汉式单例的实现没有考虑**线程安全**问题，它是线程不安全的，并发环境下很可能出现多个Singleton实例，要实现线程安全，有以下三种方式，都是对getInstance这个方法改造，保证了懒汉式单例的线程安全，如果你第一次接触单例模式，对线程安全不是很了解，可以先跳过下面这三小条，去看饿汉式单例，等看完后面再回头考虑线程安全的问题：


##### 1、在getInstance方法上加同步
 
```java
public static synchronized Singleton getInstance() {  
    if (single == null) {    
        single = new Singleton();  
    }    
    return single;  
}  
```

##### 2、双重检查锁定

```java
public static Singleton getInstance() {  
    if (singleton == null) {    
        synchronized (Singleton.class) {    
            if (singleton == null) {    
                singleton = new Singleton();   
            }    
        }    
    }    
    return singleton;   
}  
```

##### 3、静态内部类

```java
public class Singleton {    
    private static class LazyHolder {    
        private static final Singleton INSTANCE = new Singleton();    
    }    
    private Singleton (){}    
    public static final Singleton getInstance() {    
        return LazyHolder.INSTANCE;    
    }    
}
```

这种比上面1、2都好一些，既实现了线程安全，又避免了同步带来的性能影响。

#### 二、饿汉式单例

```java
//饿汉式单例类.在类初始化时，已经自行实例化   
public class Singleton1 {  
    private Singleton1() {}  
    private static final Singleton1 single = new Singleton1();  
    //静态工厂方法   
    public static Singleton1 getInstance() {  
        return single;  
    }  
}  
```
饿汉式在类创建的同时就已经创建好一个静态的对象供系统使用，以后不再改变，所以天生是线程安全的。


#### 三、登记式单例(可忽略)

```java
//类似Spring里面的方法，将类名注册，下次从里面直接获取。  
public class Singleton3 {  
    private static Map<String,Singleton3> map = new HashMap<String,Singleton3>();  
    static{  
        Singleton3 single = new Singleton3();  
        map.put(single.getClass().getName(), single);  
    }  
    //保护的默认构造子  
    protected Singleton3(){}  
    //静态工厂方法,返还此类惟一的实例  
    public static Singleton3 getInstance(String name) {  
        if(name == null) {  
            name = Singleton3.class.getName();  
            System.out.println("name == null"+"--->name="+name);  
        }  
        if(map.get(name) == null) {  
            try {  
                map.put(name, (Singleton3) Class.forName(name).newInstance());  
            } catch (InstantiationException e) {  
                e.printStackTrace();  
            } catch (IllegalAccessException e) {  
                e.printStackTrace();  
            } catch (ClassNotFoundException e) {  
                e.printStackTrace();  
            }  
        }  
        return map.get(name);  
    }  
    //一个示意性的商业方法  
    public String about() {      
        return "Hello, I am RegSingleton.";      
    }      
    public static void main(String[] args) {  
        Singleton3 single3 = Singleton3.getInstance(null);  
        System.out.println(single3.about());  
    }  
}  
```
 
登记式单例实际上维护了一组单例类的实例，将这些实例存放在一个Map（登记薄）中，对于已经登记过的实例，则从Map直接返回，对于没有登记的，则先登记，然后返回。   
这里我对登记式单例标记了可忽略，我的理解来说，首先它用的比较少，另外其实内部实现还是用的饿汉式单例，因为其中的static方法块，它的单例在类被装载的时候就被实例化了。  


#### 饿汉式和懒汉式区别

从名字上来说，饿汉和懒汉，  
饿汉就是类一旦加载，就把单例初始化完成，保证getInstance的时候，单例是已经存在的了，  
而懒汉比较懒，只有当调用getInstance的时候，才回去初始化这个单例。  
另外从以下两点再区分以下这两种方式：  

##### 1、线程安全：

饿汉式天生就是线程安全的，可以直接用于多线程而不会出现问题，  
懒汉式本身是非线程安全的，为了实现线程安全有几种写法，分别是上面的1、2、3，这三种实现在资源加载和性能方面有些区别。  

##### 2、资源加载和性能：

饿汉式在类创建的同时就实例化一个静态对象出来，不管之后会不会使用这个单例，都会占据一定的内存，但是相应的，在第一次调用时速度也会更快，因为其资源已经初始化完成，

而懒汉式顾名思义，会延迟加载，在第一次使用该单例的时候才会实例化对象出来，第一次调用时要做初始化，如果要做的工作比较多，性能上会有些延迟，之后就和饿汉式一样了。

至于1、2、3这三种实现又有些区别，

第1种，在方法调用上加了同步，虽然线程安全了，但是每次都要同步，会影响性能，毕竟99%的情况下是不需要同步的，

第2种，在getInstance中做了两次null检查，确保了只有第一次调用单例的时候才会做同步，这样也是线程安全的，同时避免了每次都同步的性能损耗

第3种，利用了classloader的机制来保证初始化instance时只有一个线程，所以也是线程安全的，同时没有性能损耗，所以一般我倾向于使用这一种。



#### 什么是线程安全？

如果你的代码所在的进程中有多个线程在同时运行，而这些线程可能会同时运行这段代码。如果每次运行结果和单线程运行的结果是一样的，而且其他的变量的值也和预期的是一样的，就是线程安全的。

或者说：一个类或者程序所提供的接口对于线程来说是原子操作，或者多个线程之间的切换不会导致该接口的执行结果存在二义性,也就是说我们不用考虑同步的问题，那就是线程安全的。



#### 应用

以下是一个单例类使用的例子，以懒汉式为例，这里为了保证线程安全，使用了双重检查锁定的方式：

```java
public class TestSingleton {  
    String name = null;  
  
        private TestSingleton() {  
    }  
  
    private static volatile TestSingleton instance = null;  
  
    public static TestSingleton getInstance() {  
           if (instance == null) {    
             synchronized (TestSingleton.class) {    
                if (singleton == null) {    
                   singleton = new TestSingleton();   
                }    
             }    
           }   
           return instance;  
    }  
  
    public String getName() {  
        return name;  
    }  
  
    public void setName(String name) {  
        this.name = name;  
    }  
  
    public void printInfo() {  
        System.out.println("the name is " + name);  
    }  
  
}  
```

可以看到里面加了volatile关键字来声明单例对象，既然synchronized已经起到了多线程下原子性、有序性、可见性的作用，为什么还要加volatile呢，原因已经在下面评论中提到，

还有疑问可参考http://www.iteye.com/topic/652440
和http://www.cs.umd.edu/~pugh/java/memoryModel/DoubleCheckedLocking.html


```java
public class TMain {  
    public static void main(String[] args){  
        TestStream ts1 = TestSingleton.getInstance();  
        ts1.setName("jason");  
        TestStream ts2 = TestSingleton.getInstance();  
        ts2.setName("0539");  
          
        ts1.printInfo();  
        ts2.printInfo();  
          
        if(ts1 == ts2){  
            System.out.println("创建的是同一个实例");  
        }else{  
            System.out.println("创建的不是同一个实例");  
        }  
    }  
}  
```

 运行结果：
![](http://img.blog.csdn.net/20140416064753093?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamFzb24wNTM5/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


结论：由结果可以得知单例模式为一个面向对象的应用程序提供了对象惟一的访问点，不管它实现何种功能，整个应用程序都会同享一个实例对象。

对于单例模式的几种实现方式，知道饿汉式和懒汉式的区别，线程安全，资源加载的时机，还有懒汉式为了实现线程安全的3种方式的细微差别。

---

作者：jason0539

博客：http://blog.csdn.net/jason0539/article/details/23297037/（转载请说明出处）
