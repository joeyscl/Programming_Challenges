# http://cpluspluslearning-petert.blogspot.co.uk/2015/06/data-structure-and-algorithm-find_19.html

''' find the biggest subset of pairs of tuples such that there is no overlap'''

def maxSubset(arr):

	'''Helper function: Sort each pair of ints, then sorts the array of pairs by the larger integer in the pair
	ie: [(5,1),(4,6),(7,3)] -> [(1,5),(4,6),(3,7)]'''
	def sort(arr):
		arr = [tuple(sorted(tup)) for tup in arr]
		arr.sort(key=lambda tup: tup[1])
		return arr

	arr = sort(arr)
	res = [arr[0]]
	for tup in arr[1:]:
		if tup[0] >= res[-1][1]:
			res.append(tup)

	return res

print(maxSubset([(0,100), (2,50), (30,150), (60,95), (110,190), (120,150), (191,200)]))

'''ALGORITHM: 
Sort the pairs by the larger number in increasing order (lowest first).
The 1st entry is guranteed to be in the optimal solution since it has the lowest "Upper bound".
Iterate through entries and append the entry to solution if the smaller number is greater than
the bigger number of the last entry in solutions.

ie:
[(0,100), (2,50), (30,150), (60,95), (110,190), (120,150), (191,200)]

						↓ sort by larger number ↓

[(2, 50), (60, 95), (0, 100), (30, 150), (120, 150), (110, 190), (191, 200)]

ITERATE:
(2,50) 		has lowest upperbound, so we are certain we can build an optimal solution from this
(60,95)		60	>=	50, add to solution
(0,100)		0	< 	95, skip
(30,150)	30	<	95, skip
(120,150)	120 >= 	95, add to solution
(110,190)	110 <	150, skip
(191,120)	191 >=	150, add to solution

RESULT:
[(2, 50), (60, 95), (120, 150), (191, 200)]

'''

'''  BAD 2^N algorithms below!'''
# def rec(arr):
# 	res = [[]]
# 	for tup in arr:
# 		for subset in res:
# 			newRes = []
# 			newRes.append([tup])
# 			newRes.append(insert(tup,subset))
# 		res = res + newRes
		
# 	best = []
# 	for sub in res:
# 		if len(sub) > len(best):
# 			best = sub
# 	return sub

# def itr(arr):
# 	def helper(res, arr):
# 		if arr == []:
# 			return res
# 		else:
# 			res1 = helper( insert(arr[0],res), arr[1:])
# 			res2 = helper(res, arr[1:])
# 			if len(res1) > len(res2):
# 				return res1
# 			else:
# 				return res2

# 	return helper([], arr)


# ''' insert a tuple into an array of sorted tuples
# tuples are set of ints where first int is smaller than the 2nd'''
# def insert(tup, arr):
# 	if arr == []:
# 		return [(tup)]

# 	arr = arr.copy()
# 	if tup[1] < arr[0][0]:
# 		arr.insert(0,tup)
# 		return arr
# 	elif tup[0] > arr[-1][1]:
# 		arr.append(tup)
# 		return arr
# 	else:
# 		for i in range(len(arr)-1):
# 			if tup[0] >= arr[i][1] and tup[1] <= arr[i+1][0]:
# 				arr.insert(i+1, tup)
# 				return arr
# 		return arr

# arr = [(1,2),(5,6)]
# tup = (1,4)
# arr = insert(tup,arr)
# print(arr)


# print(rec([(1, 3), (2, 9), (4, 6), (7, 8)]))
# print(itr([(1, 3), (2, 9), (4, 6), (7, 8)]))
