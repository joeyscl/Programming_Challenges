'''http://www.careercup.com/question?id=16230693
given an int array with no duplicate numbers, write a function to return number of ways to calculate a target number. 

example: given {2,4,6,8} Target = 12 
2 + 4 + 6 = 12, 
4 + 8 = 12, 
6 + 8 - 2 = 12, 
2 - 4 + 6 + 8 = 12, 

return 4'''

def ways(arr,target):
	global res
	res = 0

	def way(arr,target):
		global res
		if target == 0:
			res += 1
			if arr != []:
				way(arr[1:],target-arr[0])
				way(arr[1:],target+arr[0])

		elif arr == []:
			return

		else:
			way(arr[1:],target-arr[0])
			way(arr[1:],target+arr[0])
			way(arr[1:],target)

	way(sorted(arr),target)
	return res

print(ways([2,4,6,8],12))