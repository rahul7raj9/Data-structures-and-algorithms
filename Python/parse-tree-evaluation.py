##parse tree evaluation
##
import operator
class binaryTree:
	def __init__(self, node):
		self.node=node
		self.left=None
		self.right=None
	def setNode(self, value):
		self.node=value
	def getNode(self):
		return self.node
	def getLeftChild(self):
		return self.left
	def getRightChild(self):
		return self.right
	def insertLeft(self, newNode):
		if self.left==None:
			tree=binaryTree(newNode)
			self.left=tree
		else:
			tree=binaryTree(newNode)
			tree.left=self.left
			self.left=tree
	def insertRight(self, newNode):
		if self.left==None:
			tree=binaryTree(newNode)
			self.right=tree
		else:
			tree=binaryTree(newNode)
			tree.right=self.right
			self.right=tree

def printTree_inorder(tree):
	if tree!=None:
		printTree_inorder(tree.getLeftChild())
		print(tree.getNode())
		printTree_inorder(tree.getRightChild())

def printTree_preorder(tree):
	if tree!=None:
		print(tree.getNode())
		printTree_preorder(tree.getLeftChild())
		printTree_preorder(tree.getRightChild())
		

def printTree_postorder(tree):
	if tree!=None:
		printTree_postorder(tree.getLeftChild())
		printTree_postorder(tree.getRightChild())
		print(tree.getNode())
		
def buildParseTree(exp):
	stack=[]
	current=binaryTree('')
	stack.append(current)
	for i in exp:
		if i=='(':
			current.insertLeft('')
			stack.append(current)
			current=current.getLeftChild()
		elif i.isalnum():
			current.setNode(int(i))
			parent=stack.pop()
			current=parent
		elif i in ['+','*','/','-']:
			current.setNode(i)
			current.insertRight('')
			stack.append(current)
			current=current.getRightChild()
		elif i == ')':
			current=stack.pop()
		else:
			raise ValueError
	return current
def evaluate(tree):
	op_dict={'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
	leftChild=tree.getLeftChild()
	rightChild=tree.getRightChild()
	if leftChild and rightChild:
		op=op_dict[tree.getNode()]
		return (op(evaluate(leftChild), evaluate(rightChild)))
	else:
		return tree.getNode()
		
exp='(3+(4*5))'
parse_tree=buildParseTree(exp)	
print ("The result of the expression is ",evaluate(parse_tree), '\n')
print ("------------INORDER-------------")
printTree_inorder(parse_tree)
print ("------------PREORDER-------------")
printTree_preorder(parse_tree)
print ("------------POSTORDER-------------")
printTree_postorder(parse_tree)
