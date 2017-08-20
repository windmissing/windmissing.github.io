---
layout: post
title:  "《thinking in JAVA》片断记录 (十四)"
category: [读书笔记]
tags: []
---

RTTI：运行时类信息

---

#### 为什么需要RTTI

通常，希望大部分代码尽可能少地了解对象的具体类型。  
特殊情况下，能够知道某个泛化引用的确切类型，能可以使用最简单的方法解决问题。  
使用RTTI，可以查询引用所指向的对象的确切类型，然后选择或剔除特例。  

---

JAVA通过Class类的对象来获取运行时类信息的。  
每个类所在的.class文件中都会自动生成一个class对象。  
当要使用某个类时，JVM会先加载该类中的Class对象到内存。  
获取该类的class对象后，可以通过这个对象获取该类的信息。  

---

获取类的class对象的方法有

|方法|作用|副作用|
|---|---|---|
|class.forName("类名")|获取类的class对象|如果该类没有被加载，会加载该类|
|对象.getClass()|获取类的class对象|无|
|类名.class|获取类的class对象的引用|无|
|类名.TYPE|获取类的class对象的引用|仅限于部分内置类型|

---

||||
|---|---|---|---|
|通过的class引用这样写|Class intClass = int.class;|可以重新引用其它任意类型的Class对象|
|也可以使用泛化引用|Class<Integer> intClass = int.class;|不能重新引用其它类型，可以是Integer.class|
|或者使用放松限制的泛化引用|Class<? extends Number> intClass = int.class;|可以引用double.class, number.class等class对象|

Class泛型语法的**唯一**作用是：提供编译期类型检查。  

---

static final int staticFianal = 47;  
这是个编译器常量，不需要加载类就可以使用。  

static final int staticFinal2 = ClassInitialization.rand.nextInt(1000);
static int staticNonFinal = 74;
这种情况不是编译器常量，需要先加载类再使用。  

---

在C++中，类型转换并不使用RTTI，只是简单地告诉编译器将这个对象当作另一个类型对待。  
在JAVA中，向下类型转换，必须是显式地，并编译器会简单这个检查是否合理。  

---

判断一个对象是否是这个类（及其子类）  
 - 方法一：
   
```java
对象 instanceof 类名
例如：
if(pet instanceof Pet) {...}
if(pet instanceof Dog) {...}
```

 - 方法二：

```java
类的class对象.isInstace(对象)
例如：
if(Pet.class.isInstance(pet)) {...}
if(Dog.class.isInstance(pet)) {...}
```

 - 方法三：

```java
通过对象获取class对象1
通过类获取class对象2
class对象2.isAssignableFrom(class对象1)
例如：
Class<?> type = pet.getClass();
class<?> baseType1 = Pet.class;
class<?> baseType2 = Dog.class();
if(baseType1.isAssignableFrom(type)) {...}
if(baseType2.isAssignableFrom(type)) {...}
```

---

RTTI要求类型信息在编译时必须已知。  
反射可以在运行时获取类型信息。  
1. 编译时无法获取对象所属的类  
2.在跨网络的远程平台上创建和运行对象的能力。  

RTTI和反射之间的真正区别在于：
RTTI，编译器在编译时打开和检查.class文件  
反射，在运行时打开和检查.class文件  

---

代理模式：将额外的操作从“实际”对象中分离到不同的地方。  
从没有使用额外操作转为使用这些操作，或者反过来。  

---

空对象，可以接受传递给它的所代表的对象的消息，但是将返回表示为实际上并不存在任何“真实”对象的值。  

---

RTTI使得损失了多态机制的重要价值。  
凡是可以使用多态的地方都使用多态机制。  
只在必须使用RTTI的时候使用RTTI。  
1.多态机制要求我们拥有基类定义的控制权，但基类来自别人  
2.只是为了某个特定类的利益，而将某特性放进基类，使基类的其它子类带着这些无意义的东西