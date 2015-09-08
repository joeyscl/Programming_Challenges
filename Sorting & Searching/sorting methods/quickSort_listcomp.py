__author__ = 'Joey'

def quickSort(mylist):

    if len(mylist) <= 1:
        return mylist

    pivot = mylist[0]
    lefthalf = list(num for num in mylist if num < pivot)
    righthalf = list(num for num in mylist if num > pivot)

    lefthalf = quickSort(lefthalf)
    righthalf = quickSort(righthalf)

    return lefthalf + [pivot] + righthalf
    
test1 = []
test2 = [2,1,5,4,3]
test3 = [5,4,3,2,1]

print(quickSort(test1))
print(quickSort(test2))
print(quickSort(test3))
