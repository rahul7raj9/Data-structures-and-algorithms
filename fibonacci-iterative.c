//Improving performance by storing the values 
//in an array. space complexity increases.
#include <stdio.h>
#include <conio.h>
void main()
{
int n;
int i=0;
int fibArray[50]={0};
printf("Enter the number of terms in Fibonacci Series: ");
scanf("%d", &n);
for(i=0;i<n;i++)
	{
	if (i<2){
	fibArray[i]=i;
	}
	else{
	fibArray[i]=fibArray[i-1]+fibArray[i-2];
	}
	printf("%d ", fibArray[i]);
	}
	getch();

}
