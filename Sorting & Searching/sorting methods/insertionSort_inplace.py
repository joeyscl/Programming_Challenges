__author__ = 'Joey'

def insertionSort(mylist):

    if mylist == []:
        return []

    for index in range(1,len(mylist)): # assume mylist[0] to be sorted.
        # ie: mylist sorted up to 'index' non-inclusive

        position = index
        currentvalue = mylist[index] #currentvalue is the value to be inserted

        while position > 0 and mylist[position-1] > currentvalue: #keep shifting values in sorted portion...
            mylist[position] = mylist[position-1]                 #...until we find appropriate slot for currentvalue
            position -= 1
        mylist[position] = currentvalue

test1 = []
test2 = [2,1,5,4,3]
test3 = [5,4,3,2,1]

insertionSort(test1)
print(test1)
insertionSort(test2)
print(test2)
insertionSort(test3)
print(test3)