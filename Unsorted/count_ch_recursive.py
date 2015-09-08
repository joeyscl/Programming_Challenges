def count_char(word, char):
    if word == "":
        return 0
    elif word[0] == char:
        return 1 + count_char(word[1:], char)
    else:
        return count_char(word[1:], char)


test1 = ""
test2 = "a"
test3 = "abca"

print(count_char(test1,"a"))
print(count_char(test2,"a"))
print(count_char(test3,"a"))
