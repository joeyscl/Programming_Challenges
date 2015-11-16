''' http://www.careercup.com/question?id=3576940

You are given a string containing 0s and 1s. Find O(n) time and O(1) space 
algorithm to find the maximum sub sequence which has equal number of 1s and 
0s. 

Examples 
1) 10101010 
The longest sub sequence that satisfies the problem is the input itself 

2)1101000 
The longest sub sequence that satisfies the problem is 110100'''



''' We observe that any such sequence has to start from the leftmost or rightmost end
of the input string since there is always "left over" zeros or ones on either end.
We can find and compare the longest such sequence that starts from either end in O(n)'''
def longestSeq(string):

	count = 0
	fromLeft = 0
	for i in range(len(string)):
		if string[i] == '0':
			count -= 1
		else:
			count += 1

		if count == 0:
			fromLeft = i

	count = 0
	fromRight = len(string)
	for i in range(len(string))[::-1]:
		if string[i] == '0':
			count -= 1
		else:
			count += 1

		if count == 0:
			fromRight = i

	if fromLeft+1 > len(string)-fromRight:
		return string[:fromLeft+1]
	else:
		return string[fromRight:]

print(longestSeq('10101010'))
print(longestSeq('1101000'))
print(longestSeq('1100001000111'))
