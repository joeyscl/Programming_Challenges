'''given a computer user can press 'a', 'select all', 'copy', and 'paste',
determine the maximum number of a's an user can output on the screen given N
number of keystrokes'''

''' O(n) '''
def mostAs_DP(n):
  As = [0,1,2,3,4,5] + [0]*(n-5)
  copied = [1,1,1,1,1,1] + [0]*(n-5)

  if n <= 5:
    return As[n]
  else:
    for i in range(6,n+1):
      if As[i-3]*2 >= As[i-1]+copied[i-1]:
        As[i] = 2*As[i-3]
        copied[i] = As[i-3]
      else:
        As[i] = As[i-1] + copied[i-1]
        copied[i] = copied[i-1]
        
  # print(As)
  # print(copied)        
  return As[-1]

''' Not as Good. ~O(N^2)? '''
def mostAs_Rec(num):
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
			res = max(helper(num-3,printed*2,printed), helper(num-1,printed+copied,copied))
			mem[(num, printed, copied)] = res
			return res

		else: # printed == 0, copied == 0
			best = 0
			for i in range(1,num+1):
				curr = helper(num-i,0+i,0)
				best = max(best,curr)
			mem[(num, 0, 0)] = best
			return best

	return helper(num,0,0)

print(mostAs_Rec(20))
