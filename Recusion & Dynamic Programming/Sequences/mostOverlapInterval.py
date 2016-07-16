''' given an array of intervals, determine the interval with most overlaps (treat end points as open)
ie: [ (1,5), (-3,2), (4,5), (2,6)] ---> (2,6) since it has 3 overlaps '''

def mostOverlaps(intervals):

	intervals = sorted(intervals, key = lambda x: x[0])

	best = [] 		# best interval so far
	bestLen = 0 	# overlaps 'best' has

	i = 0	

	while i < len(intervals):

		count = 0		# overlaps for the current interval (at index i)
		curr = intervals[i]
		next = i + 1	# the index of the next interval we want to skip to

		for j in range(i+1, len(intervals)):
			print(curr,intervals[j])

			# case1: no overlap
			if intervals[j][0] >= curr[1]:
				print('case1')
				if count > bestLen:
					bestLen = count
					best = curr
				break

			# case2: complete overlap
			if intervals[j][1] <= curr[1]:
				print('case2')
				count += 1
				if count > bestLen:
					bestLen = count
					best = curr
				next = min(j + 1, next)


			# case3: partial overlap
			if intervals[j][1] > curr[1]:
				print('case3')
				count += 1
				if count > bestLen:
					bestLen = count
					best = curr
				next = min(j + 1, next)

			# case4: if we have reached the end of all intervals
			if j == len(intervals) - 1:
				return best, bestLen			

		i = max(next, i+1)	

	return best, bestLen


test1 = [(-1,0),(0,4),(1,2),(1,2),(1,2),(1,2)]

print(mostOverlaps(test1))