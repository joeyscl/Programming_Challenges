''' http://www.careercup.com/question?id=7781671
Given an integer array, sort the integer array such that the concatenated integer 
of the result array is max. e.g. [4, 94, 9, 14, 1] will be sorted to 
[4, 419, 94, 9, 14, 1] where the result integer is 9944419141 (9,94,4,419,14,1)
'''''' http://www.careercup.com/question?id=7781671
Given an integer array, sort the integer array such that the concatenated integer 
of the result array is max. e.g. [4, 94, 9, 14, 1] will be sorted to 
[4, 419, 94, 9, 14, 1] where the result integer is 9944419141 (9,94,4,419,14,1)
'''

def largestIntArray(arr):
	arr = [str(num) for num in arr]

	longest = max(len(num) for num in arr)
	tab = {}

	for num in arr:
		key = num + num[0]*(longest-len(num))
		if key not in tab:
			tab[key] = [num]
		else:
			tab[key].append(num)

	print(tab)

	res = ''
	for key in sorted(tab.keys(),reverse= True):
		for num in tab[key]:
			res += num

	return(res)

print(largestIntArray([5,55,555]))
print(largestIntArray([7,71, 714,717]))
print(largestIntArray([4, 419, 94, 9, 14, 1]))