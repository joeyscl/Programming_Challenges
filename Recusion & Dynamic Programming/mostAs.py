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
      P = As[i-1]+copied[i-1]  # 'copied' doesn't change; smallest valule
      SCP = As[i-3]*2          # result in largest new 'copied' value
      SCPP = As[i-4]*3
      if P > SCP and P > SCPP:  # P largest
        As[i] = P
        copied[i] = copied[i-1]
      elif SCPP > SCP:          # SCPP largest
        As[i] = SCPP
        copied[i] = As[i-4]
      else:
        As[i] = SCP             # SCP largest
        copied[i] = As[i-3]
        
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
			res = helper(num-3,0+3,0)	# We always start with at least 3 'A's
			mem[(num, 0, 0)] = res
			return res

	return helper(num,0,0)

print(mostAs_Rec(17))
print(mostAs_DP(17))
