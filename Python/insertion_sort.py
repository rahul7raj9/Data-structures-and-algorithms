import random

	
def insertion_sort(lst):
	n=len(lst)
	for i in range(1,n):
		first=lst[i]
		j=i-1
		while j>=0 and first<lst[j]:
			lst[j+1]=lst[j]
			j-=1
		lst[j+1]=first
	return lst
		
random.seed()
lst = random.sample(range(1,100), 25)

print ("input List:",lst)
lst=insertion_sort(lst)
print ("Output list:", lst)
