文字是转载的，图是原创的。
1、空类的sizeof是1。空类是指没有成员的类，类中的函数不占空间，除非是虚函数。
class A
{
       public:
       A(){}
       ~A(){}
       void fun(){}
};

sizeof(A)是1.
注：
class A1
{
 public:
     A1(){}
     ~A1(){}
     void fun(){}
     char a[0];
};
sizeof(A1)也是1.（VC6.0下编译）
2、若类中包含成员，则类对象的大小只包括其中非静态成员经过对齐所占的空间，对齐方式和结构体相同。如：
class A
{
public:
    int b;
    float c;
    char d;
};

sizeof(A)是12.
class A
{
public:
    static int a;
    int b;
    float c;
    char d;
};
sizeof(A)是12.
class A
{
public:
	static int a;
	int b;
	float c;
	char d;
	int add(int x,int y)
	{
		return x+y;
	}
};

sizeof(A)也是12.
![](http://img.my.csdn.net/uploads/201212/21/1356092197_6948.jpg)
 
3、若类中包含虚函数，则无论有几个虚函数，sizeof类都等于sizeof(数据成员)的和+sizeof(V表指针，为4)，如：
class Base
{
      public:
             Base(){cout<<"Base-ctor"<<endl;}
             ~Base(){cout<<"Base-dtor"<<endl;}
             int a;
             virtual void f(int) {cout<<"Base::f(int)"<<endl;}
             virtual void f(double){cout<<"Base::f(double)"<<endl;}
};
sizeof(Base)为8.
![](http://img.my.csdn.net/uploads/201212/21/1356092419_1293.jpg) 
4、对于子类，它的sizeof是它父类成员（无论成员是public或private)，再加上它自己的成员，对齐后的sizeof，
![](http://img.my.csdn.net/uploads/201212/21/1356093064_2665.jpg)
class A2
{
      public:
             int a;
      private:
              char b;
};
class A3:public A2
{
      public:
             char b;
             short a;             
};
sizeof(A3)是12. 但如果A3如下：
![](http://img.my.csdn.net/uploads/201212/21/1356093149_6349.jpg)
class A3:public A2
{
      public:
             short a;  
             char b;           
};
sizeof(A3)是12.
 
5、对于子类和父类中都有虚函数的情况，子类的sizeof是它父类成员（无论成员是public或private)，再加上它自己的成员，对齐后的sizeof，再加4（虚表指针）。如：
class Base
{
      public:
             Base(){cout<<"Base-ctor"<<endl;}
             ~Base(){cout<<"Base-dtor"<<endl;}
             int a;
             virtual void f(int) {cout<<"Base::f(int)"<<endl;}
             virtual void f(double){cout<<"Base::f(double)"<<endl;}
};
class Derived:public Base
{
  public:
         Derived(){cout<<"Derived-ctor"<<endl;}
         int b;
         virtual void g(int){cout<<"Derived::g(int)"<<endl;}
};
sizeof(Derived)是12.
 
6、对于虚继承的子类，其sizeof的值是其父类成员，加上它自己的成员，以及它自己一个指向父类的指针（大小为4），对齐后的sizeof。如：
#include   <iostream.h>   
class   a   
{   
private:   
	int   x;   
};   
class   b:   virtual   public   a   
{   
private:   
	int   y;   
};   
class   c:   virtual   public   a   
{   
private:   
	int   z;   
};   
class   d:public   b,public   c   
{   
private:   
	int   m;   
};   
int   main(int   argc,   char*   argv[])   
{   
	cout<<sizeof(a)<<endl;   
	cout<<sizeof(b)<<endl;   
	cout<<sizeof(c)<<endl;   
	cout<<sizeof(d)<<endl;   
	return   0;   
}   
    在VC6.0下调试结果为   
  4   
  12   
  12   
  24
sizeof(b)和sizeof(c)相同，都是4+4+4=12。
sizeof(d)是sizeof(b)(为12)+sizeof(c)(为12）-b和c相同的部分（a的成员，大小是4）+d自己的成员（大小为4）=24
7、对于既有虚继承又有虚函数的子类，其sizeof的值是其父类成员（计算虚表指针大小+4），加上它自己的成员（计算虚表指针大小+4），以及它自己一个指向父类的指针（大小为4），对齐后的sizeof
class Base
{
public:
	Base(){cout<<"Base-ctor"<<endl;}
	~Base(){cout<<"Base-dtor"<<endl;}
	virtual void f(int) {cout<<"Base::f(int)"<<endl;}
	virtual void f(double){cout<<"Base::f(double)"<<endl;}
};
class Derived:virtual public Base
{
public:
	Derived(){cout<<"Derived-ctor"<<endl;}
	virtual void g(int){cout<<"Derived::g(int)"<<endl;}
};
sizeof（Base）=4
sizeof（Derived）=12 （父类虚表指针大小4+自己虚表指针大小4+子类指向父类的一个指针大小4=12)