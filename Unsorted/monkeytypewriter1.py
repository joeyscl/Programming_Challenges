import random

def generate(goalstr, newstr):

    dic = 'abcdefghijklmnopqrstuvwxyz '
    mystring= ''
    for i in range(len(goalstr)):
        if newstr[i]==goalstr[i]:
            mystring = mystring + newstr[i]
        else:
             mystring = mystring + dic[random.randrange(27)]

    return mystring

def score(goal, teststring):
    numsame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numsame = numsame +1

    return numsame/len(goal)

def main():
    goalstring = 'my name is joey lee'
    newstring = ' ' * len(goalstring)
    newstring = generate(goalstring, newstring)
    bestscore = 0
    newscore = score(goalstring, newstring)
    attempts = 1
    while newscore != 1:
        if newscore > bestscore:
            bestscore = newscore
            print(attempts, "   ", bestscore,"   ", newstring)
        newstring = generate(goalstring,newstring)
        newscore = score(goalstring,newstring)
        attempts = attempts +1

        
    print(attempts, "   ", 1 ,"   ", newstring)
    return None
