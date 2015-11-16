''' given integer M, fill an M x M matrix using integers 0 ~ M^2 -1 in a clockwise inward spiral fashion.
1  2  3  4
12 13 14 5
11 16 15 6
10  9  8 7'''

def spiral(M):
	mat = [[0]*M for x in range(M)]

	left = 0	
	right = M-1
	upper = 0
	lower = M-1

	num = 0


	while num <= M**2-1:
		for c in range(left,right+1):
			mat[upper][c] = str(num).zfill(2)
			num += 1
		upper += 1

		for r in range(upper,lower+1):
			mat[r][right] = str(num).zfill(2)
			num += 1
		right -= 1

		for c in range(right,left-1,-1):
			mat[lower][c] = str(num).zfill(2)
			num += 1
		lower -= 1

		for r in range(lower,upper-1,-1):
			mat[r][left] = str(num).zfill(2)
			num += 1
		left += 1

	for row in mat:
		print(row)

spiral(10)







