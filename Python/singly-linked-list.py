class Node:
	def __init__(self, value):
		self.data=value
		self.next=None
		
	def getValue(self):
		return self.data
		
	def setValue(self, value):
		self.data=value
		
	def setNext(self, next):
		self.next=next
		
	def getNext(self):
		return self.next
		
def insertFront(head, value):
	newNode=Node(value)
	newNode.setNext(head)
	first=newNode
	return first

def insertBack(head, value):
	first=head
	if first:
		while (first.getNext()!=None):
			first=first.getNext()
		newNode=Node(value)
		first.setNext(newNode)
	else:
		newNode=Node(value)
		head=newNode
	return head
	
def deleteBack(head):
	first=head
	if not first:
		return None
	else:
		while (first.getNext().getNext()!=None):
			first=first.getNext()
		print ("Value Deleted from back is", first.getNext().getValue())
		first.setNext(None)
	return head
		
def deleteFront(head):
	value=head.getValue()
	head=head.getNext()
	print ("Value Deleted from front is", value)
	return head

def size(head):
	first=head
	count=0
	if first:
		while (first.getNext()!=None):
			first=first.getNext()
			count+=1
		print ("Total  nodes in linked list is ", count+1)
		return count+1
	else:
		print ("Empty list")
		return 0

##TODO 
##insert after some data
##loop detection
##delete at a position
def deletePosition(head, pos):
	first=head
	pos_count=1
	if size(first)<pos:
		print ("size of the linked list is smaller than the position specified.")
		return
	elif first:
		while pos_count<pos-1:
			pos_count+=1
			first=first.getNext()
		print ("value deleted from position ",pos,"is", first.getNext().getValue())
		first.setNext(first.getNext().getNext())
		
	return head

##delete by value
def deleteValue(head, value):
	first=head
	found=False
	pos_count=1
	if first:
		first_data=first.getValue()
		if first_data==value:
			return deleteFront(head)
		while first.getNext()!=None:
			if first.getNext().getValue()!=value:
				pos_count+=1
				first=first.getNext()
			else:
				found=True
				break
		if found:
			print (first.getNext().getValue(), "deleted from position", pos_count+1)
			first.setNext(first.getNext().getNext())
		else:
			print ("Val not found")
	else:
		print ("List is empty")
	return head

##Remove duplicates frm unsorted linked List
def removeDup(head):
	first=head
	while first.getNext() != None:
		second=first.getNext()
		while second.getNext() !=None:
			if first.getValue() == second.getNext().getValue():
				head=deleteValue(head, first.getValue())
			second=second.getNext()
		first=first.getNext()
	return head
def insertPosition(head, value, pos):
	first=head
	pos=pos-1
	pos_count=1
	if size(first)<pos:
		print ("size of the linked list is smaller than the position specified.")
		return
	elif first:
		while pos_count<pos:
			pos_count+=1
			first=first.getNext()
		else:
			next=first.getNext()
			newNode=Node(value)
			first.setNext(newNode)
			newNode.setNext(next)
			print ("value inserted at position", pos+1, "is", newNode.getValue())
		return head
		
		
def printListRecursive(node):
	if node != None:
		print (node.getValue())
		printList(node.getNext())
		
		
		
def printList(node):
	while node != None:
		print (node.getValue())
		node=node.getNext()

def driver():
	node=Node(10)
	node=insertFront(node, 5)
	node=insertFront(node, 15)
	node=insertFront(node, 25)
	node=insertFront(node, 17)
	node=insertFront(node, 19)
	node=insertFront(node, 22)
	#node=deleteFront(node)
	size(node)
	node=insertFront(node, 35)
	node=insertBack(node, 25)
	#node=insertPosition(node, 16, 4)
	#node=deleteBack(node)
	size(node)
	print ("-----ITERATIVE-----")
	#printList(node)
	#print ("----RECURSIVE------")
	#printListRecursive(node)
	#node=insertPosition(node, 12, 3)
	node=insertPosition(node, 16, 7)
	node=insertPosition(node, 1, 4)
	printList(node)
	deletePosition(node, 2)
	deletePosition(node, 17)
	print ("-----ITERATIVE-----")
	printList(node)
	deleteValue(node, 35)
	deleteValue(node, 99)
	print ("--------After Insertion and deletion-------")
	printList(node)
	print ("---------REMOVE DUP---------")
	node=removeDup(node)
	printList(node)
	
	
driver()
	
		
