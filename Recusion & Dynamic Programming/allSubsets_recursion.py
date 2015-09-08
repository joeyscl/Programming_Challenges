def genSubsetHelper(arr, subsets, index):
    if index == len(arr): #base case: return empty set
        return []
    else:
        subsets = genSubsetHelper(arr,subsets,index+1)
        oldSubsets = list(subsets)        
        subsets.append([arr[index]])

       #forloop to combine individual element with existing subsets
        for oneSet in oldSubsets:
            subsets.append( [arr[index]] + oneSet )
        
        # #recursive alternative to using forloop to combine
        # if oldSubsets != []:
        #     newSubsets = combine(arr[index], oldSubsets, [])
        #     subsets = subsets + newSubsets
                        
        return subsets

def genSubset(arr):
    subsets = [[]]
    subsets = subsets + genSubsetHelper(arr,[], 0)
    for elem in subsets:
        print(elem)
    return subsets

'''a purely recursive helper that returns a list of elem + arr[x]'''
def combine(elem, arr, result):
    if len(arr) == 0:
        return [[elem]]
    else:
        newList = arr[0]+[elem] 
        result.append(newList)
        combine(elem, arr[1:], result)
        return result

a = genSubset([1,2,3,4])

