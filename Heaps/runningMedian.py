from heapq import *

minHeap = []
maxHeap = []

def insert(num):
	if minHeap == []:
		minHeap.append(num)
	elif num >= minHeap[0]:
		if len(minHeap) <= len(maxHeap):
			heappush(minHeap, num)
		else:
			heappush(maxHeap, -heappop(minHeap))
			heappush(minHeap, num)
	else:
		if len(maxHeap) < len(minHeap):
			heappush(maxHeap,-num)
		else:
			heappush(minHeap, -heappop(maxHeap))
			heappush(maxHeap,-num)

def median():
	if len(minHeap) > len(maxHeap):
		return minHeap[0]
	else:
		return (minHeap[0] - maxHeap[0])/2

test = [4,2,6,8,2,1,8,1,0,4,5,7,4,0,4,6,3,5,7,2,0,1,8]
for num in test:
	insert(num)
	print(minHeap)
	print([-x for x in maxHeap])
	print(median())
	print()
