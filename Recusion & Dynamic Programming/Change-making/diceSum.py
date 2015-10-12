'''given n, the number of dies, m the number of faces on each die, and s, the total the dies
have to sum up to, return the number of die **combinations** there are (must use all dies)

n = dies
m = faces
s = sum
'''

def diceSum(n,m,s):
	mem = {}
	def helper(n,m,s):
		if (n,m,s) in mem.keys():
			return mem[(n,m,s)]
		elif n*m < s or n > s:
			return 0
		elif n == 1 or n*m == s:
			return 1
		else:
			count = 0
			for i in range(s//m+1):
				count += helper(n-i, m-1, s-m*i)
			mem[(n,m,s)] = count
			return count

	return helper(n,m,s)

print(diceSum(100,100,1000))

''' Algorithm:
given (4,4,10):

f(4,4,10):

	0*4 -> f(4,3,10):
				0*3 -> f(4,2,10) = 0 	(basecase: n*m < s)
				1*3 -> f(3,2,7) = 0		(basecase: n*m < s)
				2*3	-> f(2,2,4) = 1 	(basecase: n*m = s)					3,3,2,2
				3*3 -> f(1,2,1) = 1 	(basecase: n = 1)					3,3,3,1

	1*4 -> f(3,3,6):
				3*0 -> f(3,2,6) = 1 	(basecase: n*m = s)					4,2,2,2
				3*1 -> f(2,2,3):
							0*2 -> f(2,1,3) = 0		(basecase: n*m < s)
							1*2 -> f(1,1,1) = 1 	(basecase: n = 1)		4,3,2,1

				3*2	-> f(1,2,0) = 0		(basecase: n > s)

	2*4 -> f(2,3,2):
				0*3 -> f(2,2,2):
							0*2 -> f(2,1,2) = 1 	(basecase: n*m = s)		4,4,1,1
							1*2 -> f(1,1,0) = 0		(basecase: n > 0) 
'''


'''this is wrong. this gives permutations instead'''
def diceSum1(n,m,s):
	if n*m < s or n > s:
		return 0
	elif n == 1:
		return 1
	else:
		count = 0
		for i in range(1,m+1):
			count += count(n-1,m,s-i)
		return count