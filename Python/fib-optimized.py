##Memoized solution##O(n) solution. there exists an o(logn) solution.
import time
memo={}
def fib_1(n):
	if n in memo:
		return memo[n]
	if n<=2:
		memo[n]=1
		return 1
	else:
		f=fib_1(n-1)+fib_1(n-2)
		memo[n]=f
		return f
	
def fib_2(n):
	if n<=2:
		return 1
	else:
		return fib_2(n-1)+fib_2(n-2)

start = time.time()
print (fib_1(200))
end=time.time()
print ("Using method 1..", (end-start)*1000, "seconds")
start = time.time()
print (fib_2(200))
end=time.time()
print ("Using method 2..", (end-start)*1000, "seconds")
