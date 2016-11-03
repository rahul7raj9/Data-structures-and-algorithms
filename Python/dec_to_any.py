##DEC TO ANY

def dectoAny(num, base):
	stack=[]
	digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if not 1 < base < 37:
		raise ValueError("base must be between 2 and 36")
	while(num>0):
		rem=num%base
		num=num//base ##returns int 
		stack.append(str(digits[rem]))
	return (''.join(stack[::-1]))
print (dectoAny(61,17))
