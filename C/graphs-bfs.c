//BFS/////////////
/////////////////
#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>


#define MAX 6
//define the vertex structure
typedef struct Vertex{
char name;
bool visited;
}vertex;


//////////////////////////////////////////
//setup the queue to be used for BFS
//////////////////////////////////////////
int queue[MAX];
int rear = -1;
int front = 0;
int items = 0;

void insert(int data)
{
queue[++rear]=data;
items+=1;
}

int remove_ele()
{
items-=1;
return queue[front++];
}

bool isQueueEmpty()
{
return items==0;
}
////////////////////////////////////
/////////////////////////////////////


//graph functions and variables

vertex* lstVertex[MAX];
int adjMatrix[MAX][MAX];
int vertexCount=0;

void addVertex(char name){
vertex* newVertex = (vertex *)(malloc(sizeof(vertex)));
assert(newVertex!=NULL);
newVertex->name=name;
newVertex->visited=false;
lstVertex[vertexCount++]=newVertex;
}

void addEdge(int start, int end){
adjMatrix[start][end]=1;
adjMatrix[end][start]=1;
}


void displayVertex(int vertexIndex){
printf("%c", lstVertex[vertexIndex]->name);
}

int getUnvisitedVertex(int vertexIndex){
int i;
for(i=0;i<vertexCount;i++){
	if(adjMatrix[vertexIndex][i]==1 && lstVertex[i]->visited==false)
	return i;
}
return -1;
}

void bfs(){
int i;

//mark first node as visited
lstVertex[0]->visited=true;
displayVertex(0);
insert(0);
int unvisitedVertex;

while(!isQueueEmpty())
	{
	int currVertex=remove_ele();
	while((unvisitedVertex=getUnvisitedVertex(currVertex))!=-1)
		{
		lstVertex[unvisitedVertex]->visited=true;
		displayVertex(unvisitedVertex);
		insert(unvisitedVertex);
		}
	
	}
	//reset the visited flag
	for(i=0;i<vertexCount;i++)
		lstVertex[i]->visited=false;
}
int main() {
   int i, j;

   for(i = 0; i<MAX; i++){ // set adjacency 
      for(j = 0; j<MAX; j++) // matrix to 0
         adjMatrix[i][j] = 0;
   }

   addVertex('S');   // 0
   addVertex('A');   // 1
   addVertex('B');   // 2
   addVertex('C');   // 3
   addVertex('D');   // 4
   addVertex('E');
   addEdge(0, 1);    // S - A
   addEdge(0, 2);    // S - B
   addEdge(0, 3);    // S - C
   addEdge(1, 4);    // A - D
   addEdge(2, 4);    // B - D
   addEdge(3, 4);    // C - D
   printf("\nBreadth First Search: ");
   bfs();
   return 0;
}

