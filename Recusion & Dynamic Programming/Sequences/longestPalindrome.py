''' given a string, return the longest substring that is a palindrome --- test cases at very bottom'''

''' O(n^3)'''
''' find all start:end pairs and check if they're palindromes. return longest'''
def bruteForce(string):
	def isPalindrome(string):
		return string == string[::-1]

	best = ''
	for i in range(len(string)):
		for j in range(i,len(string)+1):
			if isPalindrome(string[i:j]) and len(string[i:j]) > len(best):
				best = string[i:j]
	return best

''' O(n^2)'''
''' finds longest palindrome centering around each index. return longest'''
def DP(string):

	#place $ around every character to handle even-length cases
	temp = '$'
	for ch in string:
		temp += (ch.lower()+'$')
	string = temp

	'''returns longest palindrome that centers around a specific index'''
	def expand(mid):
		low = mid
		hi = mid
		while low >= 0 and hi < len(string):
			if string[hi] == string[low]:
				hi += 1
				low -= 1
			else:
				break

		return string[low+1:hi]

	best = ''
	for i in range(len(string)):
		pali = expand(i)
		if len(pali) > len(best):
			best = pali
	return best.replace('$','')

''' O(n) aka: Manachar's algorithm'''
def manacher(string):

	''' return *length* of palindrome centered around given index'''
	def expand(mid):
		low = mid
		hi = mid
		while low >= 0 and hi < len(string):
			if string[hi] == string[low]:
				hi += 1
				low -= 1
			else:
				break

		return hi-low-1

	#place $ around every character to handle even-length cases
	temp = '$'
	for ch in string:
		temp += (ch.lower()+'$')
	string = temp

	# actual algorithm below
	lens = [0]*len(string)	# the lengths of palindrome at each index
	mid = 0

	while mid <= len(string)-1:
		lens[mid] = expand(mid)
		leftEdge = mid - lens[mid]//2	# start index of palindrome centered around mid, inclusive
		rightEdge = mid + lens[mid]//2	# end index of palindrome centered around mid, inclusive
		newMid = False	# used as flag for re-assigning value of mid

		if rightEdge >= len(string)-1:
			break

		for i in range(1, lens[mid]//2 + 1):
			toEdge = (mid-i) - leftEdge

			if lens[mid-i]//2 < toEdge:		# case 1: palindrome is bounded by the palindrome around mid. Copy value
				lens[mid+i] = lens[mid-i]

			elif lens[mid-i]//2 > toEdge:	# case 2: palindrome exceed boundary. Length is up to bound.
				lens[mid+i] = toEdge*2 + 1

			else:							# case 3: end right at boundary. Found new 'mid' 
				newMid = True
				mid += i
				break

		if not newMid:
			mid = rightEdge+1

	length = max(lens)
	mid = lens.index(length)//2
	string = string.replace('$','')
	leftEdge = mid - length//4
	rightEdge = mid + length//4


	return string[leftEdge:rightEdge+1]



test0 = 'abba'
test1 = 'abaxabaxabybaxabyb'
test2 = 'FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'
 
tests = [test0,test1,test2]
for t in tests:	
	print(bruteForce(t))
	print(DP(t))
	print(manacher(t))
	print('')


