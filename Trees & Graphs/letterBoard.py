'''http://www.careercup.com/question?id=16142677

Given an virtual 4x4 boggle board, and some 4 letter words, determine if the words are in the board
if words can be formed by using any (up-to) 8 neighboring letters

S M E F 
R A T D 
L O N I 
K A F B 

STAR- no 
TONE- no 
NOTE- yes 
SAND- yes 
'''

def search(word):
	visited = set()
	def DFS(word, r, c):
		if r < 0 or c < 0 or r >= len(mat) or c >= len(mat) or (r,c) in visited:
			return False

		if word == '':
			return True
		elif mat[r][c] != word[0]:
			return False
		else:
			visited.add((r,c))
			Rpos = [r-1, r,	 r+1, r-1, r+1, r-1, r,	  r-1]
			Cpos = [c+1, c+1, c+1, c,	 c,	c-1, c-1, c-1]
			res = False
			for x in range(8):
				res = DFS(word[1:],Rpos[x],Cpos[x])
				if res:
					return True
			return False

	''' search of entry point for DFS'''
	res = False
	for i in range(len(mat)):
		for j in range(len(mat)):
			if mat[i][j] == word[0]:
				res = DFS(word,i,j)
				if res:
					return True
	return False

mat = [\
['S','M','E','F'],\
['R','A','T','D'],\
['L','O','N','I'],\
['K','A','F','B']]

print(search('STAR'))
print(search('TONE'))
print(search('NOTE'))
print(search('SAND'))
print(search('MAMA'))


