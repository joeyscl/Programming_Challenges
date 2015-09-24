import sys, random
import time
'''given an array of ints representing up-to how many steps you're allowed to jump,
determine the fewest jumps required to reach the very last element from the first'''

''' Recursion + Memoization. !! Blows the stack for input size > 997 !! '''
def fewestJumps_Rec(str):
	mem = {}
	def helper(i):
		if i in mem.keys():
			return mem[i]

		elif i >= len(arr)-1:
			return 0

		else:
			jumps = sys.maxsize
			steps = arr[i]
			for n in range(i+1, i+1+steps):
				jumps = min(jumps, helper(n))
			mem[i] = jumps+1
			return jumps + 1

	arr = [int(num) for num in str]
	return helper(0)


''' DP. Doesn't blow stack!!! Similar performance as Above '''
def fewestJumps_DP1(str):
	arr = [int(num) for num in str]
	jumps = [sys.maxsize]*len(arr)
	jumps[0] = 0

	for i in range(len(arr)):
 		steps = arr[i]
 		for j in range(i+1,i+1+steps):
 			if j < len(arr):
 				jumps[j] = min(jumps[j], jumps[i]+1)
 			else:
 				jumps[-1] = min(jumps[-1], jumps[i]+1)
	return jumps[-1]

''' Even better Algorithm. Improvement is ~proportional with higher average of jumps defined in gen(n) '''
def fewestJumps_DP2(str):
	arr = [int(num) for num in str]
	i = 0
	count = 0
	while i < len(arr):
		steps = arr[i]

		score = 0
		for j in range(i+1,min(i+1+steps,len(arr))):
			if j >= len(arr)-1:
				return count+1
			else:
				if j+arr[j] > score:
					score = j+arr[j]
					i = j
		count += 1
	return count


def gen(n):
	res = []
	b = min(n-1,100)
	for i in range(n):
		res.append(random.randint(1,b))
	return res

# test = gen(500)
# print(test,'\n')
# 
# print(fewestJumps_Rec(test)) #dont do this for input size > 997
# print(fewestJumps_DP1(test))
# print(fewestJumps_DP2(test))

'''Comparing performances'''
Rec = 0
DP1 = 0
DP2 = 0
for T in range(100):
	test = gen(1000)

	# start = time.time()
	# fewestJumps_Rec(test)
	# Rec += (time.time()-start)*1000

	start = time.time()
	fewestJumps_DP1(test)
	DP1 += (time.time()-start)*1000

	start = time.time()
	fewestJumps_DP2(test)
	DP2 += (time.time()-start)*1000
print(DP1/DP2)
