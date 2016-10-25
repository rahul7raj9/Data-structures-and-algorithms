//binary search

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
void binary_search(int*, size_t, int);
int cmpfunc (const void * , const void *);

int main(void){
size_t n=0;
time_t seed;
int num=0;
seed=time(NULL);
srand(seed);
printf("input the total number of integers to be generated\n");
scanf("%d", (int *)&n);
printf("Enter the number to be searched\n");
scanf("%d", &num);
int arr[n];
int i=0;
for(i=0;i<n;i++){
	arr[i]=rand()%10;
			}
binary_search(arr , n, num);
return 0;
}
int cmpfunc (const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}
void binary_search(int arr[], size_t n, int num){
int i=0;
//void qsort(void *base, size_t nitems, size_t size, 
//int (*compar)(const void *, const void*))
qsort( arr,n,sizeof(int), cmpfunc);
printf("Input array is..\n");
for(i=0;i<n;i++)
{
printf("%d ", arr[i]);
}
int l=0;
int r=n;
while(r>l)
	{
		int mid = (l+r)/2;
		if(num==arr[mid]){
		printf("\nThe element to be searched is at index %d ", mid);
		return;
		}
		else if(arr[mid]>num)
		r=mid-1;
		
		else
		l=mid+1;
	}
	printf("\nnumber not found\n");
	return;
}
