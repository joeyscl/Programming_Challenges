'''You have an integer and you can flip exactly one bit from a 0 to a 1. 
Write code to find the length of the longest sequence of 1s you could create.'''
def flipOne(num):

	num = str(bin(num))[2:]

	prev = ''
	seq = ''
	best = 0

	for ch in num:
		if ch == '1':
			seq += ch
		else:
			best = max(best, len(prev) + 1 + len(seq) )
			seq = ''

	return best

print(flipOne(17))
