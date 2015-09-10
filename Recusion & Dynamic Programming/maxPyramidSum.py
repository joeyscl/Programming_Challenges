import copy
'''given an array of int that represents a full pyramid, 
ie:  [4,2,3,5,7,6] ->	4
					   / \
					  2	  3
					 / \ / \
					5	7	6

return an array that represents the path, starting from top and going down only, 
that results in greatest sum. ie: [4,3,7] '''

def maxPath(inputArr):
	def parsePyr(inputArr):
		pyr = []	
		rowLen = 1	
		i = 0
		while(i<len(inputArr)):
			row = []
			for j in range(rowLen):
				row.append(inputArr[i])
				i+=1
			rowLen+=1
			pyr.append(row)

		return pyr

	'''return just max sum'''
	# pyr = parsePyr(inputArr)
	# print(pyr)
	# for r in range(len(pyr))[:-1][::-1] : #reverse traverse indices except very last one
	# 	for i in range(len(pyr[r])):
	# 		pyr[r][i] += max(pyr[r+1][i],pyr[r+1][i+1])
	# return pyr[0][0]


	''' return the path'''
	pyr = parsePyr(inputArr)
	print(pyr)
	
	# make a matrix of same size as pyr, just copy for convenience
	paths = copy.deepcopy(pyr)
	paths[-1] = list([num] for num in paths[-1])

	for r in range(len(pyr))[:-1][::-1] : #reverse traverse indices except very last one
		for i in range(len(pyr[r])):
			if pyr[r+1][i] > pyr[r+1][i+1]:
				paths[r][i] = [paths[r][i]]+paths[r+1][i]
			else:
				paths[r][i] = [paths[r][i]]+paths[r+1][i+1]
				
	# print(paths)
	return paths[0][0]


print(maxPath([4,2,3,5,7,6]))



