##find the kth largest element

class Node:
	def __init__(self, data):
		self.data=data
		self.leftChild=None
		self.rightChild=None
		
	def setData(self,value):
		node.data=value
		
	def getData(self):
		return self.data
		
	def getRightChild(self):
		return self.rightChild
	
	def getLeftChild(self):
		return self.leftChild
		
	def setLeftChild(self, value):
		self.leftChild=value
		
	def setRightChild(self, value):
		self.rightChild=value
		
def insert(root, node):
	if root.getData()==None:
		root=node
		return 
	if node.getData() > root.getData():
		##insert at rightChild
		if root.getRightChild()==None:
			root.setRightChild(node)
		else:
			insert(root.rightChild, node)
	else:
		##insert at leftChild
		if root.getLeftChild()==None:
			root.setLeftChild(node)
		else:
			insert(root.leftChild,node)
	return 
count=0
def printtreeInorder(root):
	global count
	if root:
		count+=1
		printtreeInorder(root.getLeftChild())
		print(root.getData(),end=' ')
		printtreeInorder(root.getRightChild())
	return count
no_elem=0
def kthlargest(root, k):
	global no_elem
	if no_elem>k or not root:
		return 
	kthlargest(root.getRightChild(),k)
	no_elem+=1
	if no_elem==k:
		print (k,"largest element is ",root.getData())
	kthlargest(root.getLeftChild(),k)
	return 
	
	
def Driver():
	root=Node(10)
	insert(root, Node(12))
	insert(root, Node(15))
	insert(root, Node(2))
	insert(root, Node(7))
	insert(root, Node(9))
	insert(root, Node(17))
	print ("\n","Total Count is", printtreeInorder(root))
	kthlargest(root, 5)
Driver()
	
