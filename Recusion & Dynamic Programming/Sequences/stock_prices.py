''' STOCK OPTIMIZATION PROBLEM
Given an array of stock prices, determine when to buy and sell
to maximize profits. You must buy before you sell
'''
import sys
def findMinMax(prices):
	best = 0
	minSoFar = sys.maxsize

	for num in prices:
		minSoFar = min(minSoFar, num)
		
		if num - minSoFar > best:
			best = num - minSoFar
			print(minSoFar, num)

	return best

        
test1 = []
test2 = [1,2,1]
test3 = [2,1,3]
test4 = [4,3,2]
test5 = [30,34,37,25,25,12,11,10,30,28,36,37,34,30,28,5,23,24]

print(findMinMax(test5))