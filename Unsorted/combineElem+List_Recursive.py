'''a purely recursive helper that returns a list of elem + arr[x]'''
def combineHelper(elem, arr, result):
    if len(arr) == 0:
        return
    else:
        newList = [elem] + arr[0]
        result.append(newList)
        combineHelper(elem, arr[1:], result)
        return result

a = combineHelper(0,[[1],[1,2],[1,2,3]],[])
print(a)
