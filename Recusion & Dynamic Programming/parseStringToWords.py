'''takes input string and parses it into phrase of valid words. ie: "applepie" -> "apple pie" '''

myDict = set(['a','an','app','apple','pie','is','goo','good','dapple', 'nap','nap'])

def parseToPhrase(myStr):
	mem = {}
	def parse(myStr):
		# if myStr in mem:
		# 	return mem[myStr]
		if len(myStr) == 0:
			return ""
		elif myStr in myDict:
			return myStr
		else:
			for Len in range(1,len(myStr)):
				first = myStr[:Len]
				if first in myDict:
					rest = parse(myStr[Len:])
					if rest != None:
						# mem[rest] = first + " " + rest
						return first + " " + rest

			return None

	return parse(myStr)

print(parseToPhrase('anapplepieisgoodgoodappleapp'))
