import time

def factorial_1(num):
    '''(number) -> number

    Returns the factorial of the number using recursion
    
    >>> factorial_1(5)
    120
    >>> factorial_1(7)
    5040
    '''

    if num == 1:
        return 1
    else:
        return num * factorial_1(num-1)


def factorial_2(num):
    '''(number) -> number

    Returns the factorial of the number using tail-end recursion
    
    >>> factorial_1(5)
    120
    >>> factorial_1(7)
    5040
    '''
    def inner_func (num, product):
    
        if num == 1:
            return product
        else:
            return inner_func((num-1) , (num*product))

    return inner_func(num, 1)

def calculateRunTime():

    startTime1 = time.time()
    for i in range(1000):
        factorial_1(500)
    print(time.time()-startTime1)

    startTime2 = time.time()
    for i in range(1000):
        factorial_2(500)
    print(time.time()-startTime2)

calculateRunTime()
