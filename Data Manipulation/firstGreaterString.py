''' Given a word W, rearrange the letters of W to construct another word  in such a way that  is lexicographically greater than W. 
In case of multiple possible answers, find the lexicographically smallest one among them.
ab -> ba
bb -> no answer
hefg -> hegf
dhck -> dhkc
dkhc -> hcdk
'''

# find first drop (rev. traversal)
def findDrop(s):
    for i in range(len(s)-1, 0, -1):
        if s[i] > s[i-1]:
            return i-1
    return -1

def Solution(s):
    d = findDrop(s)
    if d == -1:
        return("no answer")
    else:
        # find first indice (rev. traversal) greater than s[d]
        t = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] > s[d]:
                t = i
                break
                
        arr = [ch for ch in s]
        arr[d],arr[t] = arr[t],arr[d]
        arr = arr[:d+1] + arr[d+1:][::-1]
        
        newS = ''
        for ch in arr:
            newS += ch
            
        return(newS)

for s in ['ab','bb','hefg','dhck','dkhc']:
    print (s,Solution(s))