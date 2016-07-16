''' given a string, find the least number of characters needed to add to the end of the string
to turn it into a palindrome '''

def isPali(string):
	return string == string[::-1]

def leastChar(string):
	for i in range(len(string)):
		if isPali(string[i:]):
			return i

test1 = 'abcd'
test2 = 'aaaa'
test3 = 'abbb'

print(leastChar(test1))
print(leastChar(test2))
print(leastChar(test3))