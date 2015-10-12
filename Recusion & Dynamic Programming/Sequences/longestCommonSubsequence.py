'''given 2 strings, find the longest common subsequence:
ie: abcde, xbcfge -> bce'''

'''Recursion + Memoization'''
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

''' DP + tabulation'''
def LCS1(str1, str2):
	len1 = len(str1)
	len2 = len(str2)

	''' Initialize table'''
	tab = [[0]*len2 for i in range(len1)]

	#initialize first cell
	if str1[0] == str2[0]:
		tab[0][0] = str1[0]
	else:
		tab[0][0] = ""

	#initialize first column
	for i in range(1,len1):
		if str1[i] == str2[0]:
			tab[i][0] = str2[0]
		else:
			tab[i][0] = tab[i-1][0]

	#initialize first row
	for j in range(1,len2):
		if str2[j] == str1[0]:
			tab[0][j] = str1[0]
		else:
			tab[0][j] = tab[0][j-1]

	''' Actual calculations'''
	for i in range(1,len1):
		for j in range(1,len2):
			if str1[i] == str2[j]:
				tab[i][j] = tab[i-1][j-1] + str1[i]
			else:
				if len(tab[i-1][j]) > len(tab[i][j-1]):
					tab[i][j] = tab[i-1][j]
				else:
					tab[i][j] = tab[i][j-1]
	return tab[-1][-1]

print(LCS("thisisatest", "testingtesting"))
print(LCS1("thisisatest", "testingtesting"))

# str1 = "697 953 900 438 899 593 591 963 31 160 894 493 782 445 326 452 988 657 7 544 768 398 791 650 818 12 347 928 828 336 692 339 130 837 548 487 989 333 875 711 957 341 821 319 338 328 234 7 670 328 451 200 685 699 855 668 609 322 752 386 81 635 952 618 133 73 548 163 221 105 773 398 639 579 660 746 718 918 224 984 265 242 506 762 734 98 324 100 896 346 344 27 420 353 532 105 914 130 695".split()
# str2 = "438 591 768 160 777 894 782 398 445 306 326 282 452 607 241 513 185 7 544 12 347 828 336 83 924 143 692 339 130 515 837 466 989 875 711 957 338 266 305 480 328 28 7 670 328 699 849 668 609 979 100 322 283 386 655 263 826 169 635 952 618 73 238 897 221 863 34 372 732 398 579 666 545 660 794 746 526 718 918 403 615 946 224 822 242 506 734 324 100 55 346 704 24 650 678 532 914 130 423 998".split()

# print(LCS1(str1,str2))
