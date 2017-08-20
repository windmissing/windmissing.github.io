---
layout: post
title:  "《thinking in JAVA》片断记录 (十一)"
category: [读书笔记]
tags: []
---

容器的基本类型有List, Set, Queue, Map。  

---

Array与Array<Type>的区别

||Array|Array<Type>|
|---|---|---|
|存入对象|能存入任何对象|只能存入Type及其子类的对象|
|取出对象的类型|Object类型|与存入的类型相同|
|使用对象|需要转换成正确的对象类型|直接使用|

---

List的remove()、contains()等方法接受的都是对象的引用，并调用对象的equals()方法。因此这两个方法的效果与对象的equals()方法有很大关系。  
containsAll()方法与顺序无关。  
list的toArray()方法返回的是Object数组，如果要得到目标类型的数组，则传入目标类型的数据。例如：

```java
Object[] o = pets.toArray();
Pet[] p = pets.toArray(new Pet[0]);
```

---

迭代器是一个对象，它的工作是遍历并选择序列中的对象。  
JAVA中的iterator()只能单移动  

```java
Iterator<Pet> it = pets.iterator();
while(it.hashNext())
{
    Pet p = it.next();
    ... // do something to p
}
```

---

迭代器能够将遍历序列的操作与序列底层的结构分离  

```java
public class Test {

	public static void display(Iterator<String> it){
		while(it.hasNext()){
			String p = it.next();
			System.out.print(p+" ");
		}
		System.out.println();
	}
	
	public static void main(String[] args) {
		
		Collection<String> pets = new ArrayList<String>();
		pets.add("mouse");
		pets.add("dog");
		pets.add("cat");
		pets.add("pig");
		pets.add("bird");
		pets.add("fish");
		LinkedList<String> ll = new LinkedList<String>(pets);
		HashSet<String> hs = new HashSet<String>(pets);
		TreeSet<String> ts = new TreeSet<String>(pets);
		display(pets.iterator());
		display(ll.iterator());
		display(hs.iterator());
		display(ts.iterator());
	}
}
/* output
	mouse dog cat pig bird fish 
	mouse dog cat pig bird fish 
	mouse cat bird fish dog pig 
	bird cat dog fish mouse pig 
 */
```

---

LinkedList实现了基本的List接口，并添加了可以使其用作栈、队列功双端队列的方法。  

几个接口的比较： 

||getFirst()|elements()|peek()|removeFirst|remove|poll()|
|---|---|---|---|---|---|---|
|相同点|返回第一个元素|返回第一个元素|返回第一个元素|返回第一个元素|返回第一个元素|返回第一个元素|
|是否同时删除第一个元素|否|否|否|是|是|是|
|列表为时处理|异常|异常|返回null|异常|异常|返回null|

---

Collection是描述所有序列容器的共性的接口。  
使代码通用的方法有两种：1.使用Collection 2.使用迭代器  
对于Collection的实现类，两种方法都行。  
对于非Collection的外部，方法一必须实现Collection的全部接口，相比之下，方法二更方便。  

---

Iterable是一个接口，任何实现了这个接口的类，都可以使用foreach语法。   

```java
public class IterableClass implements Iterable<String> {
    ... //实现Iterable接口
    
    public static void main(String[] args)
    {
        for (String s : new InterableClass())
            ... //do something
    }
}
```

实现了Iterable的类一定可以使用foreach语法。  
支持foreach语法的对象不一定都是实现了IterableClass的类的实例。例如数组，可以用foreach语法，但没有实现Iterable接口。  

---

#### 结合适配器模式实现多种迭代方法

 - 背景  
有一个class，支持Iterable接口，可以通过foreach语法以Iterable接口的方法遍历这个class  
 - 需求
希望这个类可以通过foreach语法，以另一种方式编译这个类  
同时保持原遍历方法
 - 解决方法1  
继承并重写接口Iterable  
这样会导致原遍历方式不可用  
 - 解决方法2
继承并新境一个Iterable接口，例如：  

```java
class ReversibleArrayList<T> extends ArrayList<T> {
    public ReversibleArrayList(Collection<T> c) { super(c); }
    public Iterable<T> reversed() {
        return new Iterable<T>() {
            public Iterator<T> iterator() {
                return new Iterator<T>() {
                    int current = size() - 1;
                    public boolean hasNext() { return current > -1; }
                    public T next() { return get(current--); }
                    public void remove() { // Not implemented
                        throw new UnsupportedOperationException();
                    }
                };
            }
        };
    }
}
public class AdapterMethodIdiom {
    public static void main(String[] args) {
        ReversibleArrayList<String> ral = new ReversibleArrayList<String>(
            Arrays.asList("To be or not to be".split(" ")));
        // Grabs the ordinary iterator via iterator():
        for(String s : ral)
            System.out.print(s + " ");
        System.out.println();
        // Hand it the Iterable of your choice
        for(String s : ral.reversed())
        System.out.print(s + " ");
        }
} /* Output:
To be or not to be
be to not or be To
```

---

There’s no need to use the legacy classes **Vector, Hashtable, and Stack** in new code.  

---

