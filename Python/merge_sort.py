##MERGE SORT - Divide and Conquer, Recursive method.
##TC o(n log n)
##SC o(n)

import random

def merge_sort(lst):
	i=0
	j=0
	k=0
	if len(lst)>1:
		mid=int(len(lst)/2)
		lefthalf=lst[:mid] ##use index instead of this as it is o(k) TC. 
		righthalf=lst[mid:]
		merge_sort(lefthalf)
		merge_sort(righthalf)
		#print (lefthalf)
		#print (righthalf)
		##we will get the list with 1 element each.
		##merging starts here..
		while i<len(lefthalf) and j<len(righthalf):
			if(lefthalf[i]>righthalf[j]):
				lst[k]=righthalf[j]
				j=j+1
			else:
				lst[k]=lefthalf[i]
				i=i+1
			k=k+1
			
	  
		while(i<len(lefthalf)):
			lst[k]=lefthalf[i]
			i+=1
			k=k+1
		while(j<len(righthalf)):
			lst[k]=righthalf[j]
			j=j+1
			k=k+1
	print ("Merging.. ", lst)
	return lst
				

		
random.seed()
lst = random.sample(range(1,100), 25)
print ("input List:",lst)
lst=merge_sort(lst)
print ("Output list:", lst)
