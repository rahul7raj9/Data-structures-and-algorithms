#include<stdio.h>
#define INC(X) X+1

int main()
{
printf("%d\n", INC(3));
printf("%s\n",INC("ABC"));
int a[]={23,4};
int *p=a;
printf("%d\n",*(INC(p)));
}
