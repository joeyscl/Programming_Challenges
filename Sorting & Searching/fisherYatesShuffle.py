''' shuffle an array in-place in O(n) time and O(1) memory '''

# use fisher-yates shuffle
from random import randint
def fsShuffle(arr):
	for i in range(len(arr)):
		idx = randint(i,len(arr)-1)
		arr[i], arr[idx] = arr[idx], arr[i]

	print(arr)

test = [0,1,2,3,4,5,6,7,8,9]
fsShuffle(test)