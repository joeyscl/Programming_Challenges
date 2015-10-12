import random

''' online version of the LIS problem'''
''' takes a num and create an iterator for random ints
	takes that iterator and returns the longest strictly increasing subsequence
	ie: [1,2,5,1,3,4] --> [1,2,3,4]	'''

def LIS(num):

	subs = [[]]*(num+1) 	# keep track of increasing subsequences
	ends = [0]*(num+1) 	# keep track of the last value (ie: largest) of each sequence
	# Note: we wont use index 0 so the index of the array can conveniently 
	# correspond to the length of the subsequance
	maxLen = 0

	gen = intsGen(num)	# creating our problem
	for num in gen:
		if len(subs[1]) == 0: 
			maxLen = 1
			subs[1] = [num]
			ends[1] = num

		elif num < subs[1][-1]:
			subs[1] = [num]
			ends[1] = num

		elif num > subs[maxLen][-1]:
			subs[maxLen+1] = subs[maxLen]+[num]
			ends[maxLen+1] = num
			maxLen += 1

		else:
			newSubLen = binSearchModified(ends[:maxLen+1],num)	# the len of the first sequence that has end >= num
			newSub = subs[newSubLen]		# get the first sequence that has end >= num

			if newSub[-1] < num:
				newSub = newSub + [num]
				newSubLen += 1
				subs[newSubLen] = newSub
				ends[newSubLen] = num

	# get the longest sequence
	return subs[maxLen]

'''returns index of the greatest value <= num in a given sorted array'''
'''using this will result in O(n Log n) '''
def binSearchModified(arr, num):
	lo = 0
	hi = len(arr)-1
	mid = (hi-lo)//2

	while True:
		if num == arr[mid] or hi-lo <= 1:
			# print(mid)
			return mid

		elif num < arr[mid]:
			hi = mid
			mid = (hi+lo)//2

		else:
			lo = mid
			mid = (hi+lo)//2

'''returns index of the greatest value <= num in a given sorted array'''
'''using this will result in O(n^2) '''
def linSearchModified(arr, num): 

	for i in range(len(arr)):
		if arr[i] == num:
			return i
		elif arr[i] > num:
			return i-1

'''returns an num-sized iterator of randomly generated ints'''
def intsGen(num):
	for i in range(num):
		yield random.randint(0,num)

print(len(LIS(10000)))



'''
12310161245

1

1
12

1
12
123

1
12
123

0
12
123

0
01
123

0					12310161245
01
1236

0
01
1236

0
01
012
1236

0
01
012
0124

0
01
012
0124
01245

					12310161245
'''


