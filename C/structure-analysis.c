#include <stdio.h>
 
// structure A
typedef struct structa_tag
{
   char        c;
   short int   s;
} structa_t;
 
// structure B
typedef struct structb_tag
{
   short int   s;
   char        c;
   int         i;
} structb_t;
 
// structure C
typedef struct structc_tag
{
   char        c; //4 (1+3)
   int         s; //4 (4)
   short       x; //4 (2+2)
   double      d; //  (4+8)
  
} structc_t;
 
typedef struct structf_tag
{
   char        c; //4 (1+3)
   double      d; //  (4+8)
   int         z;
  
} structf_t; 
// structure D
typedef struct structd_tag
{
   double      d;
   int         s;
   char        c;
} structd_t;
 
int main()
{
   printf("sizeof(structa_t) = %d\n", sizeof(structa_t));
   printf("sizeof(structb_t) = %d\n", sizeof(structb_t));
   printf("sizeof(structc_t) = %d\n", sizeof(structc_t));
   printf("sizeof(structd_t) = %d\n", sizeof(structd_t));
	printf("sizeof(structf_t) = %d\n", sizeof(structf_t));
   return 0;
}
