def quickSort(mylist):
    def quickSortHelper(mylist, low, hi):
        if low < hi:
            pivotIndex = partition1(mylist, low, hi)
            quickSortHelper(mylist, low, pivotIndex-1)
            quickSortHelper(mylist, pivotIndex+1, hi)
            
    quickSortHelper(mylist, 0, len(mylist)-1)


def partition(mylist, low, hi):
    if hi - low == 0:
        return
    else:       
        pivotValue = mylist[hi]
        smallerIndex = low  # Invariant: everything left of smallerIndex is smaller than the pivot
                            # ie: it marks the final position of the pivot

        for i in range(low, hi):
            if mylist[i] < pivotValue:
                mylist[i],mylist[smallerIndex] = mylist[smallerIndex],mylist[i]
                smallerIndex += 1
                
        mylist[hi], mylist[smallerIndex] = mylist[smallerIndex], mylist[hi] # swap the pivot to final position
        return smallerIndex
        

# Alternative partion method. I like this one better :)
def partition1(mylist,low,hi):
    left = low
    right = hi-1
    pivotValue = mylist[hi]

    # Loop invariant:   All elements to left of left is smaller than pivot
    #                   All elements to right of right is larger than the pivot (excluding pivot)                    
    while(not left > right):

        if mylist[left] <= pivotValue:
            left += 1
        else:
            mylist[left], mylist[right] = mylist[right],mylist[left]
            right -= 1

    mylist[left],mylist[hi] = mylist[hi],mylist[left]   #swap pivot to final position
    return left
            

test1 = [4,2,5,1,3]
quickSort(test1)
print(test1)

'''test2 = [2,1]
test3 = [4,3,2,1]
test4 = 


quickSort(test2)
quickSort(test3)
quickSort(test4)
            
print(test1)
print(test2)
print(test3)
print(test4)
'''


        
