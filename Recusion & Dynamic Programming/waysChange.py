def waysChange (cents, denoms):

	def waysChangeHelper(cents, denoms):
		ways = 0
		denoms = sorted(denoms)
		denoms.reverse() # make denoms from largest to smallest

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
							# changes[(remainder, denoms[denomIndex+1])] = subWays
							ways += subWays
		return ways

	changes = {}	# hashtable for memoization
	return waysChangeHelper(cents,denoms)

print(waysChange(4000,[1,5,10,25]))


''' Graphical Representation of algorithm: Moving down is Iteration. Moving across is recursive call 

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