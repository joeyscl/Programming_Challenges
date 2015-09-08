# Reverse linkedlist using tail recursion

def reverse(HeadNode):

	if HeadNode == None:
		return

	curr = HeadNode
	next = head.Next()
	curr.setNext(None)

	if next != None:
		reverseHelper(curr, next)
	else:
		return
		

def reverseHelper(prev, curr):
	next = curr.next()
	curr.setNext(prev)

	if next == None: #next is null, so curr is the tail of linked list
		return
	else:
		reverseHelper(curr, next)



