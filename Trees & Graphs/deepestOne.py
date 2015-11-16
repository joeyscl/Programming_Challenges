'''http://www.careercup.com/question?id=7617672
Path to deepest 1 in a binary tree. 
We have a binary tree (not a BST) made up of only 0s and 1s. 
We need to find the deepest 1 with a path from root made up only of 1's.
Return length of path
'''

global best
best = 0
def deepest(node,length):
	global best
	if node == None or node.val == 0:
		best = max(best,length)
	else:
		deepest(node.left, length+1)
		deepest(node.right, length+1)

deepest(root, 0)
print(best)
