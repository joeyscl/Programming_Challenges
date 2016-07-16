'''takes an array and returns all permutations'''
def permutations(myArr):
	if len(myArr) <= 1:
		return [myArr]
	else:
		res = []

		for i in range(len(myArr)): # for each index in myArr

			#get all permutations of sub-array (myArr with current index removed)
			subperms = permutations(myArr[0:i] + myArr[i+1:])
			
			#recombine myArr[i] with each permutations of sub-array
			for perm in subperms:
				newPerm = [myArr[i]] + perm
				res.append(newPerm)

		return res


a = permutations([1,2,3])
for perm in a:
	print(perm)

''' 
Algorithm:

For each element in the given array, we attach it to the front of each permutation of the subarray without the element.

ie: given 1 2 3 4

1 + permutations of [2 3 4] (generate recursively):
	1 + 2 3 4
	1 + 2 4 3
	etc

2 + permutations of [1 3 4] (generate recursively):
	2 + 1 3 4
	2 + 1 4 3
	etc
	
etc

'''



def genPerms(s):
	if len(s) <= 1:
		return [s]
	else:
		subPerms = genPerms(s[1:])
		newPerms = []

		for sub  in subPerms:
			for i in range(len(sub)+1):
				newPerm = sub[:i] + s[0] + sub[i:]
				newPerms.append(newPerm)

		return newPerms

for s in genPerms('123'):
	print(s)