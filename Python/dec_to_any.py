##DEC TO ANY

def dectoAny(num, base):
	stack=[]
	digits = "0123456789ABCDEF"
	while(num>0):
		rem=num%base
		num=num//base ##returns int 
		stack.append(str(digits[rem]))
	return (''.join(stack[::-1]))
print (dectoAny(255,16))

