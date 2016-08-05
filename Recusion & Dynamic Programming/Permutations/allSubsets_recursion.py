# def genSubsetHelper(arr, subsets, index):
#     if index == len(arr): #base case: return empty set
#         return []
#     else:
#         subsets = genSubsetHelper(arr,subsets,index+1)
#         oldSubsets = list(subsets)        
#         subsets.append([arr[index]])

#        #forloop to combine individual element with existing subsets
#         for oneSet in oldSubsets:
#             subsets.append( [arr[index]] + oneSet )
        
#         # #recursive alternative to using forloop to combine
#         # if oldSubsets != []:
#         #     newSubsets = combine(arr[index], oldSubsets, [])
#         #     subsets = subsets + newSubsets
                        
#         return subsets

# def genSubset(arr):
#     subsets = [[]]
#     subsets = subsets + genSubsetHelper(arr,[], 0)
#     for elem in subsets:
#         print(elem)
#     return subsets

# a = genSubset([1,2,3,4])


''' THIS IS WAY SHORTER/CLEANER'''
def genSubset2(arr):

    res = []
    
    def helper(subset,i):
        if i >= len(arr):
            res.append(subset)
            return
        else:
            helper(subset,i+1)
            helper(subset+[arr[i]],i+1)
            

    helper([],0)
    return res


for sub in genSubset2([1,2,3,4]):
    print(sub)

