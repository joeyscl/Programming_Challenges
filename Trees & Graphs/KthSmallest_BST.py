''' https://leetcode.com/problems/kth-smallest-element-in-a-bst/
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
'''

def kThSmallest(Node, k, count):
	# using in-order traversal
	if Node == None:
		return None

	else:
		left = kThSmallest(Node.left, k, count)
		if left != None:
			return left
		
		count += 1
		if count == k:
			return Node.val

		else:
			return kthSmallest(Node.right, K, count)

ex: print(kThSmallest(root, some K, 0))


''' A
   / \
  B   C

Test Input: node A, 2, 0		Expected output: A

Node: A
	left = kthSmallest(Node.left, 2, 0)

		Node: B
			left = kthSmallest(Node.left, 2, 0)
			left = None

			count += 1	;	k != count (1 != 2)

			return kthSmallest(Node.right, 2, 1)-> return None

	left = None

	count += 1 ; k == count (2 == 2)
	return A
'''





