''' STOCK OPTIMIZATION PROBLEM
Given an array of stock prices, determine when to buy and sell
to maximize profits. You must buy before you sell
'''
def findMinMax(prices):
    #Given an array of stock prices, return(buyingPrice, sellingPrice)
    #such that profit is maximized
    
    index = 0
    smallestSoFar = None
    biggestAfterSmallest = 0
    bestRatio = 0 # the ratio of selling price:buying price
    bestCombo = (0,0) # the combo that will give best ratio

    peaks = findPeaks(prices)
    mins = findMins(prices)

    #we want to find the last global max
    globalMax = 0
    for i in range(len(peaks)):
        if peaks[i] >= globalMax:
            globalMax = peaks[i]
            globalMaxIndex = i


    #find smallest price preceeding globalMax
    minBeforeMax = min(prices[:globalMaxIndex])
    
    print(minBeforeMax, globalMax)
    
    ratio1 = globalMax/minBeforeMax

    #we want to find the earliest min
    globalMin = 9999
    for i in range(len(mins)):
        if mins[i] < globalMin:
            globalMin = mins[i]
            globalMinIndex = i


    #find the largest price after globalMin
    maxAfterMin = max(peaks[globalMinIndex:])

    print(globalMin, maxAfterMin)

    ratio2 = maxAfterMin/globalMin


    if ratio1 >= ratio2:
        return (minBeforeMax, globalMax)
    else:
        return (globalMin, maxAfterMin)

    

def findPeaks(prices):
    #Find peaks. We assume that prices never stay the same
    
    if len(prices) <= 1:
        return prices
    
    peaks = [0]*len(prices)
    if prices[0] > prices[1]:
        peaks[0] = prices[0]

    for i in range(1, len(prices)-1):
        if prices[i] > prices[i-1] and prices[i] > prices[i+1]:
            peaks[i] = prices[i]

    if prices[-1] > prices[-2]:
        peaks[-1] = prices[-1]

    return peaks

def findMins(prices):
    #Find Mins. We assume that prices never stay the same
    
    if len(prices) <= 1:
        return prices
    
    valleys = [9999]*len(prices)
    if prices[0] < prices[1]:
        valleys[0] = prices[0]

    for i in range(1, len(prices)-1):
        if prices[i] < prices[i-1] and prices[i] < prices[i+1]:
            valleys[i] = prices[i]

    if prices[-1] < prices[-2]:
        valleys[-1] = prices[-1]

    return valleys
        
test1 = []
test2 = [1,2,1]
test3 = [2,1,3]
test4 = [4,3,2]
test5 = [30,34,37,25,25,12,11,10,30,28,36,37,34,30,28,5,23,24]

print(findMinMax(test5))

##print(findPeaks(test1))
##print(findPeaks(test2))
##print(findPeaks(test3))
##print(findPeaks(test4))
##print(findPeaks(test5))
##
##print(findMins(test1))
##print(findMins(test2))
##print(findMins(test3))
##print(findMins(test4))
##print(findMins(test5))
