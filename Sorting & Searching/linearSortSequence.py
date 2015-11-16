''' given an array of integers from 0 ~ n-1 where (n is the length of the input array)
sort the array in-place in linear time '''


''' We 'sort' by swapping elements directly into where they belong 
since element value correspond to indices directly '''
def linSort(arr):

	count = 0
	idx = 0

	while count < len(arr):
		print(arr)
		if idx == arr[idx]:
			idx += 1
			count += 1
		else:
			nextIdx = arr[idx]
			arr[idx], arr[nextIdx] = arr[nextIdx], arr[idx]
			count += 1

	print(arr)

test = [2,4,6,3,8,1,0,5,9,7]
linSort(test)
