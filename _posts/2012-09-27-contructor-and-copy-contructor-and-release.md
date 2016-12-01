---
layout: post 
title:  "构造函数、复制构造函数、析构函数混合使用总结"
categories: 编程语言
tags: [c++, 类, 复制构造函数]
---

一、用法

构造函数的用法：类的声明、定义与初始化
复制构造函数的用法：复制构造函数总结

2.一些混合使用的例子

1.关于强制类型转换
class A
{
	int x;
public:
	A(int i):x(i){cout<<"construct     "<<this<<endl;}
	A(const A& a){x = a.x;cout<<"copy     "<<this<<endl;}
	~A(){cout<<"delete     "<<this<<endl;}
	void operator=(const A& a){x = a.x;cout<<"=     "<<this<<endl;}
	void get(){cout<<x<<endl;}
	void set(int i){x = i;}
};
int main()
{
	A a(99), b(35);
	a.get();
	a = 1000; //隐式的强制类型转换 + 赋值
	a.get();
	a = A(2); //显式的强制类型转换 + 赋值
	a.get();
	a = b;    //赋值
	a.get();
	return 0;
}

输出：
construct     0012FF38     //a的构造
construct     0012FF34     //b的构造
99
construct     0012FF30     //临时对象的构造
=     0012FF38             //赋值
delete     0012FF30        //临时对象的析构
1000
construct     0012FF2C     //临时对象的构造
=     0012FF38             //赋值
delete     0012FF2C        //临时对象的析构
2
=     0012FF38             //赋值
35
delete     0012FF34        //
delete     0012FF38        //
解释：不管是显示类型转换还是隐式类型转换，都有以下一些共同点：
1）先构造一个临时对象，把临时对象赋值给目标，然后析构临时对象
2）由于要构造一个临时对象，必须要有只带一个参数的构造函数
3）由于要用到赋值函数，当类中有指针成员时，要定义自己的复制控制函数

2.两个例子对比看
class A
{
public:
	A(){cout<<"construct     "<<this<<endl;}
	A(const A& a){cout<<"copy     "<<this<<endl;}
	~A(){cout<<"delete     "<<this<<endl;}
	void operator=(const A& a){cout<<"=     "<<this<<endl;}
	A Test(){return *this;}
};
int main()
{
	A a;
	A b = a.Test(); 
	return 0;
}
输出：
construct     0012FF38  //a的构造
copy     0012FF34       //b的构造（返回值的构造）
delete     0012FF34     //b的析构（返回值的析构）
delete     0012FF38     //a的析构
解释：
L13中，b是返回值的别名，返回值是*this的复制，*this就是a
因此：b = 返回值 = *this的副本 = a的副本
class A
{
public:
	A(){cout<<"construct     "<<this<<endl;}
	A(const A& a){cout<<"copy     "<<this<<endl;}
	~A(){cout<<"delete     "<<this<<endl;}
	void operator=(const A& a){cout<<"=     "<<this<<endl;}
	A Test(){return *this;}
};
int main()
{
	A a, b;
	b = a.Test(); 
	return 0;
}

输出：
construct     0012FF38   //a的构造
construct     0012FF34   //b的构造
copy     0012FF30        //返回值的构造
=     0012FF34           //把返回值的内容赋值给b
delete     0012FF30      //返回值的析构
delete     0012FF34      //b的析构
delete     0012FF38      //a的析构
解释：
L13中，把返回值的内容赋值给b，然后返回值析构