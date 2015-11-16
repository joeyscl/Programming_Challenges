''' preOrder deserialize

		A
	   / \
	  B   C   <----> [A,B,D,None,None,E,None,None,C,None,None]
	 / \
	D   E
'''

def deserialize(arr):
	global idx
	idx = 1

	def helper(prev, leftAssigned):
		global idx

		if idx >= len(arr):
			return

		elif arr[idx] == None:
			if not leftAssigned:
				prev.left = None
				idx += 1
				helper(prev, True)
			else:
				prev.right = None
				idx += 1
				return
		else:
			if not leftAssigned:
				prev.left = arr[idx]
				idx += 1				
				helper(prev.left, False)				
				helper(prev, True)
			else:
				prev.right = arr[idx]
				idx += 1
				helper(prev.right, False)

	helper(arr[0],False)


	''' preOrder deserialize

		A
	   / \
	  B   C   <----> [A,B,D,None,None,E,None,None,C,None,None]
	 / \
	D   E
'''


