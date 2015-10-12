''' http://www.careercup.com/question?id=5192571630387200
Given a string (for example: "a?bc?def?g"), 
write a program to generate all the possible strings by replacing ? with 0 and 1. 
Example: 
Input : a?b?c? 
Output: a0b0c0, a0b0c1, a0b1c0, a0b1c1, a1b0c0, a1b0c1, a1b1c0, a1b1c1.
'''
def gen_rec(string):
	res = []
	def gen(string,acc):
		if string == '':
			res.append(acc)
		else:
			if string[0] == '?':
				gen(string[1:],acc+'0')
				gen(string[1:],acc+'1')
			else:
				gen(string[1:],acc+string[0])

	gen(string,'')
	print(res)

def gen_iter(string):
	perms = ['']
	for ch in string:
		temp = []
		for perm in perms:
			if ch == '?':
				temp.append(perm+'0')
				temp.append(perm+'1')
			else:
				temp.append(perm+ch)

		perms = temp

	res = []
	for perm in perms:
		if len(perm) == len(string):
			res.append(perm)
	print(res)

gen_rec('a?b?c?')
gen_iter('a?b?c?')


