#include <iostream>
using namespace std;

int main()
{
    int *p = new int;
    delete p;

    *p = 3;
    return 0;
}
