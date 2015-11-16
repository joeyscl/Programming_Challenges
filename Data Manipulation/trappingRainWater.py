''' https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''

def trappingRainWater(arr):
	water = 0
	# for each block height from 0 to tallest block
	for H in range(max(arr)+1):

		# find 1st solid block at current height
		for i in range(len(arr)):
			if arr[i] >= H:
				left = i
				break

		# find last solid block at the current height
		for j in reversed(range(len(arr))):
			if arr[j] >= H:
				right = j
				break

		# for every square between 1st and last, if height < current height, water++
		for h in arr[i:j+1]:
			if h < H:
				water += 1

	return(water)

print(trappingRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))