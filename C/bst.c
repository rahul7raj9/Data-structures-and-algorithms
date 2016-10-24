//binary search tree
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>


//size of this structure is 24 bytes.
//4+8+8
typedef struct Node{
int data;
struct Node* left;
struct Node* right;
}node;
node* root;
void insert(node* , int );
void insertRecursive(node* , node* );
//////////////////////////////////////
/////get the new node////////////////
node* getNode()
{
node* newNode = (node*)(malloc(sizeof(node)));
assert(newNode!=NULL);
newNode->data=0;
newNode->left=NULL;
newNode->right=NULL;
return newNode;
} 
//////////////////////////////////
////////INSERT IN A TREE/////////
void insert(node* root, int data)
{
	printf("data is %d\n",data);
	node* newNode=getNode();
	newNode->data=data;
	node *head=root;
	node *temp;
	if (head==NULL)
	{
		head=newNode;
		return;
	}

while(head!=NULL)
{
	temp=head;
	if (data > head->data)  //insert right
		{
			head=head->right;
		}
	else{
	 //insert left
		head=head->left;	
		}
}
if(temp->data > data){
	temp->left=newNode;
	}
else
	temp->right = newNode;

}
/////////////////////////////////////////////////////////////
////////FIND MINIMUM/////////////////////////////////////////
void find_min()
{
node*head=root;
while(head->left!=NULL)
head=head->left;

printf("The minimum element is %d\n", head->data);
return;
}
/////////////////////////////////////////////////////////////
////////INSERT RECURSIVE////////////////////////////////////
void insertRecursive(node* head, node* newNode)
{
node* prev;
if (head==NULL)
	{
	head=newNode;
	return;
	}
if (head->data>newNode->data)
	{
	if(head->left==NULL)
		{
			head->left=newNode;
		}
	else{
		insertRecursive(head->left, newNode);
		}
	}
else{
	if (head->right==NULL)
		{
			head->right=newNode;
		}
	else{
		insertRecursive(head->right, newNode);
		}
	}
	return;
}
/////////////////////////////////////////////////////////////////
////VALIDATE A BST//////////////////////////////////////////////
void validateBST(node* head){
int valid_flag=0;
if(head==NULL){
return;
}
else{
	if (head->left!=NULL)
		{
		if(head->data>head->left->data)
			{
			validateBST(head->left);
			}
		else
			{
			printf("Not a valid BST\n");
			return;
			}
		}
	if (head->right!=NULL)
		{
		if(head->data<head->right->data)
			{
			validateBST(head->right);
			}
		else
			{
			valid_flag=1;
			printf("Not a valid BST\n");
			return;
			}
		}
	else{
		return;
		}
	
}

if (valid_flag==0)
printf("valid BST\n");
return;
}
////////////////////////////////////////////////////////////////
////////	PRINT INORDER//////////////////////////////////////
void printTree(node* head)
{

if(head!=NULL)
	{
	printTree(head->left);
	printf("%d ", head->data);
	printTree(head->right);
	}
	return;
}
////////////////////////////////////////////////////////////////
////////FIND KTH LARGEST///////////////////////////////////////
int count=0;
void kthlargest(node* first, int k)
{
node* head=first;
if (head==NULL)
	{
	return;
	}
else
	{
	if(head!=NULL && count<k)
		{
		kthlargest(head->right, k);
		count+=1;
		if(count==k)
		{
		printf("%d largest element is %d\n", count,head->data);
		return;
		}
	kthlargest(head->left, k);	
	}
	return;
}
}
//////////////////////////////////////////////////////////////////
///////LEVEL ORDER LARGEST////////////////////////////////////////
void level_orderTraversal()
{
node* arr[20]={NULL};
int first= 0, last=0;
node* head=root;
node* currNode;
if(head==NULL)
return;
arr[last]=head;
last+=1;
while(first<last)
	{
	currNode=arr[first];
	printf("%d ", currNode->data);
	first+=1;
	if (currNode->left!=NULL)
		{
			arr[last]=currNode->left;
			last+=1;
		}
	if (currNode->right!=NULL)
		{
			arr[last]= currNode->right;
			last+=1;
		}
}
}
/////////////////////////////////////////////////////////
///////////INORDER SUCCESSOR/////////////////////////////
///ALGO///
//if RST not NULL --> successor in RST go to RST and find min node.
//if RST is NULL --> start from root, travel down the tree, 
//if node data > root data go right otherwise go left.
//if data on left successor = root
//root = root->left
int inorder_successor(node* n)
{
node* head=root;
node* sucess;
node* prev;
if (n->right != NULL){
    n=n->right;
	while(n!=NULL)
	{
	prev=n;
	n=n->left;
	}
	return prev->data;
}
while(head!=NULL)
	{
		if(n->data > head->data) //going right
			{
			head=head->right;
			}
		else if (n->data < head->data)
			{
				sucess=head;
				head=head->left;
			}
		else
			break;
	}
return sucess->data;
}
/////////////////////////////////
/////////////LCA////////////////
int LCA(int n1, int n2)
{
while(root!=NULL)
	{
		if(n1 > root->data && n2 > root->data)
			root=root->right;
		else if(n1 < root->data && n2 < root->data)
			root=root->left;
		else
			break;
	}
	return root->data;
}
/////////////////////////////////////////////////////////////////
////////MAIN FUNCTION////////////////////////////////////////////
int main(void)
{
int succ=0;
int seed = time(NULL);
srand(seed);
int n=0, i=0;
int root_val=0;
root=getNode();
printf("Input the total number of elements in the tree\n");
scanf("%d", &n);
printf("Input the root node in the tree\n");
scanf("%d", &root_val);
root->data=root_val;
//node* temp=getNode();
//temp->data=5;
//root->right=temp;
printf("Root is %d\n",root->data);
for (i=0;i<n;i++)
{
//insert(root,rand()%100);
//}
//printTree(root);
	node* newNode = getNode();
	newNode->data=rand()%100;
	printf("--input %i--- %d\n",i+1,newNode->data);
	insertRecursive(root, newNode);
	
}
printf("--Result of print tree is-----\n");
printTree(root);
printf("\n");
//validateBST(root);
find_min();
kthlargest(root,9);
printf("---level order traversal---\n");
level_orderTraversal();
succ=inorder_successor(root->left->left);
printf("\n%d",succ);
printf("least common ancestor is %d",LCA(45, 56));
return 0;
}
