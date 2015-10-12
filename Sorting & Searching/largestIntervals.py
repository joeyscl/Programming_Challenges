from copy import deepcopy
''' given an array of integer pairs (as tuple or list), 
minimize the number of overlapping or consecutive ones.
Test Input: [4, 8], [3, 5], [-1, 2], [10, 12] 
Test ouput: [-1, 8], [10,12]
'''

def func(pairs):
	pairs = sorted([sorted(pair) for pair in pairs])

	res = []
	curr = deepcopy(pairs[0])

	i = 1
	start = curr[0]
	end = curr[1]
	while True:

		if i >= len(pairs):
			res.append(curr)
			break

		if end+1 >= pairs[i][0]:
			if end >= pairs[i][1]:
				pass
			else:
				curr[1] = pairs[i][1]
				end = pairs[i][1]

		else:
			res.append(curr)
			curr = deepcopy(pairs[i])

		i+=1

	return(res)

print(func([[4, 8], [3, 5], [-1, 2], [10, 12]]))