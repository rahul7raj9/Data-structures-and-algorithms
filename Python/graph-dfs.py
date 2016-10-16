##GRAPHS
##tree is coneected graph without loops
##Adjacency list
##Adjacency matrix

##DFS 

class Vertex:
	def __init__(self, name):
		self.name=name
		self.distance=0
		self.predecessor=None
		self.color='white'
		self.connectedTo={}
		
	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr]=weight
		
	def getName(self):
		return self.name
		
	def getNeighbors(self):
		return self.connectedTo.keys()
		
	def getWeight(self, nbr):
		return self.connectedTo[nbr]
	
	def getDistance(self):
		return self.distance
	
	def setDistance(self, val):
		self.distance=val
		
	def getColor(self):
		return self.color
	
	def setColor(self, color):
		self.color=color
		
	def getPredecessor(self):
		return self.predecessor
		
	def setPredecessor(self, pred):
		self.predecessor=pred
		
		
	
class Graph:
	def __init__(self):
		self.vertexList={}
		self.numVertex=0
		
	def addVertex(self,name):
		vertex=Vertex(name)
		self.numVertex+=1
		self.vertexList[name]=vertex
		return vertex
	
	def getVertex(self, name):
		if name in self.vertexList.keys():
			return self.vertexList[name]
		else:
			return None
			
	def getAllVertex(self):
		return self.vertexList.keys()
	
	def addEdge(self, srcVertex, destVertex, weight=0):
		if srcVertex not in self.vertexList:
			srcVertex=self.addVertex(srcVertex)
		if destVertex not in self.vertexList:
			srcVertex=self.addVertex(destVertex)
		self.vertexList[srcVertex].addNeighbor(self.vertexList[destVertex], weight)
	
	def AdjacencyList(self, vertex):
		lst=list(self.vertexList[vertex].getNeighbors())
		for i in lst:
			print (vertex, i.getName())
			
def bfs(graph, start):
	queue=[]
	queue.append(start)
	start.setPredecessor(None)
	start.setDistance(0)
	start.setColor('Gray')
	while len(queue)>0:
		#print (queue)
		curr=queue.pop(0)
		for nbr in curr.getNeighbors():
			#print (nbr.getName())
			if nbr.getColor()=='white':
				queue.append(nbr)
				nbr.setColor('Gray')
				nbr.setDistance(curr.getDistance()+1)
				nbr.setPredecessor(curr)
		curr.setColor('Black')
		#print (curr.getColor())
				
def traverse(vertex):
    x = vertex
    try:
    	if x.getPredecessor()!=None:
    		print(x.getName())
    		x = x.getPredecessor()
    		return traverse(x)
    except:
    	print ("value doesn't Exists!!")
    	return
    print(x.getName())
    

	
		
def Driver():
	"""
	graph=Graph()
	graph.addVertex(1)
	graph.addVertex(2)
	graph.addVertex(3)
	graph.addVertex(5)
	graph.addVertex(9)
	graph.addEdge(1,2,0)
	graph.addEdge(1,3,0)
	graph.addEdge(1,5,0)
	graph.addEdge(3,9,0)
	graph.addEdge(3,2,0)
	graph.addEdge(5,3,0)
	graph.AdjacencyList(1)
	graph.AdjacencyList(3)
	graph.AdjacencyList(5)
	"""
	graph=Graph()
	root=graph.addVertex('A')
	graph.addVertex('B')
	graph.addVertex('C')
	graph.addVertex('D')
	last=graph.addVertex('E')
	graph.addEdge('A','B',0)
	graph.addEdge('A','C',0)
	graph.addEdge('B','D',0)
	graph.addEdge('B','E',0)
	print ("----------Adajcency list of A-----")
	graph.AdjacencyList('A')
	print ("----------Adajcency list of B-----")
	graph.AdjacencyList('B')
	bfs(graph, root)
	print ("-----------Graph traversal------------")
	traverse(graph.getVertex('E'))
	traverse(graph.getVertex('o'))

Driver()
			
		
		
		
	

