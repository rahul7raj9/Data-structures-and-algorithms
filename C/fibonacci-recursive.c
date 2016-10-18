//fibonacci number
//not an efficient approach as it does lots of repeated computation. 
#include <stdio.h>
int fib(int );
int result=0;
void main()
{
int n = 0;
printf("Input the nth term for which you want the fibonacci number!!\n");
scanf("%d",&n);
result=fib(n);
printf("The %dth fibonacci element is %d\n",n, result);
}
int fib(int n){
	if (n==1 || n==2)
	{
		return 1;
	}else
	{
		result=fib(n-1)+fib(n-2);

		
	}
	
	return result;
}

