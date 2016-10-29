def partition(lst, start, end):
	pivot=lst[start]
	left=start+1
	right=end
	done = False
	while (not done):
		while(pivot>=lst[left] and left<=right):
			left+=1
		while(pivot <= lst[right] and left<=right):
			right-=1
		if right < left:
			done=True
		else:
			lst[left],lst[right]=lst[right], lst[left]
	lst[start],lst[right]=lst[right], lst[start]
	return right
	
	
def q_sort(lst, start, end):
	if (end>start):
		split=partition(lst, start, end)
		q_sort(lst, start, split-1)
		q_sort(lst, split+1, end)
	return lst
	
print(q_sort([4,1,2,5,4,7,6,9],0,7))	
				
