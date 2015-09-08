def flatten(lis):
    """Given a list, possibly nested to any level, return it flattened."""
    new_lis = []
    for item in lis:
        if type(item) == type([]):
            new_lis.extend(flatten(item))
        else:
            new_lis.append(item)
    return new_lis

test1 = []
test2 = [1,2,3]
test3 = [1,2,[3,4],5]

print(flatten(test1))
print(flatten(test2))
print(flatten(test3))
