''' given an input string, return an anagram of the same string such that there are
no neighboring letters that are same. return 'Not possible' if not possible'''

def noTwins(string):
	freq = [0]*26
	for ch in string:
		freq[ord(ch.lower())-ord('a')] += 1

	if max(freq)-1 > sum(freq)-max(freq):
		return 'Not possible'



	res = ''
	while freq != [0]*26:
		mostIdx = freq.index(max(freq))
		mostLet = chr(mostIdx+ord('a'))
		while freq[mostIdx] > 0:
			# print(freq)
			res += mostLet
			freq[mostIdx] -= 1

			nextIdx = -1
			for i in range(len(freq)):
				if freq[i] != 0 and i != mostIdx:
					nextIdx = i
					break

			if nextIdx != -1:
				nextLet = chr(nextIdx+ord('a'))
				res += nextLet
				freq[nextIdx] -= 1
			else:
				break
			mostIdx = freq.index(max(freq))
			mostLet = chr(mostIdx+ord('a'))

	return(res)	

print(noTwins('aaabc'))
