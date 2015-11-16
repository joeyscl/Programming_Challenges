from copy import deepcopy
''' given integer n, determine how many ways a n by n chessboard can be filled n queens that cannot attack each other'''

def queens(n):

	size = n
	mem = {}

	def isValid(B,r,c):
			if (c in B[0] or r in B[1] or r+c in B[2] or r-c in B[3]) or (r >= size or c >= size):
				return False
			else:
				return True

	def insert(B,r,c):
		B[0].add(c)
		B[1].add(r)
		B[2].add(r+c)
		B[3].add(r-c)
		return B

	def ways(n,B,r,c):
		# print(n,B,r,c, isValid(B,r,c))

		if not isValid(B,r,c):
			return 0

		else:
			insert(B,r,c)
			n -= 1
			r += 1
			res = 0
			if n == 0:
				return 1

			for j in range(size):
				newB = deepcopy(B)
				res += ways(n,newB,r,j)

			return res
			

	B = [set() for i in range(4)]
	res = 0
	for j in range(size):
		res += ways(n,deepcopy(B),0,j)

	return res

print(queens(8))
