''' Given:
class Node {
	node 	left, right
	string	val
}
find longest increasing sequence from top-down in a binary tree
'''

best = []
def func(node):
	if node.left == None and node.right == None:
		return [node.val]
	else:
		L = None
		R = None

		if node.left != None:
			if node.val+1 == node.left:
				L = func(node.left)
			else:
				L = []

		if node.right !+ None:
			if node.val+1 == node.right:
				R = func(node.right)
			else:
				R = []

		if L == None or len(R) > len(L):
			res = [node.val] + R
		else:
			res = [node.val] + L

		if len(res) > len(best):
			best = res
		return res