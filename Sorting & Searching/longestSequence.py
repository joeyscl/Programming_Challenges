'''http://www.careercup.com/question?id=11070934

Given an int array which might contain duplicates, find the largest subset of it which form a sequence. 
Eg. {1,6,10,4,7,9,5} 
then ans is 4,5,6,7 

Sorting is an obvious solution. Can this be done in O(n) time'''

def longestSeq(arr):
	nums = set()
	for num in arr:
		nums.add(num)

	best = []
	for num in nums:
		seq = []
		while num in nums:
			seq.append(num)
			num += 1

		if len(seq) > len(best):
			best = seq

	return best

print(longestSeq([1,6,10,4,7,9,5]))