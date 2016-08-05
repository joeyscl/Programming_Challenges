''' A binary can be created from an array by inserting each element of the array successively 
from left to right. Given a binary tree, return all possible arrays that could result in the tree'''

tree = { 4:[2,6], 2:[1,3], 6:[5,7] }
tree = { 4:[2,6], 2:[1,3] }
# tree = { 2:[1,3] }

res = []
def genArrays(nexts, arr):
	# print(nexts)
	if nexts == []:
		res.append(arr)
	else:
		for i in range(len(nexts)):
			node = nexts[i]
			temp = nexts[:i] + nexts[i+1:]
			if node in tree.keys():
				temp += tree[node]
			genArrays(temp, arr+[node])

genArrays([4],[])

dic = set()
for arr in res:
	temp = ''
	for num in arr:
		temp += str(num)
	dic.add(temp)

print(dic)