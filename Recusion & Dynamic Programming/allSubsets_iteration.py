def genSubsets(arr):
    subsets = [[]] # your final results
    for elem in arr:     
        newSubsets = [[elem]] #new subsets for this iteration
        
        for oneSet in subsets:
            newSet = [elem] + oneSet #combine element with all existing subsets
            newSubsets.append(newSet)#...and append to newSubsets
        
        subsets = subsets + newSubsets #combine newSubsets with existing subsets

    # print nicely
    for subset in subsets:
        print(subset)
    
genSubsets([1,2,3,4])


'''
Iterate through each element of array and combine with all existing subsets:
ie: given 1 2 3

[]          base case
1           first element of input
2           second element of input
2 1         combine 2 with 1
3           third element of input
3 1         combine 3 with 1
3 2         combine 3 with 2
3 2 1       combine 3 with 2 1

'''



