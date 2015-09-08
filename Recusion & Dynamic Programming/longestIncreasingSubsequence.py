''' takes an array of integers and returns the longest strictly increasing subsequence
	ie: [1,2,5,1,3,4] --> [1,2,3,4]	'''

def LIS(arr):

	subs = [[]]*(len(arr)+1) 	# keep track of increasing subsequences
	ends = [0]*(len(arr)+1) 	# keep track of the last value (ie: largest) of each sequence
	# Note: we wont use index 0 so the index of the array can conveniently 
	# correspond to the length of the subsequance
	maxLen = 0

	for num in arr:
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

arr1 = [1]
arr2 = [1,2,3]
arr3 = [3,2,1]
arr4 = [1,2,3,1,0,1,6,1,2,4,5]
arr5 = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

print(LIS(arr5)))


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


