##Reverse String Recursive

rev_str=''
def find_reverse(in_str):
	global rev_str
	n=len(in_str)
	#print (n, in_str, rev_str)
	if n==1:
		rev_str+=in_str[0]
		print (rev_str)
		rev_str=''
	else:
		rev_str+=in_str[n-1]
		return find_reverse(in_str[:n-1])
	
	
find_reverse('rahul raj')
find_reverse("madam I'm adam")
find_reverse('kayak')

