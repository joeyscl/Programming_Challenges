''' https://leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays nums1 and nums2 of size m and n respectively. 
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).'''

''' assume arr1 and arr2 are equal size '''
def findMedian(arr1,arr2):
	low1 = 0
	low2 = 0
	hi1 = len(arr1)-1
	hi2 = len(arr2)-1

	while True:
		mid1 = (hi1+low1)//2
		mid2 = (hi2+low2)//2

		print(arr1[low1:hi1+1],arr2[low2:hi2+1])

		if arr1[mid1] == arr2[mid2]:
			return arr1[mid1]

		elif hi1-low1 == 1 or hi2-low2 == 1:
			return (max(arr1[low1],arr2[low2]) + min(arr1[hi1],arr2[hi2])) // 2

		elif arr1[mid1] < arr2[mid2]:
			low1 = mid1
			hi2 = mid2

		else:
			hi1 = mid1
			low2 = mid2

a1 = [1, 12, 15, 26, 38]
a2 = [2, 13, 17, 30, 45]
combined = [1,2,12,13,15,17,26,30,38,45]
print (findMedian(a1,a2))

