''' given a list of Tuples (Vi,Wi) representing Boxes, where V is the value and W is the weight,
determine the maximum amount of value that can be carried by capacity W.'''
import sys

def kp_dp(arr,W):
	arr = sorted(arr, key = lambda x: (x[1],x[0])) # sort using weight

	tab = [[0]*(W+1) for i in range(len(arr))]	# maximum attainable values using box in arr[0]~arr[x]
	keep = [[0]*(W+1) for i in range(len(arr))] # flag what boxes to keep

	# initialize keep
	for w in range(len(tab[0])):
		if w >= arr[0][1]:
			keep[0][w] = 1

	# initialize tab
	for w in range(W+1):
		if w//arr[0][1] >= 1:
			tab[0][w] = arr[0][0]
	for r in range(1,len(arr)):
		tab[r][0] = tab[0][0]

	for r in range(1,len(tab)):			# number of rows == number of boxes (ie: size of arr)
		for w in range(1,len(tab[0])):	# w == 0,2,3...W
			boxWeight = arr[r][1]
			boxVal = arr[r][0]

			if boxWeight > w:
				tab[r][w] = tab[r-1][w]

			else:
				# print(boxWeight, w)
				rem = w - boxWeight
				include = boxVal + tab[r-1][rem]

				exclude = tab[r-1][w]

				if include > exclude:
					tab[r][w] = include
					keep[r][w] = 1
				else:
					tab[r][w] = exclude

	# traverse keep matrix to find optimal combination of boxes
	bestBag = []
	r = len(keep)-1
	w = len(keep[0])-1

	while r >= 0 and w >= 0:
		if w <= 0:
			break
		else:
			while keep[r][w] == 0 and r >= 0:
				r -= 1
			bestBag.append(arr[r])
			w -= arr[r][1]

	# # print intermediate results
	# for x in range(len(tab)):
	# 	print(tab[x], ' ', arr[x])	
	# print('')
	# for x in range(len(keep)):
	# 	print(keep[x], ' ', arr[x])	

	print(bestBag)
	return tab[-1][-1]

print(kp_dp([(4,12),(2,2),(1,1),(10,4),(2,1)], 5))



def kp_rec(arr,W):

	global bestBag
	global bestVal
	bestVal = 0
	# can add memoization; too lazy

	def rec(arr, W, acc, bag):
		global bestVal
		global bestBag

		if W == 0 or arr == []:
			if acc > bestVal:
				bestVal = acc
				bestBag = bag
				# print(bestVal,bestBag)
			return bestVal

		elif W < 0:
			return -sys.maxsize

		else:
			# with 1st item
			w = rec(arr[1:], W-arr[0][1], acc+arr[0][0], bag+[arr[0]])
			# without 1st item
			wo = rec(arr[1:], W, acc, bag)

			return max(w,wo)

	res = rec(arr,W, 0, [])
	print(bestBag)
	return res

print(kp_rec([(4,12),(2,2),(2,1),(10,4),(1,1)], 5))