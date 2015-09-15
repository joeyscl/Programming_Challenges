import BinaryTree

class Node (BinaryTree.Node):

	def __init__(self, val):
		BinaryTree.Node.__init__(self,val)

	def _insert(self,val):
		curr = self
		while curr != None:
			if val <= curr._get_val() :
				if curr._get_left() == None:
					curr._left = Node(val)
					return
				else:
					curr = curr._get_left()
			else:
				if curr._get_right() == None:
					curr._right = Node(val)
					return
				else:
					curr = curr._get_right()

	def _delete(self,val):
		curr = self
		while curr != None:
			if val < curr._get_val():
				if curr._get_left() == None:
					return
				else:
					curr = curr._get_left()

			elif val > curr._get_val():
				if curr._get_right() == None:
					return
				else:
					curr = curr._get_right()
			else:
				curr._val = None
				return
				
'''
head = Node(10)
head._insert(5)
print(head._get_left()._get_val())
head._delete(5)
print(head._left._get_val())
'''