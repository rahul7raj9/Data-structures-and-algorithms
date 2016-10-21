//string comparison
#include<stdio.h>
#include<string.h>
#include<stdlib.h> //for exit(0)
int version_compare(char *, char *);

main(int argc, char **argv)
{
	if (argc!=3)
		{
		printf(" 0 or more than 2 inputs are not valid\n");
		exit(0);
		}
	else
		{
		int bool_true;
		char *version1;
		char *version2;
		version1=argv[1];
		version2=argv[2];
		printf("Versions 1 and 2 are: \n%s\n%s\n",version1, version2);
		bool_true=version_compare(version1, version2);
		//printf("value returned from function is %d\n",bool_true);
		if (bool_true==0)
		   printf("Both the versions are same");
		else
		   printf("Different Versions");
	}
}
int version_compare(char *version1, char *version2)
{
//printf("Versions 1 and 2 are: \n%s\n%s",version1, version2);
//return strcmp(version1, version2);
int len_1, len_2;
int i=0,j=0;
len_1=strlen(version1);
len_2=strlen(version2);
if (len_1!=len_2)
	return -1;
for(i=0;i<len_1;i++)
	{
	if (version1[i] != version2[i])
		{
		//printf("From here\n");
		printf("Different at position  %i\n",i);
		return -1;
		}
	}
return 0;
//return 1;
}
