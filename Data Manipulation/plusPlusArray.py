'''http://www.careercup.com/question?id=14370695

Implement the plusplus operator when we are getting the input as integer array. 
ie: [9,9,9,9] ---> [1,0,0,0,0] '''

''' "cheating" way of doing it with list comprehension '''
def cheat(arr):
	arr = [str(num) for num in arr]
	string = ''
	for ch in arr:
		string += ch

	stringPP = str(int(string)+1)
	return [int(ch) for ch in stringPP]

''' how they probably wanted you to do it '''
def plusPlus(arr):
	arr = [0]+arr

	arr[-1] += 1
	for i in range(len(arr))[::-1]:
		if arr[i] == 10:
			arr[i] = 0
			arr[i-1] += 1
		else:
			pass

	if arr[0] == 0:
		return arr[1:]
	else:
		return arr


print(cheat([9,9,9,8]))
print(plusPlus([9,9,9,8]))

print(cheat([9,9,9,9]))
print(plusPlus([9,9,9,9]))

