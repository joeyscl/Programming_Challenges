'''given 2 strings, find the longest common subsequence:
ie: abcde, xbcfge -> bce'''

'''This returns just length'''
def LCSLen(str1, str2):

	res = {}
	def helper(idx1,idx2):

		if idx1 == -1 or idx2 == -1:
			return 0

		elif str1[idx1] == str2[idx2]:
			if (idx1, idx2) in res.keys():
				return res[(idx1, idx2)]				
			else:
				val = helper(idx1-1, idx2-1)
				res[(idx1, idx2)] = 1 + val
				return 1 + val
		else:
			if ((idx1-1),idx2) in res.keys():
				val1= res[((idx1-1),idx2)]
			else:
				val1 = helper((idx1-1),idx2)
				res[((idx1-1),idx2)] = val1


			if (idx1,(idx2-1)) in res.keys():
				val2 = res[(idx1,(idx2-1))]
			else:
				val2 = helper(idx1,(idx2-1))
				res[(idx1,(idx2-1))] = val2

			return max(val1,val2)

	maxLen = helper(len(str1)-1,len(str2)-1)
	return maxLen

'''This returns the subsequence'''
def LCS(str1, str2):
	res = {}
	def helper(idx1,idx2):
		if idx1 == -1 or idx2 == -1:
			return ""

		elif str1[idx1] == str2[idx2]:
			if (idx1, idx2) in res.keys():
				return res[(idx1, idx2)]
			else:
				s = helper(idx1-1,idx2-1)+str1[idx1]
				res[(idx1, idx2)] = s
				return s
		else:
			if (idx1-1,idx2) in res.keys():
				s1 = res[(idx1-1,idx2)]
			else:
				s1 = helper(idx1-1,idx2)
				res[(idx1-1,idx2)] = s1

			if (idx1,idx2-1) in res.keys():
				s2 = res[(idx1,idx2-1)]
			else:
				s2 = helper(idx1,idx2-1)
				res[(idx1,idx2-1)] = s2

			if len(s1) > len(s2):
				return s1
			else:
				return s2

	return helper(len(str1)-1,len(str2)-1)

print(LCS("thisisatest", "testing123testing"))