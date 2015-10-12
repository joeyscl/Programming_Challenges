'''Write a function that returns whether a path of a given sum through a binary tree exists.'''

def sumInPath(head, target):
	sums = set(target)

	def search(curr, sums):
		if 0 in sums:
			return True
		elif curr == None:
			return False
		else:
			newSums = set(num-curr.val for num in sums if num-curr.val >= 0)
			newSums.add(target)
			return search(curr.left, newSums) or search(curr.right, newSums)

	return(search(head,sums))