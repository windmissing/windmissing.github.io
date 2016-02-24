#include <iostream>
using namespace std;

#include "string.h"

void test1()
{
    char ch[10] = "abcdefghi";
    char *p1 = ch;
    char *p2 = ch + 3;
    memcmp(p1, p2, 5);
}

int main()
{
    test1();
    return 0;
}
