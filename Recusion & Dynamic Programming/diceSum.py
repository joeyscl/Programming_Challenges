'''given n, the number of dies, m the number of faces on each die, and s, the total the dies
have to sum up to, return the number of die combinations there are (must use all dies)'''

'''wrong right now, gives permutations'''
def diceSum(n,m,s):
	if n*m < s or n > s:
		return 0
	elif n == 1:
		return 1
	else:
		subSum = 0
		for i in range(1,m+1):
			subSum += diceSum(n-1,m,s-i)
		return subSum

print(diceSum(2,2,2))