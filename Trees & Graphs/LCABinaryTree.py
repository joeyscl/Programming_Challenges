''' https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree (not BST), find the lowest common ancestor (LCA) of two given nodes in the tree.


        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. 
Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself'''

def LCA(root,val1,val2):
	def preOrd(node,val,path):
		if node.val == val:
			return path + [node]
		elif node == None:
			return None
		else:
			left = None
			right = None

			left = preOrd(node.left, val, path+[node])
			right = preOrd(none.right, val, path+[node])

			if left != None:
				return left
			elif right != None:
				return right
			else:
				return None

	val1Path = preOrd(root,val1,[])
	val2Path = preOrd(root,val2,[])

	if val1Path == None or val2Path == None:
		return ('Val1 or Val2 not found in Tree')

	minLen = min(len(val1Path),len(val2Path))
	for i in range(min(minLen):
		if val1Path[i] == val2Path[i] and i != minLen-1:
			continue
		elif val1Path[i] != val2Path[i]:
			return val1Path[i-1]
		else: # val1Path[i] == val2Path[i] and i is last index
			return val1Path[i]


