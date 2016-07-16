''' take an array of 0s,1s, and 2s and sort them in linear time. 
The only operations allowed are to check the value of a specific index
and to swap the values at different indicies '''

def linearSort(arr):
	i = 0

	for j in range(len(arr)):
		if arr[j] == 0:
			arr[i], arr[j] = arr[j], arr[i] #swap
			i += 1

	for j in range(i,len(arr)):
		if arr[j] == 1:
			arr[i], arr[j] = arr[j], arr[i] #swap
			i += 1

	print(arr)

linearSort([0,1,2,1,0,1,0,2,1,0,1,2])