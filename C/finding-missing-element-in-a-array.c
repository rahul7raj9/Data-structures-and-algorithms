#include <stdio.h>
int find_missing(int *arr, int n);


int find_missing(int *arr, int n)
{
    int i;
    int sum;
    //sum=n(n+1)/2//since total numbers = n+1. so (n+1)*(n+2)/2//
    sum=(n+1)*(n+2)/2;
    printf("sum=%d\n",sum);
    for(i=0;i<n;i++)
    {
        //printf("array values=%d\n",arr[i]);
        sum-=arr[i];
    }
    return sum;
    
}

int main()
{
    printf("Hello, World!\n");
    int value=0;
    int a[]={1,2,3,4,6};
    int n=sizeof(a)/sizeof(int);
    value=find_missing(a, n);
    printf("The missing value is %d\n",value);
    return 0;
}


