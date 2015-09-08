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


'''given a string as phone number, return all T9 permutations'''
def T9perms(phone):

	result = ['']

	for num in phone:
		newPerms = []
		newChars = T9(num)

		for char in newChars:
			for perm in result:
				newPerms.append( perm+char )

		result = newPerms

	# print nicely
	for perm in result:
		print(perm)
	return result

T9perms("234")

'''Algorithm:

Iterate through each number and combine T9 chars of that number with existing results. Append that number to newResults. Set existing results = newResults.

ie:
For each number in the phone #:
	for each associated Char in number:
		for each perm in results:
			append (perm + Char) to newResults.
		results = newResults

ie:

func(234):
	a +	1st of T9(3) +	1st of T9(4)
						2nd of T9(4)
						3rd of T9(4)

	a + 2nd of T9(3) +	1st of T9(4)
						2nd of T9(4)
						3rd of T9(4)
	a + 3rd of T9(3) +	...
						...
						...

	b + 1st of T9(3) +	...
						...
						...
	...

	c + 3rd of T9(3) +	...
						...
						...

'''