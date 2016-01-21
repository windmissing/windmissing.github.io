---
layout: post
title:  "const总结"
category: 编程语言
tags: [C++, const]
---

#### 一、const的作用

##### 1.将限定符声明为只读

方法：（1）在类型前加关键字const（2）必须初始化
举例：

```c++
const int i = 5;//正确
int j = 0;
const int k;//编译错误
i = j;//编译错误
j = i;//正确
```

<!-- more -->

##### 2.在另一连接文件文件中引用常量

方法：（1）在类型前加入关键字extern const（2）因为引用的是常量，不可以再次赋值
举例：

```c++
extern const int i;     //合法
extern const int j=10;  //非法，常量不可以被再次赋值
```

##### 3.用const修饰形参，对参数起保护作用

（1）用法1：若形参为const A* a，则不能对传递进来的指针的内容进行改变，保护了原指针所指向的内容，即能改变指向的地址，不能改变地址所存储的内容（1）
举例：

```c++
void Test(const int *a)
{
	a = new int(2);//正确，a指针new int，*a=2
	*a = 1;//错误，a不能给常量赋值
}
int main()
{
	int *a = new int(3);
	Test(a);
	return 0;
}
```
（2）用法2：如形参为const A& a，则不能对传递进来的引用对象进行改变，保护了原对象的属性。

对于自定义的数据类型，用引用值参速度较快，但会不改变原值，若不想改变，可以用const来保护

对于内置型数据类型，用引用值参不会使速度更快。如果是用引用传参，一般是为了改变原值，如果不想改变原值，就直接传参，不要用引用传参
 举例：

```c++
void Test(const int &a)//保护L7中的a不会被改变
{
	a = 2;//错误，a不能给常量赋值
}
int main()
{
	int a = 3;
	Test(a);
	return 0;
}
```

（3）用法3：若输入参数采用“值传递”方式，由于函数将自动产生临时变量用于复制该参数，该参数本就不需要保护，所以不用const修饰
举例：

```c++
//const能保护参数不被改变，但是这样没有意义，因为不管参数是否改变，对原来的a都没有影响
void Test(const int a)
{
	a = 2;//错误，a不能给常量赋值
}
int main()
{
	int a = 3;
	Test(a);
	return 0;
}
```

（4）对于非内部数据类型的输入参数，因该将“值传递”的方式改为“const引用传递”，目的是为了提高效率。例如，将void Func(A a)改为void Func(const A &a)

##### 4.用const修饰返回值，对返回值起保护作用

（1）用法1：用const修饰返回值为对象本身（非引用和指针）的情况多用于二目操作符重载函数并产生新对象的时候
举例：

```c++
const Rational operator*(const Rational& lhs, const Rational& rhs) 
{ 
	return Rational(lhs.numerator() * rhs.numerator(), 
	lhs.denominator() * rhs.denominator()); 
} 
Rational a,b; 
Radional c; 
(a*b) = c;//错误 
```

（2）用法2：不建议用const修饰函数的返回值类型为某个对象或对某个对象引用的情况。原因如下：如果返回值为某个对象为const（const A test = A 实例）或某个对象的引用为const（const A& test = A实例） ，则返回值具有const属性，则返回实例只能访问类A中的公有（保护）数据成员和const成员函数，并且不允许对其进行赋值操作，这在一般情况下很少用到。
举例：

```c++
class A
{
public:
	int y;
	A(int y):x(x),y(y){};
	void Sety(int y){this->y = y;}
};
const A Test1(A a)
{
	return a;
}
const A& Test2(A &a)
{
	return a;
}
int main()
{
	A a(2);
	Test1(a).Sety(3);//错误，因为Test1(a)的返回值是个const，不能被Sety(3)修改
	Test2(a).Sety(3);//错误，因为Test1(a)的返回值是个const，不能被Sety(3)修改
	return 0;
}
```

（3）用法3：如果给采用“指针传递”方式的函数返回值加const修饰，那么函数返回值（即指针）的内容不能被修改，该返回值只能被赋给加const 修饰的同类型指针。
举例：

```c++
const char * GetString(void){}
int main()
{
	char *str1=GetString();//错误
	const char *str2=GetString();//正确
	return 0;
}
```

（4）用法4：函数返回值采用“引用传递”的场合不多，这种方式一般只出现在类的赙值函数中，目的是为了实现链式表达。
举例：

```c++
class A
{
       //若负值函数的返回值加const修饰，那么该返回值的内容不允许修改，上例中a=b=c依然正确。(a=b)=c就不正确了。
	A &operate = (const A &other);  //负值函数
}
A a,b,c;              //a,b,c为A的对象
a=b=c;            //正常
(a=b)=c;          //不正常，但是合法
```

##### 5.在类成员函数的函数体后加关键字const

在类成员函数的函数体后加关键字const，形如：void fun() const; 在函数过程中不会修改数据成员。如果在编写const成员函数时，不慎修改了数据成员，或者调用了其他非const成员函数，编译器将报错，这大大提高了程序的健壮性。

如果不是在类的成员函数，没有任何效果，`void fun() const;`和`void func();`是一样的

#### 二、const常量与#define的区别

##### 1.const常量有数据类型，而宏常量没有数据类型。
而对后者只进行字符替换，没有类型安全检查，并且在字符替换时可能会产生意料不到的错误（边际效应）
举例：

```c++
#define I=10
const long &i=10;
/*由于编译器的优化，使得在const long i=10; 时i不被分配内存，而是已10直接代入以后的引用中，以致在以后的代码中没有错误，为达到说教效果，特别地用&i明确地给出了i的内存分配。不过一旦你关闭所有优化措施，即使const long i=10;也会引起后面的编译错误。*/
char h=I;      //没有错
char h=i;      //编译警告，可能由于数的截短带来错误赋值。
```

##### 2.使用const可以避免不必要的内存分配

由于const定义常量从汇编的角度来看，只是给出了对应的内存地址， 而不是象#define一样给出的是立即数，所以，const定义的常量在程序运行过程中只有一份拷贝，而#define定义的常量在内存中有若干个拷贝。
举例：

```c++
#define STRING "abcdefghijklmn\n"
const char string[]="abcdefghijklm\n";
printf(STRING);   //为STRING分配了第一次内存
printf(string);   //为string一次分配了内存，以后不再分配
printf(STRING);   //为STRING分配了第二次内存
printf(string);
```

#### 三、const的用法

##### 1.修改const的常量值

通过强制类型转换，将地址赋给变量，再作修改即可以改变const常量值。

```c++
const int i=0;
int *p=(int*)&i;
p=100;
```

##### 2.const数据成员的初始化只能在类的构造函数的初始化表中进行

```c++
class A
{
public:
	const int a;
	A(int x):a(x)//正确
	{
		a = x;//错误
	}
};
```
##### 3.const必须同时出现在声明和定义中

##### 4.构造函数不能声明为const

##### 5.在参数中使用const应该使用引用或指针，而不是一般的对象实例

const在成员函数中的三种用法（参数、返回值、函数）要很好的使用； 

不要轻易的将函数的返回值类型定为const; 

除了重载操作符外一般不要将返回值类型定为对某个对象的const引用;

#### 四、易出错的地方

##### 1.const修饰指针的情况
如果const位于星号的左侧，则const就是用来修饰指针所指向的变量，即指针指向为常量；如果const位于星号的右侧，const就是修饰指针本身，即指针本身是常量。

（1）L2和L3是一样的，const放在变量声明符的位置无关，这种情况下不允许对内容进行更改操作，如不能`*a = 3`

```c++
int i;
const int *a = &i;
int const*a = &i;
```
（2）针本身是常量，而指针所指向的内容不是常量，这种情况下不能对指针本身进行更改操作，如a++是错误的

```c++
int *const a = &i;
```

（3）指针本身和指向的内容均为常量

```c++
const int * const a = &i;
```

##### 2.mutable将数据声明为可变数据成员
可变数据成员永远不能成为const,即使它是const对象的成员

```c++
class A
{
public:
	int x;
	mutable int y;
	A(int a, int b):x(a),y(b){}
};
int main()
{
	const A a(1,2);//const对象必须初始化
	a.x = 3;//错误
	a.y = 3;//正确
	return 0;
}
```

##### 3.const成员函数返回的引用，也是const

```c++
/*从const成员函数返回的引用也是const*/
#include<iostream>
using namespace std;
class A
{
public:
	int x;
	void set(int x){this->x = x;}
	/*const成员函数返回的引用也是const，a
	如果把A&前面的const去掉会出错。
	因为返回的是一个const的对象，返回类型却不是const
	返回的内容和返回的类型不符*/
	const A& Test1()const
	{
		/*错误。这是const成员函数的特点*/
		x = 2;
		/*不限于*this。不管返回的是什么，哪怕是一个定义为非const的对象，结果也是一样的*/
		return *this;
	}
};
int main()
{
	A a, b;
	/*正确，虽然返回的是一个const，却用另一个非const来接收*/
	b = a.Test1();
	/*错误，既然是别名，那么别名的类型要与原来的类型相同*/
	A &c = a.Test1();
	//正确虽然在a.Test1()中a不能改变，但是这里已经出了这个成员函数的作用域
	a.set(2);
	//正确，b接收了a.Test1()返回的数据的内容，但是它不是const
	b.set(2);
	/*错误。a.Test1()是一个对象，这个对象是它的返回值，
	虽然没有名字，但是它就是a.Test1()的返回值，
	值是a.Test1()返回的值，类型是a.Test1()返回的类型，
	因此它是const*/
	a.Test1().set(2);
	return 0;
}
```

#### 五、思考题

##### 1.以下的这种赋值方法正确吗？

```c++
const A* c=new A(); 
A* e = c;
```
答：这种方法不正确，因为声明指针的目的是为了对其指向的内容进行改变，而声明的指针e指向的是一个常量，所以不正确； 


##### 2. 以下的这种赋值方法正确吗？ 
```c++
A* const c = new A(); 
A* b = c;
```
答：这种方法正确，因为声明指针所指向的内容可变；


##### 3.这样定义赋值操作符重载函数可以吗？ 
```c++
const A& operator=(const A& a);
```
答：这种做法不正确； 

在const A::operator=(const A& a)中，参数列表中的const的用法正确，而当这样连续赋值的时侯，问题就出现了： 

```c++
A a,b,c: 
(a=b)=c;
```
因为a.operator=(b)的返回值是对a的const引用，不能再将c赋值给const常量。

#### 4. 常量折叠

```c++
const int a = 1;
int *p = (int *)&a;
*p = 2;
cout<<*p<<" "<<a<<endl;
cout<<p<<" "<<&a<<endl;
```
输出：

2 1

0017FC30 0017FC30

答：常量折叠是其中一种被很多现代编译器使用的编译器最优化技术。常量折叠是在编译时间简单化常量表达的一个过程。简单来说就是将常量表达式计算求值，并用求得的值来替换表达式，放入常量表。可以算作一种编译优化。

在这里，a其实已经被1替代了。对i的计算就直接替换成对1的计算，而没有实际地去查a所在地址的值
