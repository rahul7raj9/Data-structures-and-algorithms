//time of the day
#include <stdio.h>
#include <time.h>
#define LEN 50
void main()
{
char buf[LEN];
time_t curr_t;
time_t start_t, end_t;
double diff_t;
//structure tm has days, date, and time stored in it
struct tm *loc_time;
time(&start_t);
//local time returns object of struct tm
loc_time=localtime(&start_t);
//asc time takes ptr to the tm structure and gives the time and date in 
//string format
printf("Time using asctime is %s\n",asctime(loc_time));
//to change the format of the output we have to use strftime
strftime(buf, LEN, "Time using strftime is %H:%M:%S %p \n", loc_time);
//fputs(buf, stdout);
printf("%s",buf);
//pointer to the time
//time_t data type to store the system time value
//they are returned from time() function
//this will return the time in seconds since 1 january 1970.
time(&curr_t);
printf("Time using time() is %s\n",ctime(&curr_t));//ctime coverts the time to string 
time(&end_t);
//difftime returns difference in time in seconds
printf("Execution time is %f", difftime(end_t,start_t));
}
