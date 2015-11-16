''' https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.'''

# uses indices of array
def findMin1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 5:
    	return min(nums)

    arr = nums + nums
    low = 0
    hi = len(arr)-1
    while True:
        mid = (low + hi)//2
        if arr[mid] < arr[mid+1] and arr[mid] < arr[mid-1]:
            return mid % len(nums)
        elif arr[mid] < arr[mid+1]:
            low = mid
        else:
            hi = mid

# uses array
def findMin2(nums):
	arr = nums
	low = 0
	hi = len(arr)-1

	while True:
		mid = (low + hi)//2
		if arr[mid] <= arr[mid+1] and arr[mid] <= arr[mid-1]:
			return mid
		elif arr[mid] > arr[low]:
			low = mid
		else:
			hi = mid 

    
print(findMin1([4,5,6,7,0,1,2]))
print(findMin2([4,5,6,7,0,1,2]))