''' takes an array of coin values, denoms, and returns the least numer of coins required to make cents'''
def leastChange(cents,denoms):
	denoms = sorted(denoms) # sort denoms into increasing order

	changes = [0]*(cents+1) #initialize 'changes' which is our "previous results" array
 
	for val in range(1,cents+1): #if the value is one of the denoms, it requires only 1 coin
		if val in denoms:
			changes[val] = 1
			continue

		# find val - denom[x] that yields least number of coins. Use 'changes', which are previous results
		remainder = val
		coins = 0
		for denom in denoms:
			if remainder - denom < 0:
				break
			if coins == 0 or changes[remainder-denom] < coins:
				coins = 1 + changes[remainder-denom]

		changes[val] = coins

	# print(changes)
	return changes[-1]

print(leastChange(63, [1,5,10,21,25]))

''' Algorithm: build array of least coins required to make X change by comparing coins required to make (X - values of denoms)
ie: Make 15 cents from [1,5,10]
	15 - 1 = 14. 5 coins required to make 14 (previously computed)
	15 - 5 = 10. 1 coins required to make 10 (previously computed)
	15 - 10 = 5. 1 coins required to make 5  (previously computed)

	Best is 1. So total 1 + 1 = 2 coins required to make 15
'''