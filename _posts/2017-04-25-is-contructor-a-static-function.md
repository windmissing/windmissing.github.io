---
layout: post
title:  "构造器是静态方法吗？"
category: [编程语言]
tags: []
---

原文链接：[link](http://rednaxelafx.iteye.com/blog/652719)  

《thinking in JAVA》P96中写道：  
> 构造器实际上也是静态方法  

对此百思不解，于是从网上找到了这篇文章。

<!-- more -->

---

如题。这个问题的答案要看你心中的“静态”指代了什么。 

看到最近在论坛的一帖：  
**renpeng301 写道**  
> 如果不熟悉JVM指令，看到这些东西确实难以理解···很直观的看到Test默认为继承自Object这个JAVA中的超级父类，当new Test()的时候，调用Test的默认构造器，构造器其实就是一个特殊的静态的方法（这样说应该没错吧？）

想起以前[在JavaEye问答频道见过的类似问题](http://www.iteye.com/problems/14154)，看来这“静态”有一定迷惑性的。   

在Java中，“static”可以有多个意思，对方法而言，至少包括下面两点：   
1、Java语言中的“static”关键字用于修饰方法时，表示“静态方法”，与“实例方法”相对。   
2、在讨论方法的具体调用目标时，一个方法调用到底能否在运行前就确定一个固定的目标，是则可以进行“静态绑定”（static binding），否则需要做“运行时绑定”（runtime binding）。这与“static”关键字不是一回事。   

=========================================================================== 

先看看第一点，Java语言中的“static“关键字修饰的方法。  

根据Java语言规范第三版，静态方法的规定为：  
**Java Language Specification, 3rd 写道**  
> **8.4.3.2 static Methods**   
>
> <font color=red>A method that is declared static is called a class method. A class method is always invoked without reference to a particular object.</font> An attempt to reference the current object using the keyword this or the keyword super or to reference the type parameters of any surrounding declaration in the body of a class method results in a compile-time error. It is a compile-time error for a static method to be declared abstract. 
> 
> <font color=blue>A method that is not declared static is called an instance method, and sometimes called a non-static method. An instance method is always invoked with respect to an object, which becomes the current object to which the keywords this and super refer during execution of the method body.</font>

注意到规范中关于“静态方法”（红色部分）与“实例方法”（蓝色部分）的定义。两者的关键差异在于：“静态方法”的调用总是不指定某个对象实例为“接收者”，而“实例方法”则总是要以某个对象实例为“接收者”（receiver）。 

用Java的语法来演示。 

调用实例方法，从调用者的一方看，“接收者”就是`.`之前的那个变量所引用的对象： 

```java
receiver.instanceMethod(args)  
```
如果一个被被调用者与调用者在同一个类中，那么receiver可以省略不写，由编译器判断出“接收者”是this。 

从被调用的一方看，“接收者”就是在方法中可以使用的伪变量“this”： 

```java
public void instanceMethod(Object... args) {  
    // 注意“this”  
    System.out.println(this);  
}  
```
“this”并没有出现在参数列表中，但它实际上做作为实例方法调用的一个隐式参数传入的。 

调用静态方法则不需要、无法指定也无法使用receiver。Java语言中的类不是对象，所以通过ClassName.aStaticMethod(args)的方式去调用一个静态方法时，`.`前面的并不是receiver。如果`.`前面的是一个指向某对象实例的变量而`.`后面指定的是一个静态方法，则实际上那个变量并没有被作为receiver使用，只是个调用变量的类型上声明的静态方法的语法糖而已。也就是说： 

```java
aVariable.aStaticMethod(args)  
```
实际上等效于： 

```java
TheClass.aStaticMethod(args)  
```

关于“this”的规定，Java语言规范第三版如是说：  
**Java Language Specification, 3rd 写道**  
> **15.8.3 this**  
> 
> <font color=red>The keyword this may be used only in the body of an instance method, instance initializer or constructor, or in the initializer of an instance variable of a class.<font> If it appears anywhere else, a compile-time error occurs.  

很明显，在构造器中是可以访问“this”的；实例初始化器与实例变量初始化器在编译时会与构造器一起被收集到`<init>()`方法中，它们也都可以访问“this”。所以从Java语言的“static”关键字的角度看，实例构造器不是“静态方法”。 

------------------------------------------- 

Java语言通常是编译为class文件后由Java虚拟机来运行的。在Java虚拟机规范第二版中，有这样的描述：  
**Java virtual machine specification, 2nd 写道**  
> 3.6.1 Local Variables  
>
> Each frame (§3.6) contains an array of variables known as its local variables. The length of the local variable array of a frame is determined at compile time and supplied in the binary representation of a class or interface along with the code for the method associated with the frame (§4.7.3). 
A single local variable can hold a value of type boolean, byte, char, short, int, float, reference, or returnAddress. A pair of local variables can hold a value of type long or double. 
>  
> Local variables are addressed by indexing. The index of the first local variable is zero. An integer is be considered to be an index into the local variable array if and only if that integer is between zero and one less than the size of the local variable array. 
>  
> A value of type long or type double occupies two consecutive local variables. Such a value may only be addressed using the lesser index. For example, a value of type double stored in the local variable array at index n actually occupies the local variables with indices n and n +1; however, the local variable at index n +1 cannot be loaded from. It can be stored into. However, doing so invalidates the contents of local variable n. 
>  
> The Java virtual machine does not require n to be even. In intuitive terms, values of types double and long need not be 64-bit aligned in the local variables array. Implementors are free to decide the appropriate way to represent such values using the two local variables reserved for the value. 
>  
> The Java virtual machine uses local variables to pass parameters on method invocation. <font color=red>On class method invocation any parameters are passed in consecutive local variables starting from local variable 0.</font> <font color=blue>On instance method invocation, local variable 0 is always used to pass a reference to the object on which the instance method is being invoked (**this** in the Java programming language). Any parameters are subsequently passed in consecutive local variables starting from local variable 1.<font>

3.6.1小节的最后一段提到了“类方法”（“静态方法”）与“实例方法”在概念中的JVM上的区别：在调用类方法时，所有参数按顺序存放于被调用方法的局部变量区中的连续区域，从局部变量0开始；在调用实例方法时，局部变量0用于存放传入的该方法所属的对象实例（Java语言中的“this”），所有参数从局部变量1开始存放在局部变量区的连续区域中。  
从效果上看，这就等于在调用实例方法时总是把“this”作为第一个参数传入被调用方法。  

在关于方法描述符的部分：  
**Java virtual machine specification, 2nd 写道** 
> **4.3.3 Method Descriptors **  
>  
> （... 省略） 
>  
> For example, the method descriptor for the method 
>  
>     Object mymethod(int i, double d, Thread t) 
> is 
>     (IDLjava/lang/Thread;)Ljava/lang/Object; 
> Note that internal forms of the fully qualified names of Thread and Object are used in the method descriptor.   
> The method descriptor for mymethod is the same whether mymethod is a class or an instance method. <font color=blue>Although an instance method is passed this, a reference to the current class instance, in addition to its intended parameters, that fact is not reflected in the method descriptor.<font> <font color=red>(A reference to this is not passed to a class method.)<font> <font color=blue>The reference to this is passed implicitly by the method invocation instructions of the Java virtual machine used to invoke instance methods.<font>

这里提到一个方法无论是类方法还是实例方法，其方法描述符都是一样的。“this”作为调用实例方法的一个隐式参数，不会反映在方法描述符中。 

=========================================================================== 

接下来看第二点，关于调用方法时选择具体的目标的“static”。 

Java语言中，虚方法可以通过覆写（override）的方式来实现[子类型多态（subtype polymorphism）](http://en.wikipedia.org/wiki/Subtype_polymorphism)。Java语言支持三种多态，除了子类型多态外还有通过方法重载支持的[ad-hoc多态（ad-hoc polymorphism）](http://en.wikipedia.org/wiki/Parametric_polymorphism#Parametric_polymorphism)与通过泛型支持的[参数化多态（parametric polymorphism）](http://en.wikipedia.org/wiki/Parametric_polymorphism#Parametric_polymorphism)。在面向对象编程的语境里“多态”一般指子类型多态，下面提到“多态”一词也特定指子类型多态。  

Java语言中非虚方法可以通过“静态绑定”（static binding）或者叫“早绑定”（early binding）来选择实际的调用目标——因为无法覆写，无法产生多态的效果，于是可能的调用目标总是固定的一个。虚方法则一般需要等到运行时根据“接收者”的具体类型来选择到底要调用哪个版本的方法，这个过程称为“运行时绑定”（runtime binding）或者叫“迟绑定”（late-binding）。   
不过Java的虚方法的迟绑定具体如何去选择目标是写死在语言规范与JVM的实现中的，用户无法干涉选择的过程。这使得Java提供的迟绑定缺乏自由度。在Java 7开始提供[invokedynamic](http://jcp.org/en/jsr/detail?id=292)支持后，用户可以自行编写程序来控制迟绑定的过程，开始对选择调用目标拥有完整的控制权。   

Java语言中，哪些方法是虚方法呢？静态方法全部都是非虚的，而实例方法则看情况。  
Java语言规范第三版说明了哪些实例方法不是虚方法：  
**Java Language Specification, 3rd 写道**  
> **8.4.3.3 final Methods**   
> 
> <font color=red>A method can be declared **final** to prevent subclasses from overriding or hiding it.</font> It is a compile-time error to attempt to override or hide a final method.   
<font color=red>A private method and all methods declared immediately within a final class (§8.1.1.2) behave as if they are final, since it is impossible to override them.</font>  
>
>It is a compile-time error for a final method to be declared abstract.  

行为如同“final”的方法都无法覆写，也就无法进行子类型多态；声明为final或private的方法都被属于这类。所以除了静态方法之外，声明为final或者private的实例方法也是非虚方法。其它实例方法都是虚方法。 

Java语言规范接着提到：  
**Java Language Specification, 3rd 写道**  
> **8.4.3.3 final Methods**  
> 
> （... 省略） 
> 
> <font color=red>At run time, a machine-code generator or optimizer can "inline" the body of a final method, replacing an invocation of the method with the code in its body.</font> The inlining process must preserve the semantics of the method invocation. In particular, if the target of an instance method invocation is null, then a NullPointerException must be thrown even if the method is inlined. The compiler must ensure that the exception will be thrown at the correct point, so that the actual arguments to the method will be seen to have been evaluated in the correct order prior to the method invocation.   
> 
> Consider the example: 
> 
> ```java
> final class Point {  
>     int x, y;  
>     void move(int dx, int dy) { x += dx; y += dy; }  
> }  
> class Test {  
>     public static void main(String[] args) {  
>         Point[] p = new Point[100];  
>         for (int i = 0; i < p.length; i++) {  
>             p[i] = new Point();  
>             p[i].move(i, p.length-1-i);  
>         }  
>     }  
> }  
>  
> Here, inlining the method move of class Point in method main would transform the for loop to the form:   
>
>```java
>for (int i = 0; i < p.length; i++) {  
>    p[i] = new Point();  
>    Point pi = p[i];  
>    int j = p.length-1-i;  
>    pi.x += i;  
>    pi.y += j;  
>}  
>  
> The loop might then be subject to further optimizations. 
>  
> Such inlining cannot be done at compile time unless it can be guaranteed that Test and Point will always be recompiled together, so that whenever Point-and specifically its move method-changes, the code for Test.main will also be updated.

这里提到“final方法”可以在运行时得到内联。其实所有非虚方法在运行时都可以安全的被内联。  
一个保守的JVM可以如上述说明一样在运行时对非虚方法的调用进行内联优化；而一个激进优化的JVM则可以更进一步，将源码中声明为虚方法、但在运行时的某个时间点可以证明（例如通过[类层次分析（CHA）](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.117.2420&rep=rep1&type=pdf)）该方法只有一个可能的调用目标时，仍然可以将调用目标内联到调用者中。现在在桌面与服务器上的主流高性能JVM，如Oracle (Sun) HotSpot、IBM J9、Oracle (BEA) JRockit等，都会做这样的激进优化。因此在开发桌面与服务器端Java程序时没有必要为了提到性能而特意将方法声明为final的。  

关于HotSpot VM对final的处理，可以参考[HotSpot Internals wiki的Virtual Calls一篇](http://wikis.sun.com/display/HotSpotInternals/VirtualCalls)：  

> It is legal for an invokevirtual bytecode to refer to a final method. A final method need not have a vtable slot allocated. This means that, after linking, an invokevirtual bytecode might in fact collapse into the equivalent of an invokestatic bytecode. The interpreter is prepared to do this.


Anders Hejlsberg曾经在多个场合提到虚方法是无法内联的（例如这个Artima的访谈）；确实CLR是无法内联任何虚方法调用，但那只是CLR的实现限制而已。这点上高性能JVM比CLR要先进（且复杂）许多。   

来看看Oracle/Sun JDK里的HotSpot VM是如何做初步的是否能静态绑定的：   

```c++
bool methodOopDesc::can_be_statically_bound() const {  
  if (is_final_method())  return true;  
  return vtable_index() == nonvirtual_vtable_index;  
}  
```
也就是，如果某个Java方法是final的或者不是虚方法的话，它就可以做静态绑定。 

------------------------------------------- 

Java虚拟机规范第二版中定义了四种不同的字节码指令来处理Java程序中不同种类的方法的调用。包括，  
- invokestatic - 用于调用类（静态）方法   
- invokespecial - 用于调用实例方法，特化于super方法调用、private方法调用与构造器调用  
- invokevirtual - 用于调用一般实例方法（包括声明为final但不为private的实例方法）  
- invokeinterface - 用于调用接口方法   

其中，invokestatic与invokespecial调用的目标必然是可以静态绑定的，因为它们都无法参与子类型多态；invokevirtual与invokeinterface的则一般需要做运行时绑定，JVM实现可以有选择的根据final或实际运行时类层次或类型反馈等信息试图进行静态绑定。 

=========================================================================== 

那么Java中的实例构造器是不是“静态方法”呢？从Java语言规范中给出的“静态方法”的定义来看，答案是“否”——首先从Java语言规范对“方法”的定义来说，构造器根本不是“方法”；其次，实例构造器有一个隐式参数，“this”，在实例构造器中可以访问“this”，可以通过“this”访问到正在初始化的对象实例的所有实例成员。      

Java语言规范中关于构造器的说明中提到：  
**Java Language Specification, 3rd 写道**  
> 8.8 Constructor Declarations  
>  
> A constructor is used in the creation of an object that is an instance of a class: 
>  
> （... 省略） 
>  
> <font color=red>Constructor declarations are not members. They are never inherited and therefore are not subject to hiding or overriding.<red>  

实例构造器无法被隐藏或覆写，不参与多态，因而可以做静态绑定。从这个意义上可以认为实例构造器是“静态”的，但这种用法与Java语言定义的“静态方法”是两码事。  

另外需要注意的是，Java语言中，实例构造器只能在new表达式（或别的构造器）中被调用，不能通过方法调用表达式来调用。new表达式作为一个整体保证了对象的创建与初始化是打包在一起进行的，不能分开进行；但实例构造器只负责对象初始化的部分，“创建对象”的部分是由new表达式本身保证的。  

举个例子，下面的Java代码 

```java
public class ConstructorDemo {  
    private int value;  
      
    public ConstructorDemo(int i, Object o) {  
        this.value = i;  
    }  
      
    public static void main(String[] args) {  
        ConstructorDemo demo = new ConstructorDemo(2, args);  
    }  
}  
```
被编译为class文件后，实例构造器与main()方法的内容分别为： 

```java
public ConstructorDemo(int, java.lang.Object);  
  Code:  
   Stack=2, Locals=3, Args_size=3  
   0:   aload_0  
   1:   invokespecial   #1; //Method java/lang/Object."<init>":()V  
   4:   aload_0  
   5:   iload_1  
   6:   putfield        #2; //Field value:I  
   9:   return  
  
public static void main(java.lang.String[]);  
  Code:  
   Stack=4, Locals=2, Args_size=1  
   0:   new     #3; //class ConstructorDemo  
   3:   dup  
   4:   iconst_2  
   5:   aload_0  
   6:   invokespecial   #4; //Method "<init>":(ILjava/lang/Object;)V  
   9:   astore_1  
   10:  return  
```

先从main()方法开始看。  
第一条指令是new，用于创建出ConstructorDemo类型的一个空对象，执行过后指向该对象的引用被压到操作数栈上。  
第二条指令是dup，将操作数栈顶的值复制一份压回到栈顶；其中dup出来的一份用于作为隐式参数传到实例构造器里去（对应后面的invokespecial），原本的一份用于保存到局部变量去（对应后面的astore_1）。  
第三条指令是iconst_2，将常量2压到操作数栈上，作为ConstructorDemo实例构造器的第一个显式参数。  
第四条指令是aload_0，将main()方法的参数args作为ConstructorDemo实例构造器的第二个显式参数。  
第五条指令是invokespecial，调用ConstructorDemo实例构造器。再次留意，前面已经传了三个参数，分别是new出来的实例的引用、常量2与main()的参数args。该指令执行过后，操作数栈顶就只剩下dup前通过new得到的引用。  
第6条指令是astore_1，将操作数栈顶的引用保存到局部变量1中。执行过后操作数栈空了。  
最后一条指令是return，结束main()方法的执行并返回。  

然后从ConstructorDemo的实例构造器来看。  
第一条指令是aload_0，将第一个参数（不管是隐式还是显式参数）压到操作数栈上。从main()的调用序列可以看到第一个参数是刚new出来的对象实例的引用，对这个构造器来说也就是“this”。   
第二条指令是invokespecial，调用Object的实例构造器。前一条指令的“this”就是这个调用的参数。执行过后操作数栈就空了。  
第三条指令又是aload_0，再次将“this”压到操作数栈上。  
第四条指令是iload_1，将第二个参数压到操作数栈上，也就是i。  
第五条指令是putfield，将i赋值给this.value。执行过后操作数栈又空了。  
最后一条指令是return，结束该实例构造器的执行并返回。   

这个例子的注意点在于：  
1、Java的实例构造器只负责初始化，不负责创建对象；Java虚拟机的字节码指令的设计也反映了这一点，有一个new指令专门用于创建对象实例，而调用实例构造器则使用invokespecial指令。  
2、“this”是作为实例构造器的第一个实际参数传入的。   



相信能区分“静态方法”与“静态绑定”中的“静态”之后，就不会再将Java中的实例构造器看作是“静态方法”了。  