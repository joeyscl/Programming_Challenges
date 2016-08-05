''' Find the number of ways to break change given cents and denominations'''

''' DP is actually slower in this problem'''
def ways_DP(cents, denoms):
	denoms = sorted(denoms)
	tab = [[0]*(cents+1) for i in range(len(denoms))]

	for j in range(cents+1):
		if j % denoms[0] == 0:
			tab[0][j] = 1

	for i in range(len(denoms)):
		tab[i][0] = tab[0][0]

	for i in range(1,len(denoms)):
		for j in range(1,cents+1):
			ways = tab[i-1][j]
			for x in range(1, j//denoms[i] + 1):	
				rem = j - x*denoms[i]
				ways += tab[i-1][rem]
			tab[i][j] = ways

	for x in tab:
		print(x)

	return(tab[-1][-1])

''' recursion + memoization is faster'''
def ways_rec (cents, denoms):

	denoms = sorted(denoms)
	denoms.reverse() # make denoms from largest to smallest
	changes = {}	# hashtable for memoization

	def waysChangeHelper(cents, denoms):
		ways = 0
		
		if cents == 0:
			return 1
		else:
			for denomIndex in range(len(denoms)):
				denom = denoms[denomIndex]
				for count in range( 1, cents//denom +1 ):
					if denom == denoms[-1]:
						ways += 1
						break
					else:
						remainder = cents - denom*count

						# use results if it is already in hashtable
						if (remainder, denoms[denomIndex+1]) in changes.keys():
							ways += changes[(remainder, denoms[denomIndex+1])]

						else: # not in hashtable, need to compute
							subWays = waysChangeHelper(remainder, denoms[denomIndex+1:])
							changes[(remainder, denoms[denomIndex+1])] = subWays
							ways += subWays
		return ways

	res = waysChangeHelper(cents,denoms)
	return res

print(ways_DP(10,[1,5,10,25]))
# print(ways_rec(10000,[1,5,10,25]))


''' Graphical Representation of recursive algorithm: Moving down is Iteration. Moving across is recursive call 

25	
	- 1 x 25

	- 1 x 10	- 3 x 5 	- 0 x 1 base case
				- 2 x 5 	- 5 x 1 base case
				- 1 x 5 	- 10x 1 base case

	- 2 x 10 	- 1 x 5 	base case
				- 5 x 1 	base case

	- 5 x 5 	- base case

	- 4 x 5 	- 5 x 1 	base case

	- 3 x 5 	- 10x 1 	base case

	- 2 x 5 	- 15x 1 	base case

	- 1 x 5 	- 20x 1 	base case

	- 25 x 1 basecase
'''