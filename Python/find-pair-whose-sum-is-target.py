
import random 
import time
target = 50
num_lst=random.sample(range(1,100), 25)

##SOLUTION 1. Complexity o(n^2) -- Bad choice
def is_pair_1(num_lst, target):
	for i in range(len(num_lst)):
		for j in range(len(num_lst)):
			if i!=j and num_lst[i]+num_lst[j]==target:
				print (num_lst[i],'and',num_lst[j],"sums up to the target value of",target)
				return True
	return False

##SOLUTION 2:again o(n^2) worst case.
def is_pair_2(num_lst, target):
	i=0
	while i!=len(num_lst):
		num_1=num_lst[i]
		to_find=target-num_1
		if to_find in num_lst and num_lst.index(to_find)!=i: ##Time complexity of in is o(n) - 
			print (num_1,'and',to_find,"sums up to the target value of",target)
			return True
		i+=1
	else:
		return False
	
##SOLUTION 3: Using hash maps complexity o(n)
def is_pair_3(num_lst, target):
    arr_size=len(num_lst)
    ##Initialize a binary map
    binmap = [0]*10000
    for i in range(0,arr_size):
        temp = (target - num_lst[i])
        if (temp>=0 and binmap[temp]==1):
            print ("Pair with the given sum is", num_lst[i], "and", temp)
        binmap[num_lst[i]]=1

##SOLUTION 4
def is_pair(in_lst, target):
	in_dict={}
	bool_is_pair=False
	for i in range(len(in_lst)):
		in_dict[in_lst[i]]=None
	i=0
	while i<=len(in_dict)-1:
		if (target-list(in_dict.keys())[i]) in in_dict.keys():
			bool_is_pair=True
			print(list(in_dict.keys())[i],"and",target-list(in_dict.keys())[i], "Will sum up to", target)
		i+=1
	else:
		return bool_is_pair
		
print ("\n---------METHOD 1 -----------------\n")
start=time.time()	
print (is_pair_1(num_lst, target), "using method 1..!!")
end=time.time()
print ("Time taken using method 1 is ",end-start)
print ("\n---------METHOD 2 -----------------\n")
start=time.time()	
print (is_pair_2(num_lst, target), "using method 2..!!")
end=time.time()
print ("Time taken using method 2 is ",end-start)
print ("\n---------METHOD 3 -----------------\n")
start=time.time()	
is_pair_3(num_lst, target)	
end=time.time()
print ("Time taken using method 3 is ",end-start)
print ("\n---------METHOD 4 -----------------\n")
start=time.time()
print (is_pair(in_lst, target))
end=time.time()
print ("Time taken using method 4 is ",end-start)
