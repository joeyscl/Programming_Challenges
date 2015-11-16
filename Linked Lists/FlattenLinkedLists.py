''' PIE page 53
Given this kind of struct:
struct Node {
	Node 	prev
	Node 	next
	Node 	child
	int 	val
}
flatten the web of double-linked lists
'''
import Queue
q = Queue.Queue()
def flatten1(node):
	
	while node != None:
		if node.child != None:
			q.put(node.child)

		node = node.next

	if q.empty():
		return None
	else:
		node.next = flatten(q.get())

	return node


q = Queue.Queue()
def flatten2(node,prev):
	if node == None:
		if q.empty():
			return
		else:
			nxt = q.get()
			prev.next = nxt
			flatten(nxt,prev)

	else:
		if node.child != None:
			q.put(node.child)
		
		flatten(node.next,node)