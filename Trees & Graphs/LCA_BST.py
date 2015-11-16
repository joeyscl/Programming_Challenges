'''Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, 
since a node can be a descendant of itself according to the LCA definition.'''

def LCA(Node, val1, val2):
	def valInTree(node, val):
		if node == None:
			return False
		elif node.val == val:
			return True
		elif node.val > val:
			return valInTree(node.left, val)
		else:
			return valInTree(node.right, val)


	if Node == None: # Only happens when both vals are not found in the tree
		return None

	elif Node.val == val1 or Node.val == val:
		if valInTree(Node, val1) and valInTree(Node,val2):
			return Node
		else: # One of the vals is not in the tree
			return None

	elif Node.val > val1 and Node.val > val2:
		LCA(node.left, val1, val2)

	elif Node.val < val1 and Node.val < val2:
		return VCA(node.right, val1, val2)

	else:
		return Node
