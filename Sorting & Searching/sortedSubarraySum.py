''' given a sorted subarray and a target sum, determine if there is a subarray that 
adds up to the target sum
ie: [1,3,5,7], 8 --> True
	[1,3,5,7], 6 --> False
'''

def subarraySum(arr, num):

	i = 0
	j = 0
	total = 0

	while j < len(arr):

		if total < num and j < len(arr):
			total += arr[j]
			j += 1		

		if total > num and i < len(arr):
			total -= arr[i]
			i += 1

		if total == num:
			return True

	return False


print(subarraySum([1,3,5,7], 1))
print(subarraySum([1,3,5,7], 8))
print(subarraySum([1,3,5,7], 7))
print(subarraySum([1,1,1,1], 4))
print(subarraySum([1,1,1,1], 6))