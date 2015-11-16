''' given a sorted array that has been shifted. ie: [4,5,6,7,1,2,3]
return the index of a given integer. Return -1 if not found '''

def findVal(arr,num):
	low = 0
	hi = len(arr)-1

	while True:
		if hi - low <= 10:
			if num in arr[low:hi+1]:
				return low + arr[low:hi+1].index(num)
			else:
				return -1

		mid = (hi+low)//2
		if arr[mid] == num:
			return mid
		elif arr[mid] < arr[hi]:
			if num > arr[mid] and num < arr[hi]:
				low = mid+1
			else:
				hi = mid-1
		else:
			if num > arr[low] and num < arr[mid]:
				hi = mid-1
			else:
				low = mid+1

test = [266,267,268,269,271,278,282,292,293,298,6,9,15,19,21,26,33,35,37,38,39,46,49,54,65,71,74,77,79,82,83,88,92,93,94,97,104,108,114,115,117,122,123,127,128,129,134,137,141,142,144,147,150,154,160,163,166,169,172,173,177,180,183,184,188,198,203,208,210,214,218,220,223,224,233,236,241,243,253,256,257,262,263]
num = 208

print(findVal(test,num))