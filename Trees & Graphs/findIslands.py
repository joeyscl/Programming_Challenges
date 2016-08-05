'''
Counting the islands. 
Given a map respresented as n-length list of n-length strings,
0 - sea 
X - land 

Land is connected by 4-Neighbor connections, i.e.: above, down, left and right. 

Output of this map: 4 (totally 4 islands on the map)
'''


def countIslandsDFS(Map):
	height = len(Map)
	width = len(Map[0])
	global islands 
	islands = 0
	visited = set()
	
	def explore():
		global islands
		for i in range(height):
			for j in range(width):
				if (i,j) in visited:
					continue
				elif Map[i][j] != 'X':
					# print((i,j),'0')
					visited.add((i,j))
				else:
					Xs = DFS(i,j)
					if Xs >= 4:
						islands += 1

	def DFS(r,c):
		if (r,c) in visited or r < 0 or c < 0 or r >= height or c >= width:
			return 0		
		if Map[r][c] != 'X':
			visited.add((r,c))
			return 0
		else:
			# print((r,c,),'X')
			visited.add((r,c))
			Xs = 1 + DFS(r+1,c) + DFS(r-1,c) + DFS(r,c+1) + DFS(r,c-1)
			return Xs

	explore()
	return islands

from collections import deque
def countIslandsBFS(Map):
	height = len(Map)
	width = len(Map[0])
	global islands 
	islands = 0
	visited = set()
	
	def explore():
		global islands
		for i in range(height):
			for j in range(width):
				if (i,j) in visited:
					continue
				elif Map[i][j] != 'X':
					# print((i,j),'0')
					visited.add((i,j))
				else:
					Xs = BFS(i,j)
					if Xs >= 4:
						islands += 1

	def BFS(r,c):
		count = 1
		Q = deque()
		Q.appendleft((r,c))
		i = 0
		j = 0

		while len(Q) > 0:
			temp = Q.pop()
			i = temp[0]; j = temp[1]
			if (i,j) in visited or i < 0 or j < 0 or i >= height or j >= width:
				continue
			else:
				visited.add((i,j))
				if Map[i][j] == 'X':
					# print(i,j)
					count += 1
					for nexts in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
						Q.appendleft(nexts)
				

		return count

	explore()
	return islands



M = \
[\
'00000000000000000000000000000000000', 
'00000000000000000000000000000000000', 
'00000000000000000000000000000000000', 
'0000000000000000000X000000000000000', 
'000000000000000000XXX00000000000000', 
'000XX000000000000000000000000000000', 
'000XXXX0000000000000000000000000000', 
'0000000X0000000000000X0000000000000', 
'0000000X0000000000000XXX00000000000', 
'0000000X0000000000000X0000000000000', 
'0000000X000000000000000000000000000', 
'00000000000000000000000000000000000', 
'00000000000000000000000000000000000', 
'000000000000000000000000000X0000000', 
'000000000000000000000000000XXXX0000', 
'00000000000000000000000000000000000', 
'00000000000000000000000000000000000', 
'00000000000000000000000000000000000'] 
print(countIslandsDFS(M))
print(countIslandsBFS(M))

