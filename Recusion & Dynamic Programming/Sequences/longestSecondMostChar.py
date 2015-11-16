''' given a string, find the longest substring such that it contains
1) any number of most frequent character
2) at most 2 of second most frequent character
3) none of any other character '''

def findSub(string):

	def isValid():
		temp = [num for num in tab if num != 0]
		if len(temp) > 2:
			return False

		elif len(temp) == 2:
			return min(temp) <= 2

		else:
			return True

	def insert(idx):
		tab[ord(string[idx])-ord('a')] += 1

	def remove(idx):
		tab[ord(string[idx])-ord('a')] -= 1


	tab = [0]*26
	best = ''

	i = 0
	j = 0

	while j < len(string):

		if isValid():
			insert(j)
			j += 1

		if isValid() and j-i > len(best):
			best = string[i:j]
			
		if not isValid():
			remove(i)
			i += 1

	return best

test1 = 'aaxxaaxbbbbxbbb'
test2 = 'aabbbabccc'
test3 = 'abbbabbbbbbaa'
print(findSub(test1))
print()
print(findSub(test2))
print()
print(findSub(test3))






