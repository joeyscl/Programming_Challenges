'''given a computer user can press 'a', 'select all', 'copy', and 'paste',
determine the maximum number of a's an user can output on the screen given N
number of keystrokes'''


def mostAs(num):
	mem = {}
	def helper(num, printed, copied):
		if (num, printed, copied) in mem.keys():
			return mem[(num, printed, copied)]
		elif num <= 6 and printed == 0:
			return num

		elif num < 3:
			return printed + num * copied

		elif num >= 3 and printed != 0:
			#compare select-copy-paste whole thing vs paste existing clipboard
			mem[(num, printed, copied)] = max(helper(num-3,printed*2,printed), helper(num-1,printed+copied,copied))
			return mem[(num, printed, copied)]

		else: # printed == 0, copied == 0
			best = 0
			for i in range(1,num+1):
				curr = helper(num-i,0+i,0)
				best = max(best,curr)
			mem[(num, 0, 0)] = best
			return best

	return helper(num,0,0)

print(mostAs(20))