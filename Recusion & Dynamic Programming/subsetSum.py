'''given an array of integers and an integer, return true if there is a subset whose sum equals to the integer'''

''' Method 1: Use recursion + tabulation to solve subproblems'''
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

'''Method 1: Use recursion to find sums of subproblems'''
def subsetSum1(arr,num):
	def genSubsums(arr,total):
		if total > num:
			return
		elif arr == []:
			return [total]
		else:
			res = []
			for i in range(len(arr)):
				newSums = genSubsums(arr[i+1:],arr[i]+total)
				if newSums != None:
					res += newSums
			return res

	res = genSubsums(arr,0)
	# print(res)
	return num in res


# print(subsetSum([12, 1, 50, 3, 8, 20],44))
# print(subsetSum1([12, 1, 50, 3, 8, 20],44))

target = 7417681752321838920495924036
A = [2316931787588303659213440000,
     1303274130518420808307560000,
     834095443531789317316838400,
     579232946897075914803360000,
     425558899761116998631040000,
     325818532629605202076890000,
     257436865287589295468160000,
     208523860882947329329209600,
     172333769324749858949760000,
     152389238109289308120900000,
     144808236724268978700840000,
     123386899930738064691840000,
     106389724940279249657760000,
     106389724940279249657750000,
     92677271503532146368537600,
     81454633157401300519222500,
     72153585080604612224640000,
     64359216321897323867040000,
     57762842349846905631360000,
     57153583683422246400000000,
     52130965220736832332302400,
     47284322195679666514560000,
     43083442331187464737440000,
     39418499221729173786240000,
     36202059181067244675210000,
     33363817741271572692673536]

print(subsetSum(A,target))
# print(subsetSum1(A,target))