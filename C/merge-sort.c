//merge sort
//O(n^2)
#include <stdio.h>
#include <stdlib.h>
#include<time.h>

int b[20];
void merge(int arr[], int l, int m, int r)
{
 int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;
 
    /* create temp arrays */
    int L[n1], R[n2];
 
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[(m + 1)+ j];
 
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = l; // Initial index of merged subarray
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 /* Copy the remaining elements of L[], if there
       are any */
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    /* Copy the remaining elements of R[], if there
       are any */
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}
void merge_sort(int a[], int low, int high)
{
int mid;
if(low<high){
mid=(low+high)/2;
merge_sort(a, low, mid);
merge_sort(a, mid+1, high);
merge(a, low, mid, high);
}
else{
return;
}
}

int main(void)
{
size_t n ;
printf("Enter the number of elements in a array\n");
scanf("%d", (int*)(&n));
int a[n];
size_t seed;
seed=time(NULL);
srand(seed);
int i=0;
printf("Input array is \n");
for(i=0; i<n; i++)
{
a[i]=rand()%20;
printf("%d ",a[i]);
}
merge_sort(a,0,n-1);
printf("\nSorted array is\n");
for(i=0;i<n;i++)
    printf("%d ", a[i]);
return 0;
}
