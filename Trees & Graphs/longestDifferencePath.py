''' Given an input matrix of integer values, find the length of the longest path 
such that all adjacent nodes in the path are within a difference of 1 of each other in value. 
Assuming a paths starts from top-left and can end anywhere'''

def longestPath(mat):

	global best
	best = 0

	def dfs(r,c, visited, count):
		global best

		# reached bottom right exit
		if r == len(mat) and c == len(math[0]):
			best = max(best, count)
			return

		# node has already been visited
		elif (r,c) in visited:
			best = max(best, count)
			return

		# out of bound
		elif r <= 0 or r >= len(mat) or c <= 0 or c >= len(mat[0]):
			best = max(best, count)
			return

		else:
			visited.add((r,c)) # update visited
			count += 1		   # update steps taken
			neighbors = [ [r+1,c], [r-1,c], [r,c+1], [r,c-1] ]

			for n in neighbors:
				if abs( mat[r][c] - mat[n[0][1]]] ) <= 1: # check constraint
					dfs(n[0],n[1], deepcopy(visited), count)

	dfs(0,0, set(), 1)


