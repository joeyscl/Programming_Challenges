''' http://www.careercup.com/question?id=5676298150084608 

Given an array of "array range", return an optimized array by deleting subarrays. 

NOTE: Array range (2,6) represents (2,3,4,5,6) 

INPUT: [(2,6),(3,5),(7,21),(20,21)] 
OUTPUT: [(2,6),(7,21)] 

[(2,6),(3,10),(7,21),(20,21)] 

Reason: (3,5) is a subarray of (2,6) and (20,21) is a subarray of (7,21)
'''

def intervals(arr):

	arr = sorted(arr, key = lambda x: (x[0],1/x[1]))
	res = [arr[0]]

	for i in range(1,len(arr)):
		curr = arr[i]

		# if previous interval 'completely covers' curr, skip
		if curr[0] >= res[-1][0] and curr[1] <= res[-1][1]: 
			continue
		else:
			useCurr = True
			for j in range(i+1,len(arr)):
				# check if curr is 'covered' by it's neighbors. ie: [1,5][3,7][6,10].
				# in this case we would not need [3,7]
				if arr[j][0] == res[-1][1] or arr[j][0] == res[-1][1]+1:
					if curr[1] <= arr[j][1]:
						useCurr = False
					else:
						break
				else:
					break					
			if useCurr:
				res.append(curr)

	return(res)

test1 = [(2,6),(3,5),(7,21),(20,21)]
test2 = [(2,6),(3,9),(8,21),(20,21)]
print(intervals(test1))
print(intervals(test2))
