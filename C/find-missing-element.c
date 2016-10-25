//binary search to find a missing element
//the difference between middle and first or middle and last will be
//equal to the number of elements in that half.
#include <stdio.h>
#include <stdlib.h>
#include<time.h>
int cmpfunc(const void* a, const void* b)
{
return ((*(int*)a)-(*(int*)b));
}
void find_missing_binary_search(int arr[], size_t n)
{
int l=0;
int r=n-1;
int mid=0;

while(r>l)
		{
		mid=(l+r)/2;
			if(arr[mid]-arr[l]!=mid-l){
				if((mid-l)==1 && arr[mid]-arr[l]>1){
					printf("Missing element is %d \n", arr[mid]-1);
					return;
					}
			r=mid;
			}
			else if(arr[r]-arr[mid]!=r-mid){
				if((r-mid==1) && arr[r]-arr[mid]>1){
					printf("Missing element is %d \n", arr[mid]+1);
					return;
					}
			l=mid;
			}
			else
			{
				printf("Not found\n");
				return;
				}
		}
}
/*void missing_consecutive_num(int a[], int start, int end){
    int mid = (int)((start+end)/2);
    if(start+1 == end){
        if (a[start]+1 != a[end]){
            printf("Missing number is %d ", a[end]-1);
            exit(0);
        }
        else{
           return;
        }
    }
    missing_consecutive_num(a,start,mid);
    missing_consecutive_num(a,mid,end);

}*/
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
for(i=0; i<n; i++)
scanf("%i", (int *)&arr[0+i]);
//qsort(arr, n, sizeof(int), cmpfunc);
find_missing_binary_search(arr, n);
//missing_consecutive_num(arr,0,n);
return 0;
}

