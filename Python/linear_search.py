import random 
num = 80
random.seed()
lst=(random.sample(range(1,100),50)) ##Generate a random list
#lst=[1,2,3,4,5,6,86,84,80,54] ##or have your own list
#lst=list(map(int, input().split(' '))) ##or ask for lst value as the input from the user space seperated
#print (lst)
for i in range(len(lst)):
	if num==lst[i]:
		print ("Found")
		break
else:
	print ("Not Found")

##TC - o(n)
##SC - o(1)
