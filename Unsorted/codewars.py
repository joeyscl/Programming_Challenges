import math
f = math.factorial
def powers(lst):
    total = 0
    n = len(lst)
    for r in range(len(lst)+1):
        options = f(n)//(f(r)*f(n-r))
        total = total + options
    return total

print(powers([1]*500))
