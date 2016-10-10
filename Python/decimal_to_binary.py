##DEC TO BIN
##O(n)

def dectoBin(num):
	stack=[]
	while(num>0):
		bin=num%2
		num=num//2 ##returns int 
		stack.append(str(bin))
	return (''.join(stack[::-1]))
print (dectoBin(100))
