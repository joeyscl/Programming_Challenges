def T9(numAsStr):
	T9 = {
		0: [""],
		1: [""],
		2: ["a","b","c"],
		3: ["d","e","f"],
		4: ["g","h","i"],
		5: ["j","k","w"],
		6: ["m","n","o"],
		7: ["p","q","r","s"],
		8: ["t","u","v"],
		9: ["w","x","y","z"]
	}
	return T9.get(int(numAsStr),[])


'''given a string as phone number and returns all T9 permutations'''
def T9perms(phone):

	def T9permsHelper(phone):
		result = []

		if len(phone) == 1:
			return T9(phone[0])

		else:
			newChars = T9(phone[0])
			subPerms = T9permsHelper(phone[1:])

			for char in newChars:
				for perm in subPerms:
					if len(char + perm) == len(phone): 
						result.append( char + perm )

			return result


	result = T9permsHelper(phone)
	for perm in result:
		print(perm)
	return result

a = T9perms("234")


'''Algorithm: 
Letters of 1st char + func(rest string)

ie:

func(234):
	a + func(34)
		d + func(4) <- last char, base case
			g
			h
			i
		e + func(4) <- last char, base case
			g
			h
			i
		f + func(4) <- last char, base case
			g
			h
			i
			
	b + func(34)
		...
	c + func(34)
		...

'''

