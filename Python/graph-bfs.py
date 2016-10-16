##GRAPHS
##tree is coneected graph without loops
##Adjacency list
##Adjacency matrix

##DFS 

class Vertex:
	def __init__(self, name):
		self.name=name
		self.distance=0  ##for BFS
		self.predecessor=None
		self.color='white'
		self.discovery=0  ##for DFS
		self.finish=0 ##for DFS
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
		
	def setDiscovery(self, value):
		self.discovery=value
		
	def getDiscovery(self):
		return self.discovery
	
	def setFinish(self, value):
		self.finish=value
		
	def getFinish(self):
		return self.finish
	
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
    
class dfsGraph(Graph):
	def __init__(self):
		super().__init__()
		self.time=0
		
	##set all the nodes to white and predecessors to -1
	##for each vertex call dfsvist
	def dfs(self):
		for vertex in self.vertexList.values():
			vertex.setColor('white')
			#print (vertex.getName())
			vertex.setPredecessor(-1)
			
		for vertex in self.vertexList.values():
			if vertex.getColor()=='white':
				self.dfsvisit(vertex)
	
	##set the color to grey
	##increment time and set discovery time
	##for each neighbors of the vertex if color is white
	##set predecessor
	##call dfs visit again
	##once done set the color to Black
	##increment time and setFinish
	
	def dfsvisit(self, vertex):
		self.time+=1
		vertex.setColor('Gray')
		vertex.setDiscovery(self.time)
		print (vertex.getName())
		for nbr in vertex.getNeighbors():
			if nbr.getColor()=='white':
				nbr.setPredecessor(vertex)
				self.dfsvisit(nbr)
		vertex.setColor('Black')
		self.time+=1
		vertex.setFinish(self.time)
				
def dfsvisit_path(graph, start,finish, path_lst):
	start.setColor('Gray')
	finish_found=False
	nbr_lst=list(start.getNeighbors())
	[print (nbr.getName()) for nbr in nbr_lst]
	for nbr in nbr_lst:
		if nbr.getColor()=='white':
			if nbr.getName()!=finish.getName():
				nbr.setPredecessor(start)
				path_lst.append(nbr.getName())
				return dfsvisit_path(graph, nbr,finish,path_lst)
			else:
				path_lst.append(nbr.getName())
				print ("Found!! The path is",' -> '.join(path_lst))
				[vertex.setColor('white') for vertex in graph.vertexList.values()]
				return dfsvisit_path(graph, nbr_lst.pop(0),finish,path_lst=[])
	start.setColor('Black')
	print ("Not found")
	
		
def findPath(graph, start, finish):
	path_lst=[]
	[vertex.setColor('white') for vertex in graph.vertexList.values()]
	if start not in graph.vertexList.values():
		print ("start not found in graph")
		return
	elif finish not in graph.vertexList.values():
		print ("finish not found in graph")
		return
	else:
		path_lst.append(start.getName())
		dfsvisit_path(graph, start,finish, path_lst)
		
		
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
	graph=dfsGraph()
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
	print ("-----------BFS Graph traversal------------")
	traverse(graph.getVertex('E'))
	traverse(graph.getVertex('o'))
	print ("---------DFS-----------")
	g = dfsGraph()
	two=g.addVertex('2')
	zero=g.addVertex('0')
	one=g.addVertex('1')
	three=g.addVertex('3')
	#e = g.addVertex('e')
	g.addEdge('0','1',0)
	g.addEdge('0','2',5)
	g.addEdge('1','2',7)
	g.addEdge('2','0',10)
	g.addEdge('2','3',10)
	g.addEdge('3','3',10)
	g.dfsvisit(zero)
	#findPath(g,zero,two)
	#findPath(g,zero,three)
	#findPath(g,three,one)
	
	
Driver()
			
		
		
		
	

