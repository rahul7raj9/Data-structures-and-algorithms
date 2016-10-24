//size without using sizeof
//
#include<stdio.h>
int main(void)
{
int a;
int size_int = (char *)((&a)+1)-(char *)(&a);
printf("size of int is %i", size_int);
return 0;
}
