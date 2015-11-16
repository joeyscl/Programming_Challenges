'''
Given a linked list and a number x, 
partition the linked list such that no nodes smaller than x are to the right of nodes with value x, 
and no nodes with values larger than x are to the left of nodes with value x.

assume a linked list node has the fields:

node 	next
int		val

'''

''' O(n) memory solutions '''
def sortLL(node, val):

	greater = []
	equal = []
	lesser = []

	''' "bin" the nodes that are greater, equal, or lesser '''
	while node != None:
		if node.val > val:
			greater.append(node)
		elif node.val < val:
			lesser.append(node)
		else:
			equal.append(node)

	''' connect all the nodes that are greater, equal, or lesser '''
	prev = greater[0]		# the head node of greater
	for node in greater[1:]:
		prev.next = node
		prev = node

	prev = equal[0]			# the head node of equal
	for node in equal[1:]:
		prev.next = node
		prev = node

	prev = lesser[0]		# the head node of lesser
	for node in equal[1:]:
		prev.next = node
		prev = node

	''' connect everything together '''
	lesser[-1].next = equal[0]
	equal[-1].next = greater[0]
	greater[-1] = None

	return lesser[0]	# return 1st lesser node as head


def sortLL1(node, val):

	lesserHead = None
	lesserTail = None

	equalHead = None
	equalTail = None

	greaterHead = None
	greaterTail = None

	while node != None:
		if node.val < val:
			if lesserHead == None:
				lesserHead = node
				lesserTail = node
			else:
				lesserTail.next = node
				lesserTail = node

		elif node.val > val:
			if greaterHead == None:
				greaterHead = node
				greaterTail = node
			else:
				greaterTail.next = node
				greaterTail = node

		else:
			if equalHead == None:
				equalHead = node
				equalTail = node
			else:
				equalTail.next = node
				equalTail = node

	lesserTail.next = equalHead
	equalTail.next = greaterHead
	greaterTail.next = None

	return lesserHead