'''https://leetcode.com/problems/largest-divisible-subset/

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

ie: [3,4,16,8] ---> [4,8,16]'''

def largestDivisibleSubset(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if nums == []:
        return []
    
    
    nums.sort()
    
    subsets = [[nums[i]] for i in range(len(nums))]
    
    for i,num in enumerate(nums[1:], start = 1):
        best = 0
        for j, subset in enumerate(subsets[:i]):
            if num%subset[-1]==0 and len(subset)+1>best:
                best = len(subset)+1
                subsets[i] = subset+[num]
                
    best = []
    for subset in subsets:
        if len(subset) > len(best):
            best = subset
    return best