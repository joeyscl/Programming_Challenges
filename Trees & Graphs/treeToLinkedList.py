''' Given a binary tree, convert it to a doubly linked list *IN-PLACE* and return the head '''

def convert(head):
	prev = None

	def connect(curr, prev):
		curr.left = prev
		if prev != None:
			prev.right = curr
		prev = curr

 	def inorder(curr):
 		if curr == None:
 			return
 		else:
 			inorder(curr.left)
 			connect(curr,prev)
 			inorder(curr.right)

 	inorder(head)
 	return head