//Bubble Sort
//O(n^2)
#include <stdio.h>
#include <stdlib.h>
#include<time.h>
void swap(int *a, int *b)
{
int temp;
temp=*a;
*a =*b;                        
*b = temp;
return;
}
void insertion_sort(int a[], int n)
{
int i=0;
int j=0;
int first=0;
for(i=1;i<n;i++)
	{
		first=a[i];
		j=i-1;
		while(j>=0 && first<a[j])
		{
		a[j+1]=a[j];
		j=j-1;
		}
	a[j+1]=first;
}
return;
}
int main(void)
{
size_t n ;
printf("Enter the number of elements in a array\n");
scanf("%d", (int*)(&n));
int arr[n];
size_t seed;
seed=time(NULL);
srand(seed);
int i=0;
printf("Input array is \n");
for(i=0; i<n; i++)
{
arr[i]=rand()%20;
printf("%d ",arr[i]);
}
insertion_sort(arr,n);
printf("\nSorted array is\n");
for(i=0;i<n;i++)
    printf("%d ", arr[i]);
return 0;
}
