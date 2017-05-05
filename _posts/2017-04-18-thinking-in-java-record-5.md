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
2. 检测对象是否被释放，举例：  

```java
class Book {
    boolean checkedOut = false;
    Book(boolean checkOut)
    {
        checkedOut = checkOut;
    }
    void checkIn()
    {
        checkedOut = false;
    }
    protected void finalize()
    {
        if(checkedOut)
        {
            System.out.println( "Error: checked out" );
            // Normally, you'll also do this:
            // super.finalize();
        }
    }
}

public class TerminationCondition {
    public static void main( String[] args )
    {
        Book novelBook = new Book( true );
        // Proper cleanup:
        novelBook.checkIn();
        // Drop the reference, forget to clean up:
        new Book( true );
        // Force gargabe collection & finalization:
        System.gc();
    }
}
```

所有的Book对象在被当作垃圾回收前都应该被签入，但由于程序员的错误，有一本书未被签入，要是没有finalize()来验证终结条件，将很难发现这种缺陷。

---

#### JVM的GC

对于其它语言，堆上分配对象的代码十分高昂。  
对于JAVA，由于GC的作用，使得堆分配的速度可以与其它语言栈分配的速度相媲美。
 - **为什么空间释放会影响到空间分配的速度？**
因为GC在回收空间的同时，还会使堆中的对象紧凑排列。  
 - **垃圾收集方式：引用计数法？**
引用计数法由于效率较低，且不能处理循环引用的问题，因此并没有实际应用于JVM中。

---

#### GC的工作方法

##### 主要流程：  
1. 根据算法1追踪到所有的对象，剩下的就是要回收的空间  
2. 根据算法2决定使算法3还是算法4回收空间
3. 算法3/算法4

##### 算法1：追踪“活”的对象
对于任何“活”的对象，一定能最终追溯到其存活在堆栈或静态存储区之中的引用。这个引用链条可以穿过数个对象层次。  
1.从堆栈和静态存储区开始  
2.遍历所有引用，找到所有“活”的对象  
3.对于发现的每个引用，进一步追踪它所引用的对象，如此反复
##### 算法2：自适应技术

JVM会监视系统状态，如果所有对象都稳定，垃圾回收器的效率降低的话，就切换到算法4。  
同样，JVM会跟踪算法4的效果，要是堆空间出现很多碎片，就会切换到算法3.  

##### 算法3：停止-复制

1.暂停程序的运行  
2.把所有活着的对象从当前堆复制到另一个堆  
3.搬的同时，修正指向它的引用

优点：新堆保持紧凑排列  
缺点：1.需要两个堆，空间2.稳定后垃圾少，大量的复制是浪费的  
改进：内存分配以“块”为单位，小的对象被复制并整理，大的对象不会被复制

##### 算法4：标记-清扫

找到活的对象时仅作标记  
标志完成才开始清理  
未标记的对象会被释放  

优点：不需要复制  
缺点：产生内存碎片  

---

#### 初始化

在不同情况下使用未初始化的变量会有不同的结果。  
对于未初始化的局部变量，使用时会报错，因为JAVA认为**未初始化的局部变量更有可能是程序员的疏忽，所以采用默认值反而会掩盖这种失误**。  
对于未初始化的类成员变量，系统会给个默认值0。  

---

#### 自动初始化

在定义类成员变量的地方为其赋值

```java
public class initValue {
    boolean bool = true;
    char ch = 'x';
    int i; //没有指定初值则初始化为0
}
```

##### 各种初始化的顺序
静态成员的初始化  
自动初始化（以定义为顺序）（即使散布于方法定义之间）。  
构造函数初始化  

---

#### 初始化块

```java
public class Spoon {
    static int i;
    //静态块
    static {
        i = 47;
    }
    //非静态块
    int j;
    {
        j = 48;
        print("j is inited");
    }
}

初始化块也在构造函数之前执行
```

---

#### 数组初始化

 - 声明的两种方式

```java
int[] a;  //a只是个引用
int a2[];
```

编译器不允许指定数组的大小。  
要给数组创建空间，必须写初始化表达式。  

```java
int [] a = new int[5];
int [] a = new int[](1, 3, 4, 5,); //最后一个,可写可不写
```

---

#### 可变参数

##### 声明带可变参数的函数

```java
void func1(Object[] args) //以前的写法
void func2(Object[]... args)
void func3(int required, String... trailing) //当具有可选的尾随参数时，这一特性会很有用

//重载
void func(Character... args)
void func(Integer... args)
```

##### 使用带可变参数的函数

```java
//常规调用方法
func1(new Object[]{"1", "2", "3"});
func2(new Object[]{"1", "2", "3"});
//自动转型为数组
func3(1, "1");
func3(0);
//当没有参数时，使用重载的可变参函数会有歧义
func();
```

**只在重载方法的一个版本上使用可变参数列表，或者压根不用它。**  
[自动包装机制](http://blog.csdn.net/caster_saber/article/details/50950466)