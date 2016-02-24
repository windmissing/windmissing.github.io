#include <iostream>
using namespace std;
#include "string.h"

void test1()
{
    int s[5] = {1, 2, 3, 4, 5};
    cout<<s[5]<<endl;
}

void test2()
{
    int *s = new int[5];
    memset(s, 0, sizeof(s));
    cout<<s[5]<<endl;
    delete []s;
}

void print(int *s, int id)
{
    cout<<s[id]<<endl;
}

void test3()
{
    int s[5] = {1, 2, 3, 4, 5};
    print(s, 5);
}
int main()
{
    test1();
    test2();
    test3();
    return 0;
}
