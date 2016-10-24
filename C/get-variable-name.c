
///////get variable name///////////
#include <stdio.h>
#define getName(var)  #var
#define getName_str(var, str)  sprintf(str, "%s", #var)
int main()
{
    int myVar;
	char str[30];
    printf("%s\n", getName(myVar));
	getName_str(myVar, str);
	printf("%s", str);
    return 0;
} 
