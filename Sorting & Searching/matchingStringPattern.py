'''given 2 input strings that contains spaces and no numers, 
return true if the 2 input strings have a matching pattern

ie: 'abc abc apple apple'
	'tom tom hank hank'    
	--> True
	For both strings, 1st and 2nd words are the same, 3rd and 4th words are the same
'''
from collections import OrderedDict

def match(str1, str2):

	arr1 = str1.split()
	arr2 = str2.split()

	if len(arr1) != len(arr2):
		return False


	pat1 = OrderedDict()
	pat2 = OrderedDict()

	for i in range(len(arr1)):
		if arr1[i] not in pat1.keys():
			pat1[arr1[i]] = [i]
		else:
			pat1[arr1[i]].append(i)

	for i in range(len(arr2)):
		if arr2[i] not in pat2.keys():
			pat2[arr2[i]] = [i]
		else:
			pat2[arr2[i]].append(i)

	keys1 = [key for key in pat1.keys()]
	keys2 = [key for key in pat2.keys()]

	if len(keys1) != len(keys2):
		return False
	else:
		for i in range(len(keys1)):
			if pat1[keys1[i]] != pat2[keys2[i]]:
				return False

		return True

print(match('abc abc apple apple','tom tom hank hank'))
print(match('abc abc apple apple','tom tom hunk hank'))
print(match('lol what sup lol', 'a b c a'))
print(match('a b c', 'a b a'))

'''Algorithm
Hash each substring into OrderedDict. 
Key = substring, Val = array of indices of where substring was in original input

iterate through each entry in OrderedDict to see if values match

ie:
('abc abc apple apple','tom tom hank hank') will give
dict1 = 'abc':[0,1] , 'apple':[2,3]
dict2 = 'tom':[0,1] , 'hank' :[2,3]

corresponding entries have same values, so return True
'''