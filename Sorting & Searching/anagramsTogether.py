import collections

'''Takes list of strings and returns a list such that anagrams are neighboring'''
def anagramsTogether(myStrings):

	myAnams = collections.OrderedDict() 	# a set to hold "histogram" of the letters (ie: for a given string, a count of each letter)
					# ie: "abc" and "cab" would both the same key of (1,1,1,0,0...)
					# values are a list of the original string
	
	for word in myStrings:
		key = [0] * 26
		for char in word.lower().replace(" ", ""): #change to lowercase and remove spaces
			key[ord(char)-ord('a')] += 1	# increase count of Nth char from 'a' by 1
		key = tuple(key)	# turn key into tuple so we can hash it (lists, which are mutable cannot be used as key)
		
		if key not in myAnams.keys():
			myAnams[key] = [word]
		else:
			myAnams[key].append(word)

	results = []
	for anams in myAnams.values(): #iterate through values, which are lists of words that are anagrams
		for word in anams:
			print(word)
			results.append(word)

	return results

anagramsTogether(["abc","xyz","cab","zxy","debit card","apple","Bad Credit"])

'''Algorithm:

For each string, create an array that counts number of each letter.
	ie: "abe" and "bae" would result in the same array [1,1,0,0,1,0,0...]
Use the array as key for hashtable, append string into value
	ie: for input ["abe", "abcd" ,"bae"] will result in the following hashtable:
			
			hashtable:
			{
				(1,1,0,0,1,0,0...) -> ["abe", "bae"]
				(1,1,1,1,0,0,0...) -> ["abcd"]
			}

Finally combine all values into a single array.
'''