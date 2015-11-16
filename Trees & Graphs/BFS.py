''' given a binary tree, find a given value using BFS (ie: level order traversal) '''

def BFS(head,num):

	todo = []
	node = head

	while todo != []:
		if node == None:
			node = todo[0]
			todo = todo[1:]
		else:
			if num == node.val:
				return true

			todo.append(node.left)
			todo.append(node.right)
			node = todo[0]
			todo = todo[1:]

	return False