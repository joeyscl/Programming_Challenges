__author__ = 'Joey'


def mergeSort(mylist):

    if len(mylist) < 2:
        return mylist

    else:
        mid = len(mylist)//2
        lefthalf = mylist[:mid]
        righthalf = mylist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0  # index for lefthalf
        j = 0  # index for righthalf
        k = 0  # index for mylist

        
        # merging procedure below:
        #While there are still elements in both left and right
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                mylist[k] = lefthalf[i]
                i += 1
            else:
                mylist[k] = righthalf[j]
                j += 1
            k += 1

        #right has run out of elements, add rest of left
        while i < len(lefthalf):
            mylist[k] = lefthalf[i]
            i += 1
            k += 1

        #left has run out of elements, add rest or right
        while j < len(righthalf):
            mylist[k] = righthalf[j]
            j += 1
            k += 1

test1 = []
test2 = [2 ,1, 5, 4, 3]
test3 = [5, 4, 3, 2, 1]

mergeSort(test1)
print(test1)
mergeSort(test2)
print(test2)
mergeSort(test3)
print(test3)
