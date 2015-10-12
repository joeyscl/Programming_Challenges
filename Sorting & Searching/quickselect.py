from random import randint
def quickselect(arr,index):

	k = index

	def qs(low, hi):		
		temp = randint(low,hi)
		arr[temp], arr[hi] = arr[hi], arr[temp]
		pivot = arr[hi]

		i = low
		j = hi-1

		while True:
			if i > j:
				break
			else:
				if arr[i] <= pivot:
					i += 1
				else:
					arr[i], arr[j] = arr[j], arr[i]
					j -= 1

		arr[hi], arr[i] = arr[i], arr[hi]
		print(arr)

		if i == k:
			return arr[i]
		elif i > k:
			return qs(low,i-1)
		else:
			return qs(i+1,hi)


	return qs(0,len(arr)-1)

print(quickselect([6,7,9,2,5,0,3,1,8,4],5))
		

