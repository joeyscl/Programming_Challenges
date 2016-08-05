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
		M = [['_']*(y_intercepts[-1]+1) for _ in range(x_intercepts[-1]+1)]
		return M

	return parseMap()

x_intercepts = [0, 2, 4]
y_intercepts = [0, 2]
homes = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2), (3, 0), (3, 2), (4, 0), (4, 1), (4, 2)]

print(count_paper_streets(x_intercepts,y_intercepts,homes))