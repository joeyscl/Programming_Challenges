'''http://www.careercup.com/question?id=16759664
You have k lists of sorted positive integers. Find the smallest range that includes at least one number from each of the k lists. 
Assume all numbers are unique

For example, 
List 1: [4, 10, 15, 24, 26] 
List 2: [0, 9, 12, 20] 
List 3: [5, 18, 22, 30] 

The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2, and 22 from list 3.'''
from sys import maxsize
def func(*lists):

	combined = []
	for i in range(len(lists)):
		for num in lists[i]:
			combined.append((num,i))

	combined = sorted(combined)
	print(combined)

	best = (0 , maxsize)
	for i in range(len(combined)):
		
		j = i
		flags = {}	# Key: index of lists. Val: actual value. IE: Key: combined[x][1], Val: combined[x][0]
		print('')
		while j <= len(combined):

			#check if encountered at least 1 number from each list
			containsAll = True
			for k in range(len(lists)):
				if k not in flags.keys():
					containsAll = False
					break

			if containsAll:
				M = max(flags.values())
				m = min(flags.values())
				print(m,M)
				if (M - m) < (best[1]-best[0]):
					best = (m, M)
				break
			else:
				if j >= len(combined):
					break
				else:
					flags[combined[j][1]] = combined[j][0]
					print(j,flags)
					j += 1
	return(best)

print(func([4, 10, 15, 24, 26,29],[0, 9, 12, 20, 31],[5, 18, 22, 30]))

''' Algorithm:
build a combined sorted array of tuples- (actual value, index of input list the value is from)
it represents the following

	 0	1	2	3	4	5	6	7	8	9	10	11	12	13	14

0	[	4, 			10, 	15, 			24,	26,	29] 
1	[0,			9, 		12, 		20,						31] 
2	[		5, 					18, 	22,				30]

Try to build an interval starting from each value. We can only build an interval if we have encountered
a value from each list. Use hashtable to track.
Using the above example, the various intervals are:
(0,5)
(4,9)
(5,10)
(9,18)
(10,18)
(12,18)
(15,20)
(18,24)
(20,24)
(22,31)
(24,31)
(26,31)
(29,31)
'''






