#include <iostream>
using namespace std;

#include "string.h"

void test1()
{
    int a;
    cout<<a+3<<endl;
}

void test2()
{
    char *p1 = new char[50];
    char *p2 = new char[50];
    memcpy(p1, p2, 50);
    delete []p1;
    delete []p2;
}

void test3()
{
    char *p1 = new char[50];
    char *p2 = new char[50];
    memcpy(p1, p2, 50);
    cout<<p1[3]<<endl;
    delete []p1;
    delete []p2;
}

void test4()
{
    char p1[50];
    char p2[50];
    memcpy(p1, p2, 50);
    cout<<p1[3]<<endl;
}

int main()
{
    test1();
    test2();
    test3();
    test4();
    return 0;
}
