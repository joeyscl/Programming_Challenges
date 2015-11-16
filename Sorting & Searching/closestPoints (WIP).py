'''http://www.careercup.com/question?id=5080100049518592

You are given a set of points on x axis (consumers) 
Also you are given a set of points on a plane (producer) 

For every consumer print the nearest producer. 
Wanted something better than O(n^2) time. 

Example: 
consumers: 1 5 7 
producers: (0, 3), (1,1), (3, 2), (8, 10), (9, 100) 

Answer: 
for 1 nearest producer is (1, 1), for 5 nearest is (3, 2), for 7 nearest is (3, 2)

Follow-up question: now both sets are sorted by x coordinate. Could you come up with a linear algorithm?
'''

def closests(cons,pros):

	def calDist(con,pro):
		return (pro[0]-con)**2 + pro[1]**2

	cons = sorted(cons)
	pros = sorted(pros, key = lambda p: ( (p[0]-cons[0])**2 + p[1]**2) )

	pros = [pros[0]] + [p for p in pros[1:] if p[0] >= cons[0]]

	

	print(pros)

cons = [1,5,7]
pros = [(0, 3), (1,1), (3, 2), (8, 10), (9, 100)]

closests(cons,pros)