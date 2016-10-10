##EUCLIDS ALGO TO FIND GCD
##O(n)

def gcd(a,b):
	while a%b !=0: 
		old_a=a  
		old_b=b
		
		a=old_b
		b=old_a%old_b
	return b
	
print (gcd(30,12))
