''' given an array of integers, return a value from the array using a weighted distribution
ie: [1,9] would have 90% of return 9 and 10% chance of returning 1 '''

import random

def weightedRNG(arr):
	weighted = []

	prev = 0
	for num in arr:
		weighted.append(prev + num)
		prev = weighted[-1]

	x = random.randint(1,sum(arr))
	print(x, weighted)

	for i in range(len(weighted)):
		if x <= weighted[i]:
			return arr[i]

print(weightedRNG([1,2,3]))


