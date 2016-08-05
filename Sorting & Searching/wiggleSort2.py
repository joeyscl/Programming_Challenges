''' given an array of integers (that may have redundant entries), sort the array in O(n) time and O(1) memory
such that A[0] < A[1] > A[2] < A[3]...
There can be redundant entries in the array
'''
from random import randint

def wiggleSort(arr):
	# finds the (k+1)th smallest element in an unsorted array and partitions the array
	def quickSelect(low, hi, k):
		p = randint(low,hi)
		arr[p], arr[hi] = arr[hi], arr[p]
		pivot = arr[hi]

		i = low
		j = hi-1

		while True:
			if i > j:
				break
			else: 
				if arr[i] <= pivot:
					i += 1
				else:
					arr[i], arr[j] = arr[j], arr[i]
					j -= 1

		arr[i], arr[hi] = arr[hi], arr[i]	#swap pivot into place
		if i == k:
			return i
		elif i > k:
			return quickSelect(low, i-1, k)
		else:
			return quickSelect(i+1, hi, k)


	print(arr)
	j = quickSelect(0, len(arr)-1, len(arr)//2) #find the median and partition
	k = arr.index(arr[j])

	median = arr[len(arr)//2]
	print(arr,median)

	i = 0
	up = 0
	down = 1
	
	while i < len(arr):
		# print(i, up, down)
		if arr[i] > median and i%2 == 1:
			arr[i], arr[up] = arr[up], arr[i]
			up += 2
		elif arr[i] < median and i%2 == 0:
			arr[i], arr[down] = arr[down], arr[i]
			down += 2
		elif arr[i] == median:
			pass

		i += 1


	print(arr)

wiggleSort([5,3,2,3,3,1,0,4,3])