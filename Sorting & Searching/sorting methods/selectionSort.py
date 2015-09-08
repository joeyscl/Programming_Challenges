__author__ = 'Joey'

def selectionSort(mylist):

    if mylist == [] or len(mylist) == 1:
        return mylist

    for index in range(len(mylist)):
        posofmax = 0 #assume largest of the unsorted numbers
        for i in range(len(mylist)-index):
            if mylist[i] > mylist[posofmax]:
                posofmax = i
        mylist[posofmax],mylist[-1-index] = mylist[-1-index],mylist[posofmax]


test1 = []
test2 = [2,1,5,4,3]
test3 = [5,4,3,2,1]

selectionSort(test1)
print(test1)
selectionSort(test2)
print(test2)
selectionSort(test3)
print(test3)