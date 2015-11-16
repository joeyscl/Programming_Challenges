''' given a string that is a setence, reverse the sentence
ie: "I am dog" -> "dog am I" '''

''' the "cheating" way using python list comprehension '''
def revSentence1(string):

	arr = string.split()
	arr = [word for word in reversed(arr)]

	res = ''
	for word in arr[:-1]:
		res += word + " "
	res += arr[-1]
	return res

''' how they probably wanted you to do it '''

def revSentence2(string):
	res = ""
	word = ""
	prev = "" # track previous ch; used to get rid of multiple spaces
	for ch in string[::-1]:
		if ch == " ":
			if prev != " ":
				res += word[::-1] + " "
				word = ""
				prev = " "
			else:
				pass
		else:
			word += ch
			prev = ch
	res += word

	return res

print(revSentence1("I  am  dog"))
print(revSentence2("I  am  dog"))