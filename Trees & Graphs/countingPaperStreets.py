'''https://github.com/housecanary/paper_streets

x_intercepts = [0, 2, 4]
y_intercepts = [0, 2]
homes = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 2), (4, 0), (4, 1), (4, 2)]

2 X---X---X---X---X
  |       |       |
1 X       |       X
  |       |       |
0 X---X---X---X---X
  0   1   2   3   4

A paper street is a street on which there is no home. Count all groups of interconneected paper streets

'''
from bisect import *

def count_paper_streets(x_intercepts, y_intercepts, homes):

	def parseMap():
		M = [['_']*(x_intercepts[-1]+1) for _ in range(y_intercepts[-1]+1)]
		return M

	def searchUp(i,j):
		print("up",i,j)
		if i >= rowCount or j >= colCount:
			return 0

		for r in range(i, nextIntersectUp(i)):
			if (r,j) in visited:
				continue
			else:
				visited.add((i,j))
				if (r,j) in homes:		#there is a home on this street					
					return False
				else:
					continue		 	#keep looking

		searchUp(nextIntersectUp(i), j)
		searchRight(i, nextIntersectUp(j))
		return True

	def searchRight(i,j):
		print("right",i,j)
		if i >= rowCount or j >= colCount:
			return 0

		for c in range(j, nextIntersectRight(j)):
			if (i,c) in visited:
				continue
			else:
				visited.add((i,c))
				if (i,c) in homes:		#there is a home on this street					
					return False
				else:
					continue 			#keep looking

		searchUp(nextIntersectUp(i), j)
		searchRight(i, nextIntersectUp(j))
		return True


	def nextIntersectUp(i):
		return x_intercepts[bisect_right(x_intercepts,i)]

	def nextIntersectRight(j):
		return y_intercepts[bisect_right(y_intercepts,j)]


	print(parseMap())

	# rowCount = x_intercepts[-1]+1
	# colCount = y_intercepts[-1]+1

	# xSet = set(x_intercepts)
	# ySet = set(y_intercepts)

	# x_intercepts.append(rowCount)
	# y_intercepts.append(colCount)

	# homes = set(homes)
	# visited = set()

	# psCount = 0		#number of paper street groups

	# for i in range(rowCount):
	# 	for j in range(colCount):
	# 		print(i,j, (i,j) in visited)

	# 		if (i,j) in visited:
	# 			continue

	# 		elif i in xSet and j in ySet:
	# 			if searchUp(i,j) or searchRight(i,j):
	# 				psCount += 1
	# 				print("PS found", i,j)
	# 			visited.add((i,j))
	# 		else:
	# 			visited.add((i,j))

	# return psCount

x_intercepts = [0, 2, 4]
y_intercepts = [0, 2]
homes = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 2), (4, 0), (4, 1), (4, 2)]

# x_intercepts = [0, 2, 5, 7]
# y_intercepts = [0, 3, 5, 7]
# homes = [(0, 0), (0, 3), (0, 5), (0, 6), (0, 7), (1, 0), (1, 3), (1, 5), (1, 7), \
# (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (3, 0), (4, 3), (4, 7), (5, 0), \
# (5, 1), (5, 3), (5, 4), (5, 5), (5, 7),(6, 0), (6, 5), (6, 7), (7, 0), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]

# x_intercepts = [0, 1, 2, 3, 4, 6, 9, 11, 12, 13, 14, 18, 19, 20, 21, 24, 27, 29, 31]
# y_intercepts = [0, 3, 6, 7, 12, 14, 17, 18, 21, 22, 28, 30, 31]
# homes = [(0, 1), (0, 4), (0, 9), (0, 10), (0, 11), (0, 15), (0, 16), (0, 19), (0, 20), (0, 23), (0, 24),
#                       (0, 25), (0, 26), (0, 29), (1, 1), (1, 2), (1, 8), (1, 10), (1, 15), (1, 16), (1, 29), (2, 1),
#                       (2, 2), (2, 4), (2, 8), (2, 10), (2, 13), (2, 15), (2, 16), (2, 20), (2, 23), (2, 25), (2, 29),
#                       (3, 1), (3, 2), (3, 5), (3, 8), (3, 9), (3, 11), (3, 15), (3, 19), (3, 20), (3, 23), (3, 25),
#                       (3, 27), (3, 29), (4, 8), (4, 19), (4, 20), (4, 25), (6, 5), (6, 9), (6, 15), (6, 19), (6, 25),
#                       (6, 26), (6, 29), (9, 2), (9, 8), (9, 11), (9, 13), (9, 16), (9, 20), (9, 23), (9, 24), (9, 25),
#                       (9, 26), (9, 29), (11, 4), (11, 9), (11, 10), (11, 15), (11, 20), (11, 23), (11, 24), (11, 25),
#                       (11, 26), (11, 27), (12, 2), (12, 8), (12, 13), (12, 15), (12, 16), (12, 20), (12, 23), (12, 24),
#                       (12, 25), (12, 29), (13, 1), (13, 2), (13, 4), (13, 10), (13, 11), (13, 19), (13, 20), (13, 23),
#                       (13, 29), (14, 2), (14, 4), (14, 16), (14, 26), (18, 2), (18, 4), (18, 8), (18, 10), (18, 11),
#                       (18, 16), (18, 25), (18, 26), (19, 10), (19, 11), (19, 15), (19, 16), (19, 20), (19, 25),
#                       (19, 29), (20, 8), (20, 10), (20, 11), (20, 16), (20, 19), (20, 20), (20, 23), (20, 24), (20, 27),
#                       (21, 1), (21, 2), (21, 4), (21, 5), (21, 9), (21, 11), (21, 13), (21, 15), (21, 16), (21, 23),
#                       (21, 24), (21, 26), (21, 27), (24, 1), (24, 2), (24, 9), (24, 10), (24, 15), (24, 19), (24, 20),
#                       (24, 24), (24, 29), (27, 2), (27, 5), (27, 9), (27, 25), (27, 29), (29, 1), (29, 2), (29, 8),
#                       (29, 9), (29, 11), (29, 15), (29, 19), (29, 25), (31, 1), (31, 2), (31, 9), (31, 10), (31, 11),
#                       (31, 13), (31, 15), (31, 23), (31, 29), (5, 0), (7, 0), (8, 0), (17, 0), (22, 0), (23, 0),
#                       (25, 0), (30, 0), (5, 3), (8, 3), (10, 3), (23, 3), (25, 3), (26, 3), (28, 3), (5, 6), (7, 6),
#                       (8, 6), (15, 6), (16, 6), (17, 6), (23, 6), (26, 6), (28, 6), (30, 6), (10, 7), (15, 7), (16, 7),
#                       (17, 7), (28, 7), (5, 12), (7, 12), (16, 12), (17, 12), (23, 12), (28, 12), (5, 14), (8, 14),
#                       (10, 14), (16, 14), (25, 14), (30, 14), (15, 17), (16, 17), (17, 17), (25, 17), (28, 17), (7, 18),
#                       (8, 18), (10, 18), (16, 18), (17, 18), (25, 18), (26, 18), (28, 18), (5, 21), (7, 21), (10, 21),
#                       (15, 21), (23, 21), (26, 21), (28, 21), (30, 21), (7, 22), (8, 22), (16, 22), (23, 22), (26, 22),
#                       (8, 28), (10, 28), (17, 28), (23, 28), (26, 28), (30, 28), (8, 30), (10, 30), (16, 30), (17, 30),
#                       (22, 30), (23, 30), (25, 30), (26, 30), (30, 30), (7, 31), (10, 31), (15, 31), (16, 31), (17, 31),
#                       (23, 31), (26, 31), (28, 31)]


print(count_paper_streets(x_intercepts,y_intercepts,homes))
