from random import randint
from copy import deepcopy
def qselect1(arr,k):
	if k > len(arr):
		print('invalid inputs')
		return None

	k -= 1 # we want to find the Kth low element, not element at Kth index

	def qs(low, hi):		
		temp = randint(low,hi)
		arr[temp], arr[hi] = arr[hi], arr[temp]
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

		arr[hi], arr[i] = arr[i], arr[hi]
		print(arr)
		if i == k:
			return arr[i]
		elif i > k:
			return qs(low,i-1)
		else:
			return qs(i+1,hi)

	return qs(0,len(arr)-1)

def qselect2(arr, n):
	if n > len(arr):
		print('invalid inputs')
		return None

	# find nth smallest element
	pivotIdx = randint(0,len(arr)-1)
	pivotVal = arr[pivotIdx]
	arr[pivotIdx], arr[-1] = arr[-1], arr[pivotIdx]

	lessThan = [num for num in arr[:-1] if num <= pivotVal]
	greaterThan = [num for num in arr[:-1] if num > pivotVal]

	# arr = lessThan + [pivotVal] + greaterThan
	print(arr)

	if len(lessThan) == n-1:
		return pivotVal
	elif len(lessThan) > n-1:
		return qselect2(lessThan, n)
	else:
		return qselect2(greaterThan, n-1-len(lessThan))

test = [6,7,9,2,5,0,3,1,8,4]
print(qselect1(deepcopy(test),6))
print('')
print(qselect2(deepcopy(test),6))
