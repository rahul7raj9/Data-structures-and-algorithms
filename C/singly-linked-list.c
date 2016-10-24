//singly likned list
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include<assert.h>
typedef struct Node{
int data;
struct Node *next;
}node;

//take current and head as global
node *head=NULL;
//node *current=NULL;

///////////////////////////////
//Different Functions prototype
node* getNode();
void insertFront(int data);
void deleteBack();
void size();
void printList();
void insertBack(int data);
void deleteFront();
void deleteData(int data);
void insertIndex(int data);
void reverse(); //using iterative
void sort();
void kthlast(int n);
void removeDup();
void reverseRecursive(node* head);
void reversePrint(node *);
void findLoop();
static void swap(node*, node*);
//////////////////////////
///PRINT LIST////////////
void printList()
{
node* first = head;
if(first==NULL)
{
printf("No data in the list..");
return;
}
while(first!=NULL)
{
printf("%d\n",first->data);
first=first->next;
}
}
//////////////////////////
///kth last/////////////////
void kthlast(int n)
{

node* first=head;
node* kth=head;
int i=0; 
if (first==NULL){
	printf("List is empty no kth last element\n");
	return;
}
if(first->next==NULL){
	printf("Only 1 element in the list. its value is %d", first->data);
	return;
}
//
for(i=0;i<n-1;i++){
printf("%d\n ",first->data);
first=first->next;
}
while(first->next !=NULL){
kth=kth->next;
first= first->next;
}
printf("kth last element is %d",kth->data);
}
/////////////////////////
//DELETE FRONT////////////
void deleteFront()
{
node* first = head;
if (first==NULL){
printf("List is empty from deleteFront\n");
return;
}
head=first->next;
printf("Value deleted is %d\n",first->data);
free(first);
}

//////////////////////////
/////DELETE DATA///////////
void deleteData(int data)
{
node* first = head;
node* temp;
if (head==NULL){
printf("List is empty..\n");
return;
}
//check first data
if (first->data==data){
head=first->next;
free(first);
return;
}
while(first->next!=NULL){
if(first->next->data!=data){
first=first->next;
}
else{
printf("Found\n");
temp=first->next;
first->next=temp->next;
free(temp);
return;
}
}
printf("Data not found\n");
}
//////////////////////////
//insert at the front/////
void insertFront(int data)
{
node* newNode = getNode();
//check if head is null
if (head==NULL){
	head = newNode;
	newNode->data = data;
	}
else{
	node* temp = head;
	newNode->data = data;
	head = newNode;
	head->next = temp;
	}
}
////////////////////////////////////
////DELETE BACK/////////////////////
void deleteBack()
{
node* first = head;
node* temp;
if (head==NULL){
printf("List is empty\n");
return;
}
if(head->next==NULL){
printf("value deleted is %d Now the list is empty\n",head->data);
free(head);
}
while(first->next->next != NULL)
{
first=first->next;
}
temp=first->next;
first->next=NULL;
printf("value deleted is %d\n",temp->data);
free(temp);
}
///////////////////////////////
///INSERT BACK////////////////
void insertBack(int data)
{
node* first=head;
node* newNode=getNode();
newNode->data=data;
if(first==NULL){
	head=newNode;
	return;
}
while(first->next!=NULL){
first=first->next;
}
first->next=newNode;
}
//////////////////////////////
////LENGTH OF LIST/////////////
void size()
{
node* first=head;
int count=0;
while(first!=NULL){
count+=1;
first=first->next;
}
printf("The length of the list is %d\n", count);
}
///////////////////////////////
//PRINT REVERSE////////////////
void reversePrint(node *first)
{
if (first==NULL)
{
return;
}
reversePrint(first->next);
printf("%d\n",first->data);
}
//////////////////////////////
////////TO DO THIS////////////
void reverseRecursive(node* temp)
{
node* first=temp;
node* rest=first->next;
if (first==NULL)
{
return;
}
if(rest == NULL){
return;
}
head=rest;
reverseRecursive(head);
rest->next=first;
first->next=NULL;
//first->next=NULL;
head=rest;
}
//////////////////////////////////
/////SELECTION SORT//////////////
void sort()
{
int min;
node* min_node;
node* first=head;
node* rest=first->next;

while(first!=NULL){
	min=first->data;
	min_node = first;
	rest=first->next;
	while(rest!=NULL)
	{
		if (min>rest->data)
		{
			min_node=rest;
		}
	rest=rest->next;
	}
	swap(first,min_node);
	first=first->next;
	//rest=first->next;
	}
}
/////////////////////////////////
////swap 2 nodes//////////////////
static void swap(node* a, node* b)
{
int temp;
temp=a->data;
a->data=b->data;
b->data=temp;
return;
}
////////////////////////////////
/////REVERSE ITERATIVE//////////
void reverse()
{
node *first=head;
if(first->next==NULL){
printList();
return;
}
node *current=head->next;
node *temp=current->next;
current->next=first;
first->next=NULL;
while(temp!=NULL)
{
first=current;
current=temp;
temp=temp->next;
current->next=first;
}
head=current;
printList();

}
///////////////////////////////////////////////////////////
//main function will do all the insert and delete from this.
int main(void)
{
insertFront(10);
insertFront(20);
insertFront(30);
insertFront(40);
insertFront(50);
printList();
printf("-------------\n");
//reversePrint(head);
//reverse();
printf("--------------\n");
//reverseRecursive(head);
sort() ;
printList();
//kthlast(7);
//printList();
//deleteData(10);
//deleteFront();
//deleteData(20);
//size();
//printList();
//size();
//deleteBack();
//insertBack(40);
//insertBack(250);
//insertBack(20);
//size();
//deleteData(250);
//size();
///insertBack(150);
//printList();
//size();
//deleteData(150);
//size();
return 0;
}
//
node* getNode()
{
node* newNode = (node*) malloc(sizeof(node));
assert(newNode!=NULL);
newNode->data=0;
newNode->next = NULL;
return newNode;
}
//
