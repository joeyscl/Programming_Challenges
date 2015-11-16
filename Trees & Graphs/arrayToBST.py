''' Given a sorted array, return a balanced BST '''

def arrayToBST(arr):

	def helper(start,end):
		if start == end:
			return Node(arr[start])

		elif end-start == 1:
			parent = Node(arr[start])
			parent.right = Node(arr[end])
			return parent

		else:
			mid = (start+end)//2
			parent = Node(arr[mid])
			parent.left = helper(start, mid-1)
			parent.right = helper(mid+1, end)
			return parent