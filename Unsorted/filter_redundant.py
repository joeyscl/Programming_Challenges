def filterlist(mylist):
    #mylist.reverse()
    newlist = []
    for i in range(len(mylist)):
        num = mylist[i]
        print(num)
        if num not in newlist:
            newlist.append(num)
    return newlist

mylist = [1,9,3,4,5,4,3,7,1]
print(list(filterlist(mylist)))
