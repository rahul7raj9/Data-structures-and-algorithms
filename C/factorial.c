//program to find factorial of a given number.
//complexity is O(n) 
#include<stdio.h>
int fact(int );
int result;
void main()
{
int n=0;
printf ("Enter the value for which you want to find the factorial\n");
scanf("%d",&n);
result=fact(n);
printf ("Factorial of %d is %d",n,result);
}
int fact(int a)
{
if (a==1 || a==0){
	return 1;
	}	
else{
	result=a*fact(a-1);
	}
return result;
}
