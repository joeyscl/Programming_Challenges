''' https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

There CAN be duplicates in the array.'''

# uses indices of array
def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    low = 0
    hi = len(nums)-1

    while True:
    	if hi - low <= 5:
    		return min(nums[low:hi+1])
    	else:
    		mid = (hi+low)//2
    		if nums[mid] > nums[hi]:
    			low = mid
    		elif nums[mid] < nums[hi]:
    			hi = mid
    		else:
    			hi -= 1

test1 = [4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
test2 = [3,3,3,3,3,3,1,2,3,3]
print(findMin(test1))
print(findMin(test2))

