def countIslands(Map):
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
					print((i,j),'0')
					visited.add((i,j))
				else:
					Xs = expIsland(i,j)
					if Xs >= 4:
						islands += 1

	def expIsland(r,c):
		if (r,c) in visited or r < 0 or c < 0 or r >= height or c >= width:
			return 0		
		if Map[r][c] != 'X':
			visited.add((r,c))
			return 0
		else:
			print((r,c,),'X')
			visited.add((r,c))
			Xs = 1 + expIsland(r+1,c) + expIsland(r-1,c) + expIsland(r,c+1) +expIsland(r,c-1)
			return Xs

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
print(countIslands(M))


'''
Counting the islands. 
Given a map respresented as n-length list of n-length strings,
0 - sea 
X - land 

Land is connected by 4-Neighbor connections, i.e.: above, down, left and right. 

Output of this map: 4 (totally 4 islands on the map)
'''