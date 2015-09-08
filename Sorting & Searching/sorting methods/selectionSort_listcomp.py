__author__ = 'Joey'

def selectionSort(mylist):

    if len(mylist) <= 1:
        return mylist

    maxval = max(mylist)
    mylist.remove(maxval)
    rest = mylist
    rest = selectionSort(rest)

    return rest + [maxval]


test1 = []
test2 = [2,1,5,4,3]
test3 = [5,4,3,2,1]

print(selectionSort(test1))
print(selectionSort(test2))
print(selectionSort(test3))