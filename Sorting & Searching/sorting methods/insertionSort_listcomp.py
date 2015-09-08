__author__ = 'Joey'


def insertionSort(mylist):

    if len(mylist) <= 1:
        return mylist
    else:

        return insertOne(insertionSort(mylist[1:]), mylist[0])

def insertOne(mylist, num):
    #helper for insertionSort. Given a sorted list and num, inserts num into sorted list
    if mylist == []:
        return [num]

    elif len(mylist) == 1:
        if num < mylist[0]:
            return [num] + mylist
        else:
            return mylist + [num]

    else:
        for i in range(len(mylist)):
            if num < mylist[i]:
                mylist.insert(i,num)
                return mylist
        mylist.append(num)
        return mylist

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
