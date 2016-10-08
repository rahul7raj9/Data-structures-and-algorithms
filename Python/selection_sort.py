##BUBBLE SORT, INSERTION SORT and SELECTION SORT
##TC o(n^2)
##SC o(1)

import random
def selection_sort(lst):
	n=len(lst)
	for i in range(n):
		min_indx=i
		for j in range(i+1,n):
			if lst[min_indx]>lst[j]:
				min_indx=j
		##swap
		lst[i],lst[min_indx]=lst[min_indx],lst[i]
	return lst
random.seed()
lst = random.sample(range(1,100), 25)

print ("input List:",lst)
lst=selection_sort(lst)
print ("Output list:", lst)
