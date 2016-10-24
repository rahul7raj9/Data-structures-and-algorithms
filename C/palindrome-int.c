//palindrome number
#include <stdio.h>
#include <stdbool.h>
void is_palindrome(int num)
{
int n=num;
int rem=0, rev=0;
while(n!=0)
{
rem=n%10;
rev=rev*10+rem;
n=n/10;
}
//printf("%d\n", rev);
if (rev==num)
{
printf("is palindrome");
}
else
{
printf("not a palindrome");
}
}

int main(void)
{
int num=1551;
is_palindrome(num);
return 0;
}
