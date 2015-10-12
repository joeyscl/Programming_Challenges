'''http://www.careercup.com/question?id=14974673
McDonald’s sells Chicken McNuggets in packages of 6, 9 or 20 McNuggets. 
Thus, it is possible, for example, to buy exactly 15 McNuggets (with one package of 6 and a second package of 9), 
but it is not possible to buy exactly 16 McNuggets, 
since no non- negative integer combination of 6's, 9's and 20's add up to 16. 
To determine if it is possible to buy exactly n McNuggets, 
one has to find non-negative integer values of a, b, and c such that 
6a+9b+20c=n 
Write a function, called McNuggets that takes one argument, n, 
and returns True if it is possible to buy a combination of 6, 9 and 20 pack units 
such that the total number of McNuggets equals n, and otherwise returns False.'''

def nuggets(nugs, denoms):

	if nugs == 0:
		return True

	if denoms == []:
		return False
	
	for i in range(len(denoms)):
		if denoms[i] > nugs:
			break
		for boxes in range( nugs//denoms[i] + 1):
			rem = nugs - boxes*denoms[i]
			if nuggets(rem, denoms[1:]):
				return True

	return False

print(nuggets(16,[6,9,20]))

