'''given an array of integers and an integer, return true if there is a subset whose sum equals to the integer'''

def subsetSum(arr,num):
	mem = {}
	def helper(idx,num):
		if (idx,num) in mem.keys():
			return mem[(idx,num)]
		elif idx == -1 and num == 0:
			return True
		elif idx == -1:
			return False
		elif num == 0:
			return True
		else:
			With = helper(idx-1, num - arr[idx])
			if With:
				mem[(idx-1, num - arr[idx])] = True
				return True
			else:
				mem[(idx-1, num - arr[idx])] = False


			WithOut = helper(idx-1, num)
			if WithOut:
				mem[(idx-1, num)] = True
				return True
			else:
				mem[(idx-1, num)] = False

			return False

	return helper(len(arr)-1,num)

print(subsetSum([12, 1, 3, 8, 20, 50],44))