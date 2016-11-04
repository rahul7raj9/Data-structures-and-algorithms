##Algorithm to move all zeros to the back of a array


def moveZerosBack(lst):
	n=len(lst)
	count=0
	for i in range(len(lst)):
		if lst[i]!=0:
			lst[count]=lst[i]
			count+=1
	while(count<n):
		lst[count]=0
		count+=1
			
	print (lst)
	
moveZerosBack([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0])
		
