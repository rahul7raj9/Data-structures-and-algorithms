##PALINDROME RECURSIVE

def is_palindrome(in_str):
	bool_is_palindrome=False
	if len(in_str)==1 or len(in_str)==0:
		bool_is_palindrome=True
		return bool_is_palindrome
	else:
		if in_str[0]==in_str[len(in_str)-1]:
			return is_palindrome(in_str[1:len(in_str)-1])
		else:
			return bool_is_palindrome
			
	#return bool_is_palindrome
print (is_palindrome(('Go hang a salami; I’m a lasagna hog').lower()))
print(is_palindrome(("madam i'm adam").lower()))
print(is_palindrome(("Rahul Raj").lower()))
print (is_palindrome(("Kayak").lower()))
