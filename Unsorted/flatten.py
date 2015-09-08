def flatten(mylist):
    result = []
    for e in mylist:
        if type(e) == []:
            result = result + flatten(e)
        else:
            result.append(e)
        
    return result

test1 = []
test2 = [1,2,3]
test3 = [1,2,[3,4],5]

print(flatten(test1))
print(flatten(test2))
print(flatten(test3))
