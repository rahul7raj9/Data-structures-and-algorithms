##GRAPHS
##tree is connected graph without loops
##Adjacency list
##Adjacency matrix
class Vertex:
	def __init__(self, name):
		self.name=name
		self.connectedTo={}
		
	def addNeighbor(self, nbr, weight=0):
		self.connectedTo[nbr]=weight
		
	def getName(self):
		return self.name
		
	def getNeighbors(self):
		return self.connectedTo.keys()
		
	def getWeight(self, nbr):
		return self.connectedTo[nbr]
		
	
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
		
def Driver():
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
Driver()
			
		
		
		
	

