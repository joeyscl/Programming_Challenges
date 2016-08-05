'''You have an integer and you can flip exactly one bit from a 0 to a 1. 
Write code to find the length of the longest sequence of 1s you could create.'''
def flipOne(num):

	def DP(num):
		num = str(bin(num))[2:]

		i = 0
		j = 0

		best = 0
		counter = [0,0]

		counter[int(num[j])] += 1

		while j < len(num)-1:
			j += 1
			counter[int(num[j])] += 1
			if counter[0] > 1:
				counter[int(num[i])] -= 1
				i += 1
			else:
				best = max(best,sum(counter))

		return best


	def noDP(num):
		num = str(bin(num))[2:]
		prevChar = ''
		prev1s = 0
		curr1s = 0
		best = 0

		for ch in num:
			if ch == '0':
				if prevChar == '0':
					prev1s = 0
					curr1s = 0
				else:
					prev1s = curr1s
					curr1s = 0
					best = max(best, prev1s+1)
			else:
				curr1s += 1
				best = max(best, curr1s+prev1s+1)

		return best


	print(num, str(bin(num))[2:])
	return(DP(num),noDP(num))


print(flipOne(90))
