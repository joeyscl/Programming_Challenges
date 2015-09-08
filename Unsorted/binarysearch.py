def binarysearch1(num, mylist):
    index = len(mylist)//2 ## midpoint of mylist
    print(index)
    
    if mylist[index] == num:
        return True
    elif len(mylist) == 1:
        return False
    else:
        if mylist[index] > num:
            return binarysearch(num,mylist[:index])
        else:
            return binarysearch(num,mylist[index:])


def binarysearch2(target, mylist):

    def bshelper(lo,hi):
        mid = (hi+lo)//2
        if mylist[mid] == target:
            return mid
        elif hi-lo == 1:
            return False
        elif mylist[mid] > target:
            return bshelper(lo,mid)
        else:
            return bshelper(mid,hi)

    return bshelper(0,len(mylist)-1)

mylist = [1,2,3,4,5,6,7,8,9]
print(binarysearch2(8,mylist))
