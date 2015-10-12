''' given 2 strings, determine the min number of edits (delete, insert, substitute) required to 
turn one string into the other'''
'''aka Levenshtein distance'''

def dp(str1,str2):
	tab = [[0]*len(str2) for i in range(len(str1))]

	tab[0] = [j for j in range(len(str2))]

	for i in range(len(str1)):
		tab[i][0] = i

	for i in range(1,len(str1)):
		for j in range(1,len(str2)):
			tab[i][j] = min(tab[i-1][j-1], tab[i-1][j], tab[i][j-1]) + (str1[i]!=str2[j]) # +1 if different character

	return(tab[-1][-1])


def rec(str1,str2):
	mem = {}
	def helper(str1, str2):
		if (str1,str2) in mem.keys():
			return mem[(str1,str2)]

		elif str1 == "" or str2 == "":
			mem[(str1,str2)] = max(len(str1),len(str2))
			return max(len(str1),len(str2))

		else:
			x = rec(str1[1:], str2[1:]) + (str1[0]!=str2[0]) # +1 if first character is same

			if len(str1) > len(str2):
				y = helper(str1[1:], str2) + 1
			else:
				y = helper(str1, str2[1:]) + 1

			mem[(str1,str2)] = min(x,y)
			return min(x,y)

	return helper(str1,str2)

print(dp('abc','axbycz'))
print(rec('abc','axbycz'))