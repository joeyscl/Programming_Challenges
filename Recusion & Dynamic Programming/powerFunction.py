''' implement the power function with O(nLogn) time complexity and O(1) space complexity '''

def powerFunction(x, y): #calculate x^y
	if y == 0:
		return 1
	else:
		total = x
		power = 1
		rem = y - power
		while  rem >= power:
			print(total,power)
			total *= total
			power *= 2
			rem = y - power
		return total * powerFunction(x, rem)

print(powerFunction(2,10))
