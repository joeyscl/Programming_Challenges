def countWords(mystring):
    count = 0    
    prevChar = None
    currChar = None
    for ch in mystring:
        currChar = ch
        if currChar != " " and prevChar == " ":
            count = count + 1
    return count
            
print(countWords("My name is Joey"))
