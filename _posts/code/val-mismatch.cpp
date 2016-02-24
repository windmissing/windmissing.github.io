#include <iostream>
using namespace std;

void test1()
{
    int *p = new int[5];
    delete p;
}

int main()
{
    test1();
}
