##BINARY SEACRCH
##SC- o(1)
##ASC - o(log n) - for recursive calls to store the value in stack
##ASC - o(1) for iterative solution.
##TC - o(log n)

##the array should be in sorted order.

import random

##APPROACH - 1 RECURSION
##NOT THE BEST AS IT MODIFIES THE ORIGINAL LIST AND ONLY RETURNS TRUE OR FALSE
def binary_search_1(lst, num):
	n=len(lst)
	mid=int((n)/2)
	if n==1:
		if num == lst[0]:
			return 1
		else:
			return 0
	if lst[mid]==num:
		return 1
	elif lst[mid]>num:
		lst=lst[:mid]
		return binary_search(lst, num)
		
	elif lst[mid]<num:
		lst=lst[mid:]
		return binary_search(lst, num)
	else:
		return 0

##APPROACH - 2 RECURSION WITH 2 POINTERS
def binary_search_2(lst, num, left, right):
	if right>=left:
		mid=int(left+(right-left)/2)
		if lst[mid]==num:
			return 1, mid
		elif lst[mid]>num:
			return binary_search_2(lst, num, left, mid-1)
		else:
			return binary_search_2(lst, num, mid+1, right)
	return 0, 0
	
##APPROACH - 3 ITERATIVE WITH 2 POINTERS
def binary_search_3(lst, num, left, right):
	while right>=left:
		mid=int(left+(right-left)/2)
		if lst[mid]==num:
			return 1, mid
		elif lst[mid]>num:
			right=mid-1
		else:
			left=mid+1
	return 0, 0
		
		
###END OF THE FUNCTION DEFINITION##


num= 9
random.seed()
lst = random.sample(range(1,10), 6)
lst=sorted(lst) ##This is TIMSORT algorithm. Hybrid sorting algorithm derived from merge sort and insertion sort. 
##The algorithm finds subsets of the data that are already ordered, and uses the subsets to sort the data more efficiently. This is done by merging an identified subset, called a run, with existing runs until certain criteria are fulfilled.
n=len(lst)
print (lst)
#bool=binary_search_1(lst, num)
#bool, i=binary_search_2(lst, num, 0, n-1)
bool, i=binary_search_3(lst, num, 0, n-1)
if bool:
	print ("Found at ",i)
else:
	print ("Not Found")


	
