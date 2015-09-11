'''given 2 strings, find the longest common subsequence:
ie: abcde, xbcfge -> bce'''

'''This returns the subsequence'''
def LCS(str1, str2):
	mem = {}
	def helper(idx1,idx2):
		if (idx1,idx2) in mem.keys():
			return mem[(idx1,idx2)]

		elif idx1 == -1 or idx2 == -1:
			return ""

		elif str1[idx1] == str2[idx2]:
			s = helper(idx1-1,idx2-1)+str1[idx1]
			res = s

		else:
			s1 = helper(idx1-1,idx2)

			s2 = helper(idx1,idx2-1)

			if len(s1) > len(s2):
				res = s1
			else:
				res = s2

		mem[(idx1,idx2)] = res
		return res

	return helper(len(str1)-1,len(str2)-1)

print(LCS("thisisatest", "testing123testing"))