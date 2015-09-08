__author__ = 'Joey'

def insertionSort(mylist):

    if len(mylist) <= 1:
        return mylist
    
    else:
        return insertOne(insertionSort(mylist[1:]), mylist[0])
    

def insertOne(mylist, elem):

    if len(mylist) == 0:
        return [elem]
    else:
        if elem < mylist[0]:
            return [elem] + mylist
        else:
            return [mylist[0]] + insertOne(mylist[1:], elem)

        

# print(insertOne([],1))
# print(insertOne([1],2))
# print(insertOne([1,3],2))
# print(insertOne([1,2],3))
# print(insertOne([2,3],1))

test1 = []
test2 = [2,1,5,4,3]
test3 = [5,4,3,2,1]

print(insertionSort(test1))
print(insertionSort(test2))
print(insertionSort(test3))
