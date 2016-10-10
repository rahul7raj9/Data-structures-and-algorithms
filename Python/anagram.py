##ANAGRAM- O(n) solution

def is_anagram(a,b):
	count_a=[0]*26
	count_b=[0]*26
	for i in range(len(a)):
		indx=ord(a[i])-ord('a')
		count_a[indx]+=1
	for i in range(len(b)):
		indx=ord(b[i])-ord('a')
		count_b[indx]+=1
	bool_is_anagram=True
	j=0
	while j<26 and bool_is_anagram:
		if (count_a[j]==count_b[j]):
			j+=1
		else:
			bool_is_anagram=False
			
	return bool_is_anagram
		
		
print (is_anagram('rahul','luhar'))  ##True
print (is_anagram('rahulajar','luharraj')) ##Fasle
print (is_anagram('rahulraj','luharraj')) ##True
print (is_anagram('rahul','luhaar')) ##False
