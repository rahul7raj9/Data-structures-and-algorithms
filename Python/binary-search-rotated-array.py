##complexity is o(logn)

def search_rotated(lst, key, low, high):
	mid=(low+high)//2
	if key==lst[0]:
		print ("found at first position")
		return
	if lst[mid]==key:
		print ("found at position ", mid)
		return
	elif (lst[low]<=lst[mid]):##low to mid is sorted
		if key>=lst[low] and key<=lst[mid]:
			return search_rotated(lst, key, low, mid-1)
		else:
			return search_rotated(lst, key, mid+1, high)
		
	##if low to mid is not sorted then mid to high will be sorted
	elif key>=lst[mid] and key<=lst[high]:
		return search_rotated(lst, key, mid+1, high)
	else:
		try:
			return search_rotated(lst, key, low, mid-1)
		except:
			print ("not found")
			
lst=[2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
search_rotated(lst, 0, 0, len(lst)-1) ##does not work for duplicates. FIXME
search_rotated([50,56,59,7,11,12,17,45], 59, 0, 7) ##works fine for such cases.
