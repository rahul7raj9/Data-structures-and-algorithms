##PALINDROME 

def is_palindrome(in_str):
	bool_is_palindrome=True
	clean_str=''
	for c in in_str.lower():
		if c.isalnum():
			clean_str+=c
	ptr1=0
	n=len(clean_str)
	ptr2=n
	
	for i in range((n//2)):
		if clean_str[i]!=clean_str[n-i-1]:
			bool_is_palindrome=False
			break
	return bool_is_palindrome
print (is_palindrome('Go hang a salami; I’m a lasagna hog'))
print(is_palindrome("madam i'm adam"))
print(is_palindrome("Rahul Raj"))
