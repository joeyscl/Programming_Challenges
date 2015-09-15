class Node (object):

	def __init__(self, val):
		self._left = None
		self._right = None
		self._val = val

	def _get_val(self):
		if self == None or self._val == None:
			return None
		else:
			return self._val

	def _get_left(self):
		if self._left == None or self._left._val == None:
			return None
		else:
			return self._left

	def _get_right(self):
		if self._right == None or self._right._val == None:
			return None
		else:
			return self._right


