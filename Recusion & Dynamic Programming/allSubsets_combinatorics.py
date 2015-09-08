def genSubsets(arr):

	subsets = []

	length = len(arr)
	for i in range(2**length):
		binStr = str(bin(i))[2:].zfill(length) # change i to binary. convert to string. fill preceeding 0s.

		newSet = []
		for j in range(length):
			if binStr[j] == '1':
				newSet.append(arr[j])

		subsets.append(newSet)	

	# print nicely
	for subset in subsets:
	    print(subset)

genSubsets([1,2,3,4])



