'''http://www.careercup.com/question?id=12986664
Push all the zero's of a given array to the end of the array. In place only. 
Ex: 1,2,0,4,0,0,8 becomes 1,2,4,8,0,0,0'''

def partition(arr):

	i = 0
	j = len(arr)-1

	while i <= j:
		if arr[i] > 0:
			i += 1
		else:
			arr[i], arr[j] = arr[j], arr[i]
			j -= 1

	print(arr)

partition([1,2,0,4,0,0,8])