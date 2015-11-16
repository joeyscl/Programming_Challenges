''' http://www.careercup.com/question?id=5757635703865344

1. Balanced Parentheses 
Given a string s of parentheses (ex: “(()”), return the minimum number of parentheses 
that need to be inserted to make it into a well formed string 
A well formed (balanced) string of parentheses is defined by the following rules: 

● The empty string is well formed. 
● If s is a well formed string, (s) is a well formed string. 
● If s1 and s2 are well formed strings, their concatenation s1s2 is a well formed string. 
'''

def minBrackets(string):
	
	balance = 0 		# open paran - close paran (let this >= 0)
	unbalancedLefts = 0 # number of close parans when balance is 0

	for ch in string:
		if ch == '(':
			balance += 1
		else:
			if balance > 0:
				balance -= 1
			else:
				unbalancedLefts += 1

	return balance + unbalancedLefts

print(minBrackets('()'))
print(minBrackets(')'))
print(minBrackets('('))
print(minBrackets(')('))
print(minBrackets(')(()('))
