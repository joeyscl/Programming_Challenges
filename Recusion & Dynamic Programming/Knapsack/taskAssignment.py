'''http://www.careercup.com/question?id=6282171643854848
There are at most eight servers in a data center. Each server has got a capacity/memory limit. There can be at most 8 tasks that need to be scheduled on those servers. Each task requires certain capacity/memory to run, and each server can handle multiple tasks as long as the capacity limit is not hit. Write a program to see if all of the given tasks can be scheduled or not on the servers? 

Ex: 
Servers capacity limits: 8, 16, 8, 32 
Tasks capacity needs: 18, 4, 8, 4, 6, 6, 8, 8 
For this example, the program should say 'true'. 

Ex2: 
Server capacity limits: 1, 3 
Task capacity needs: 4 
For this example, program should return false. 
'''
from copy import deepcopy

mem = {}
def assign(caps, tasks):

	if (frozenset(caps),frozenset(tasks)) in mem:
		return mem[(frozenset(caps),frozenset(tasks))]

	elif tasks == []:

		if -1 in [num//abs(num) for num in caps if num!= 0]:
			return False
		else:
			return True

	else:
		res = False
		for i in range(len(caps)):
			newCaps = deepcopy(caps)
			newCaps[i] -= tasks[0]
			res = res or assign(newCaps, tasks[1:])

		mem[(frozenset(caps),frozenset(tasks))] = res
		return res

print(assign([8, 16, 8, 32],[18, 4, 8, 4, 6, 6, 8, 8]))
print(assign([1,3],[4]))