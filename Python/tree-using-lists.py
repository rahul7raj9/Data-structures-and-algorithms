##TREE USING LISTS OF LIST
##LIST AS TREES
##STRUCTURE OF A LIST DEFINED FOR SUB ADHERES TO THE SRTUCTURE DEFINED FOR A TREE
##CAN BE EASILY ENTENDED FOR MORE THAN A BINARY TREE.

def BinaryTree(root):
	return [root,[],[]] ##CONSTRUCTS THE ROOT WITH 2 EMPTY SUBLIST FOR CHILDRENS
	
def insertLeft(root, newNode):
	temp=root.pop(1)
	if len(temp)>1:
		root.insert(1,[newNode, temp, []])
	else:
		root.insert(1,[newNode,[],[]])
	return root
	
def insertRight(root, newNode):
	temp=root.pop(2)
	if len(temp)>1:
		root.insert(2,[newNode, [], temp])
	else:
		root.insert(2,[newNode,[],[]])
	return root
	
def getRoot(root):
	return root[0]
	
def setRoot(root, value):
	root[0]=value
	
def getRightChild(root):
	return root[2]
	
def getLeftChild(root):
	return root[1]
	
Tree = BinaryTree(3)
insertLeft(Tree,4)
insertLeft(Tree,5)
insertRight(Tree,6)
insertRight(Tree,7)
child = getLeftChild(Tree)
print(child)
setRoot(child,9)
print(Tree)
insertLeft(child,11)
print(Tree)
print(getRightChild(getRightChild(Tree)))
