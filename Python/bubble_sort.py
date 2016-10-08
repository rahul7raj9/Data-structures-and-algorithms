##BUBBLE SORT - 
##TC o(n^2)
##SC o(1)

import random
def swap(a,b):
	a=a+b
	b=a-b
	a=a-b
	return a,b
def bubble_sort(lst):
	n=len(lst)
	for i in range(n):
		for j in range(n-i-1):
			if lst[j]>lst[j+1]:
				lst[j],lst[j+1]=swap(lst[j],lst[j+1])
	return lst
			

random.seed()
lst = random.sample(range(1,100), 25)

print ("input List:",lst)
lst=bubble_sort(lst)
print ("Output list:", lst)
