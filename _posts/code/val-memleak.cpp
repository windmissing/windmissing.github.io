#include <iostream>
using namespace std;

void test1()
{
    int *p = new int;
}

void test2()
{
    int *p = new int;
    char *p2 = (char *)p;
    delete p2;
}

class father
{
    int *p;
public:
    father(){p = new int;}
    ~father(){delete p;}
};

class son : public father
{
    int *p2;
public:
    son(){p2 = new int;}
    ~son(){delete p2;}
};

void test3()
{
    father *p = new son;
    delete p;
};
int main()
{
    test1();
    test2();
    test3();
    return 0;
}
