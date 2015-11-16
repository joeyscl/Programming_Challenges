''' given a square m by m matrix, rotate each entry clockwise. ie: M[0][3] -> M[3][-1] '''

def rotateMatrix(arr):
	layers = len(arr)//2
	size = len(arr)

	for row in arr:
		print(row)
	print('')
	
	for i in range(layers):
		topRow = [arr[i][x] for x in range(i,size)]
		btmRow = [arr[-1-i][-1-x] for x in range(i,size)]
		leftCol = [arr[-1-x][i] for x in range(i,size)]
		rightCol = [arr[x][-1-i] for x in range(i,size)]

		for x in range(i,size):
			arr[i][x] = leftCol[x-i] 		# assign top row
			arr[-1-i][-1-x] = rightCol[x-i] # assign btm row
			arr[-1-x][i] = btmRow[x-i]		# assign left col
			arr[x][-1-i] = topRow[x-i]		# assign right col

		size -= 1

	for row in arr:
		print(row)

t0 = [[1,2,],[3,4]]
t1 = [[1,2,3],[4,5,6],[7,8,9]]
t2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotateMatrix(t2)

