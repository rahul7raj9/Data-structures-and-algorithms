//quick sort
//O(logn) sorting algorithm. (average case). 
//inplace sort no extra overhead of the space
//worst case can go upto o(n^2)
#include <stdio.h>
#include <stdlib.h>
#include<time.h>
#include<stdbool.h>
void swap(int *a, int *b)
{
int temp;
temp=*a;
*a =*b;                        
*b = temp;
return;
}
int partition(int a[],int start ,int n)
{
int pivot = start;
int l=start+1;
int r=n;
while(l<=r){
	while(a[l]<a[pivot])
		l+=1;
	while(a[r]>a[pivot] && r>0)
		r-=1;
	if(r<=l){
		break;
	}
	else{
	swap(&a[l],&a[r]);
	}
}
swap(&a[r], &a[pivot]);
return r;
}
void q_sort(int a[],int l ,int r)
{
if(r-l<=0)
	return;
else
	{
	int mid=0;
	mid=partition(a,l,r);
	q_sort(a, l, mid-1);
	q_sort(a, mid+1, r);
	}
	
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
q_sort(arr, 0, n-1);
printf("\nSorted array is\n");
for(i=0;i<n;i++)
    printf("%d ", arr[i]);
return 0;
}
