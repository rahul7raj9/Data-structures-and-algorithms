//stack implementation
//other way is creating stack with structures.

#include <stdio.h>

#define MAX 3

int top = -1;
int stack[MAX];


int is_empty()
{
if (top==-1)
return 1;
else
return 0;
}

int is_full()
{
if(top==MAX-1)
return 1;
else
return 0;
}

void push(int a)
{
if (is_full()==0){
printf("Value pushed to the stack is %d \n", a);
top++;
stack[top]=a;
}
else
{
printf("Stack is full can't push\n");
return;
}
}

void pop()
{
if(is_empty()==0)
{
int val=0;
val=stack[top];
top--;
printf("value popped is %d \n", val);
}
else
{
printf("Stack is empty..can't pop..\n");
}
}

int main(void)
{
push(5);
push(4);
push(3);
push(2);
push(1);
pop();
pop();
push(1);
push(2);
push(3);

return 0;
}
