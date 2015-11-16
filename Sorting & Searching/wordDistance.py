''' http://www.careercup.com/question?id=6273553081040896

Given a string and two words which are present in the string, find the minimum distance between the words 
Eg: "the brown quick frog quick the", "the" "quick" O/P -> 1 
"the quick the brown quick brown the frog", "the" "the" O/P -> 2
'''
from sys import maxsize
def minDist(phrase, str1, str2):
	phrase = phrase.split()

	dic = {str1: [], str2: []}
	for i in range(len(phrase)):
		if phrase[i] == str1 or phrase[i] == str2:
			dic[phrase[i]].append(i)

	print(dic)

	arr1 = dic[str1]
	arr2 = dic[str2]

	best = abs(arr1[0]-arr2[0])
	i = 0
	j = 0

	while i < len(arr1) and j < len(arr2):
		best = min(best, abs(arr1[i]-arr2[j]))
		if arr1[i] < arr2[j]:
			i += 1
		else:
			j += 1

	return best



print(minDist("the brown quick frog quick the", "the", "quick"))

