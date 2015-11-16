'''
Given a random string S and another string T with unique elements, find the minimum consecutive
sub-string of S such that it contains all the elements in T. 
example: 
S='adobecodebanc' 
T='abc' 
answer='banc'
'''

def minString(string, T):

	def valid():
		return 0 not in dic.values()

	def insert(idx):
		if idx < len(string):
			if string[idx] in dic.keys():
				dic[string[idx]] += 1

	def remove(idx):
		if idx < len(string):
			if string[idx] in dic.keys():
				dic[string[idx]] -= 1

	dic = {}
	for ch in T:
		dic[ch] = 0


	i = 0
	j = 0
	best = string

	while j < len(string):

		while not valid():
			insert(j)
			j += 1

		if valid() and j-i < len(best):
			best = string[i:j]
			print(string[i:j])

		remove(i)
		i += 1
		while string[i] not in dic.keys():
			remove(i)
			i += 1
		

minString('adobecodebanc','abc')

