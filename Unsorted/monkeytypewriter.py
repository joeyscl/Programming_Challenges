import random

def generateone(n):
    ''' (int) -> string

    returns random string of length n
    '''

    dic = 'abcdefghijklmnopqrstuvwxyz '
    mystring = ''
    for i in range(n):
        mystring = mystring + dic[random.randrange(27)]

    return mystring

def score(goal, teststring):
    numsame = 0
    for i in range(len(goal)):
        if goal[i] == teststring[i]:
            numsame = numsame +1

    return numsame/len(goal)

def main():
    goalstring = 'methinks it is like a weasel'
    newstring = generateone(len(goalstring))
    beststring = ''
    bestscore = 0
    newscore = score(goalstring, newstring)
    attempts = 1
    while bestscore < 1:
        if newscore > bestscore:
            bestscore = newscore
            print(attempts, "   ", bestscore,"   ", newstring)
        newstring = generateone(len(goalstring))
        newscore = score(goalstring,newstring)
        attempts = attempts +1
        
        
        
