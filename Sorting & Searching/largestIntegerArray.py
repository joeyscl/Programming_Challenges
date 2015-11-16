''' http://www.careercup.com/question?id=7781671
Given an integer array, sort the integer array such that the concatenated integer 
of the result array is max. e.g. [4, 94, 9, 14, 1] will be sorted to 
[9,94,4,14,1] where the result integer is 9944141
'''
import sys

def largestIntArray(arr):

	arr = (sorted([str(num) for num in arr]))[::-1]
	dic = {}

	for num in arr:
		if num[0] not in dic.keys():
			dic[num[0]] = [num]
		else:
			dic[num[0]].append(num)

	for key in dic.keys():
		length = len(max(dic[key]))
		dic[key] = [string.ljust(length,'$') for string in dic[key]]
		dic[key] = sorted(dic[key], key = custom, reverse = True)
	# print(dic)

	resStr = ''
	res = []
	for key in reversed(sorted(dic.keys())):
		for entry in dic[key]:
			resStr += entry
			res.append(entry.replace('$',''))
	resStr = resStr.replace('$','')
	return(res)

''' some special math for special sorting so we can use built in sort function
(alternatively if we can write a comparator(input1,input2) and implement our own sorting)'''
'''We generate key value by character. Normal value if ch is >= than the ch that preceeds it.
Inverse value if ch is < value that preceeds it'''
def custom(string):
	if len(string) == 0 or len(string) == 1:
		return ord(string)

	elif string[0] == '0':
		return 1/sys.maxsize

	elif string[0] > string[1]:
		return 1/ord(string[0]) + custom(string[1:])/1000

	else:
		return ord(string[0]) + custom(string[1:])/1000

# test the custom sorting key
# print(sorted(['553','55$','544'], key = custom)[::-1])

print(largestIntArray([4, 94, 9, 14, 1]))