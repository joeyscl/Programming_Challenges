'''http://www.careercup.com/question?id=14539805

Three strings say A,B,C are given to you. Check weather 3rd string is interleaved from string A and B. 
Ex: A="abcd" B="xyz" C="axybczd". answer is yes. o(n)
'''

''' O(n) solution if str1 and str2 have no same characters '''
def interleaved(str1,str2,str3):

	''' check same if str3 is anagram of str1+str2 '''
	combinedTab = [0] * 26
	str3Tab = [0] * 26

	for ch in str1:
		combinedTab[ord(ch)-ord('a')] += 1

	for ch in str2:
		combinedTab[ord(ch)-ord('a')] += 1

	for ch in str3:
		str3Tab[ord(ch)-ord('a')] += 1

	if combinedTab != str3Tab:
		return False

	''' now check if letters in str1 and str2 ordered correctly within str3 '''
	k = 0
	for ch in str1:
		while True:
			if k >= len(str3):
				return False
			if ch == str3[k]:
				break
			else:
				k += 1

	k = 0
	for ch in str2:
		while True:
			if k >= len(str3):
				return False
			if ch == str3[k]:
				break
			else:
				k += 1

	return True

''' O(2^n) recursive solution for if str1 and str2 have same characters '''
def rec(str1,str2,str3):

	def helper(str1,str2,str3):
		if str1 == '':
			str1 = '$'
		if str2 == '':
			str2 = '$'
		if str3 == '':
			str3 = '$'

		# print(str1,str2,str3)

		if (str1 == '$' or str1 == '') and (str2 == '$' or str2 == '') \
		and (str3 == '$' or str3 == ''):
			return True
		elif str1[0] == str3[0] and str2[0] != str3[0]:
			return helper(str1[1:],str2,str3[1:])
		elif str2[0] == str3[0] and str1[0] != str3[0]:
			return helper(str1,str2[1:],str3[1:])
		elif str1[0] == str3[0] and str2[0] == str3[0]:
			return helper(str1[1:],str2,str3[1:]) or helper(str1,str2[1:],str3[1:])
		else:
			return False

	if len(str1)+len(str2) != len(str3):
		return False
	else:

		res = helper(str1,str2,str3)
		return res

''' DP solution O(n*m) '''
def DP (s1,s2,s3):

	s1 = " " + s1
	s2 = " " + s2
	s3 = " " + s3

	tab = [[0]*(len(s2)) for i in range(len(s1))]

	if s1[1] == s3[1]:
		tab[0][1] = 1

	if s2[1] == s3[1]:
		tab[1][0] = 1

	for i in range(1,len(tab)):
		for j in range(1,len(tab[0])):
			if (s1[i] == s3[i+j-1] or s2[j] == s3[i+j-1]) and (tab[i-1][j] == 1 or tab[i][j-1] == 1):
				tab[i][j] = 1

	return tab[-1][-1] == 1



print(rec("axbcd","xyz","axxybczd"))
print(DP("axbcd","xyz","axxybczd"))

