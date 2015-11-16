''' given an unsorted subarray, find the shortest contiguous array that sums to greater or equal to the target '''

''' buggy solutions but the general idea is there xD '''

''' bad brute force O(n^3) '''
def badBrute(arr,target):

	best = [0]*(len(arr)+1)

	for i in range(len(arr)):
		for j in range(i,len(arr)+1):
			if sum(arr[i:j]) >= target and len(arr[i:j]) < len(best):
				best = arr[i:j]

	return best

''' good brute force O(n^2) -semi-dp '''
def goodBrute(arr,target):

	best = [0]*(len(arr)+1)

	subSum = sum(arr)
	for i in range(len(arr)):
		temp = subSum
		if temp < target:
			break

		for j in range(i,len(arr))[::-1]:
			temp -= arr[j]
			# print(arr[i:j])
			if temp >= target and len(arr[i:j]) < len(best):
				best = arr[i:j]
			# else:
			# 	if temp < target:
			# 		break
		subSum -= arr[i]

	return best

''' good dp algorithm O(n). Uses the fact that any better result will be shorter than current best,
so resize the rolling "scanning window" '''

def dp(arr, target):

	best = [0]*(len(arr)+1)
	j = 0	# end index
	windowSize = 0

	# first find the smallest array starting from index 0 whose sums >= target
	subSum = 0
	for k in range(len(arr)):
		subSum += arr[k]
		if subSum >= target:
			best = arr[:k+1]
			j = k
			windowSize = k+1
			break

	i = 1	# start index
	while i + windowSize-1 < len(arr):
		j = i + windowSize-1

		subSum += arr[j]-arr[i-1]
		if subSum < target:
			i+=1
			continue
		else:
			while i <= j:
				if subSum - arr[i] >= target:
					subSum -= arr[i]
					i += 1
				else:
					windowSize = j-i+1
					if len(arr[i:j+1]) < len(best): # keep the earlier array
						best = arr[i:j+1]
					break
			i += 1

	return best
	

from random import randint
def genArr(num):
	return [randint(0,max(9,num//10)) for x in range(num)]

test = [4,2,6,8,2,1,8,1,0,4,5,7,4,0,4,6,3,5,7,2,0,1,8]
test1 = genArr(40)
target = 120

print(test1)
print(badBrute(test1,target))
# print(goodBrute(test1,target))
print(dp(test1,target))
