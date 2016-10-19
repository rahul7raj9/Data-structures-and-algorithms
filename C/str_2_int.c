//STRING TO INTEGER
/////////////////////////////////////////////////////////////////////////////////
//The value of a char can be 0-255, where the different ////////////////////////
//characters are mapped to one of these values. The numeric digits////////////// 
//are also stored in order '0' through '9', but they're also not typically/////
//stored as the first ten char values. That is, the character '0' ////////////
//doesn't have an ASCII value of 0. The char value of 0 is almost//////////// 
//always the \0 null character./////////////////////////////////////////////
//Without knowing anything else about ASCII, it's pretty straightforward////
//how subtracting a '0' character from any other numeric character ////////
//will result in the char value of the original character.////////////////
//So, it's simple math////////////////////////////////////////////////://
//'0' - '0' = 0  // Char value of character 0 minus char value of ///////
//character 0///////////////////////////////////////////////////////////
// In ASCII, that is equivalent to this:///////////////////////////////
//48  -  48 = 0 // '0' has a value of 48 on ASCII chart///////////////
//So, similarly, I can do integer math with any of the char///////////
//numberics...///////////////////////////////////////////////////////
//(('3' - '0') + ('5' - '0') - ('2' - '0')) + '0') = '6'/////////////
///////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////
#include <stdio.h>
int num_int=0;
int to_int(char num[])
{
int n=0;
int i=0;
for(i=0;num[i]!='\0';i++)
{
num_int=num_int*10+num[i]-'0';
}
return num_int;
}
void main ()
{
char num[]="100";
num_int=to_int(num);
printf("%d is the integer representation for of the string %s",num_int, num);
}
