'''Give you an array which has n positive and negative integers, 
sort this array so that all the negative integers are in the front and all the positive integers are in the back. 
The relative positions of the integers should not be changed.
eg. -1 1 3 -2 2 ans: -1 -2 1 3 2.
There is an o(n)time complexity and o(1) space complexity.
'''

def part(arr):
	size = len(arr)
	i = 0
	j = size-1

	while i < j:
		if arr[i] < 0:
			i += 1
		else:
			arr[i], arr[j] = arr[j], arr[i]
			j -= 1

	print(arr)

part([-1, 1, 3, -2, 2])