//permutation of all numbers

#include <stdio.h>
#include <string.h>
void swap(char *, char *);
void permute(char *, int, int);
void swap(char *a, char *b)
{
char temp;
temp=*a;
*a=*b;
*b=temp;
}
void permute(char *s, int l, int r)
{
int i;
if (l == r){
	printf("%s\n", s);	
	}
else{
for (i=l;i<=r;i++)
{


swap((s+l),(s+i));
permute(s,l+1,r);
swap((s+l),(s+i));
}
}
}
int main()
{
char str[] = "RAJ"; //string for which we want to find permutation
int n= strlen(str);
permute(str, 0, n-1);
return 0;
}


