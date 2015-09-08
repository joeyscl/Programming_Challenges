__author__ = 'Joey'

def bubbleSort(mylist):

    if mylist == []:
        return []


    for index in range(len(mylist)):
        for i in range(len(mylist)-1):
            if mylist[i] > mylist[i+1]:
                mylist[i],mylist[i+1] = mylist[i+1],mylist[i]

test1 = []
test2 = [2,1,5,4,3]
test3 = [5,4,3,2,1]

bubbleSort(test1)
print(test1)
bubbleSort(test2)
print(test2)
bubbleSort(test3)
print(test3)
