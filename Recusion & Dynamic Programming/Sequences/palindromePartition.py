''' https://leetcode.com/problems/palindrome-partitioning-ii/
given a string, use the minimum partitions such that each substring is a palindrome.
ie: abfbcbd -> aa, bcb, d
'''
def partition(string):

	def isPalindrome(string):
		return string == string[::-1]


	mem = {}
	def part(string):
		if len(string) <= 1:
			return [string]

		if string in mem.keys():
			return mem[string]

		shortestRest = ['0']*(len(string)+1)
		bestPali = ''

		# find all palindromes that start with index 0 of our string
		# can use better algorithms such as manacher's to optimize
		# or use memoization/dp to store intermediate results
		for i in range(1,len(string)):
			if isPalindrome(string[:i]):
				rest = part(string[i:])
				if len(rest) < len(shortestRest):
					shortestRest = rest
					bestPali = string[:i]

		mem[string] = [bestPali] + shortestRest
		return [bestPali] + shortestRest

	temp = part(string)
	res = temp[0]
	for pali in temp[1:]:
		res += ' ' + pali
	return res

print(partition('abfbcbd'))
print(partition('aabbaaa'))
print(partition("ababababababababababababcbabababababababababababa"))