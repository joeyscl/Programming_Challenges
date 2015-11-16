''' given a min heap, find the Kth smallest element '''

from heapq import *
from math import *
from random import randint

''' use built-in heap module '''
def findKth1(heap, k):
	for i in range(k-1):
		heappop(heap)
	return (heappop(heap))

''' use quickselect with minor optimization in search range '''
def findKth2(heap, k):

	def findLower(k):
		# find the level that contains kth elements, then return the index of the 1st element of that level
		level = int(log2(k))
		return 2**level -1

	def findUpper(k):
		# find the index of the last element at the Kth level
		level = k
		return min(2** level -1, len(heap)-1)

	def qselect(arr, n):
		# find nth smallest element
		pivotIdx = randint(0,len(arr)-1)
		pivotVal = arr[pivotIdx]
		arr[pivotIdx], arr[-1] = arr[-1], arr[pivotIdx]

		lessThan = [num for num in arr[:-1] if num <= pivotVal]
		greaterThan = [num for num in arr[:-1] if num > pivotVal]

		# arr = lessThan + [pivotVal] + greaterThan

		if len(lessThan) == n-1:
			return pivotVal
		elif len(lessThan) > n-1:
			return qselect(lessThan, n)
		else:
			return qselect(greaterThan, n-1-len(lessThan))

	if k > len(heap):
		print ("invalid input")
		return None
	else:
		lower = findLower(k)
		upper = findUpper(k)
		return qselect(heap[lower:upper+1], k-lower)

test = [6,7,9,2,5,0,3,1,8,4]
heapify(test)
print(test)
print(sorted(test))
print(findKth2(test, 5))

print(findKth1(test,5))