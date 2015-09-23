''' Given integer n, return a n bc n chessboard with n number of queens that cannot attack each other'''

def queens(n):
	def backtrack():
		global r,c,count
		while r >= 0 and c >= 0:
			# print("backtrack",(r,c))
			if board[r][c] == 1:
				board[r][c] = 0
				count -= 1
				hor.remove(c)
				vert.remove(r)
				dia1.remove(r+c)
				dia2.remove(r-c)
				return True
			else:
				if c - 1 < 0:
					r -= 1
					c = n-1
				else:
					c -= 1
		return False

	def insert():
		global r,c, count
		if r >= 0 and c >= 0 and r < n and c < n:
			board[r][c] = 1
			count += 1			
			hor.add(c)
			vert.add(r)
			dia1.add(r+c)
			dia2.add(r-c)
			return True
		else:
			return False

	def isValid():
		global r,c
		if c in hor or r in vert or r+c in dia1 or r-c in dia2:
			return False
		else:
			return True

	board = [[0]*n for i in range(n)]	# the board

	# sets to keep keep track where queens can attack
	hor = set()
	vert = set()
	dia1 = set()
	dia2 = set()
	checks = (hor,vert,dia1,dia2)

	global count,r,c 
	count = 0	# number of queens
	r = 0
	c = 0

	'''Use backtracking DFS'''
	while count < n:
		while r < n and c < n:
			if isValid():
				insert()
				r+=1
				c=0
			else:
				c+=1

		if count == n:
			break
		elif r <= 0 or c <= 0:
			print("No solution")
			break
		else:
			c-=1
			backtrack()
			c+=1
	return board

def printNicely(board):
	for row in board:
		print(row)

printNicely(queens(20))
