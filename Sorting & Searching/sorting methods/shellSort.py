__author__ = 'Joey'

def shellSort(mylist):

    if mylist == []:
        return []

    gap = len(mylist) // 2 #the initial gap to use for sorting
    for start in range(gap):
        gapInsertionSort(mylist, start, gap)
        gap = gap // 2
        if gap < 1:
            break

def gapInsertionSort(mylist, start, gap):

    for index in range(1*gap,len(mylist), gap): #assume mylist is sorted up to index not inclusive
        currentval = mylist[index]     #currentval is the value to be inserted
        position = index

        while position > start-gap and mylist[position-gap] > currentval: #keep shifting values in sorted portion...
            mylist[position] = mylist[position-gap]               #...until we find appropriate slot for currentvalue
            position -= gap
        mylist[position] = currentval

test1 = []
test2 = [2,1,5,4,3]
test3 = [5,4,3,2,1]

shellSort(test1)
print(test1)
shellSort(test2)
print(test2)
shellSort(test3)
print(test3)