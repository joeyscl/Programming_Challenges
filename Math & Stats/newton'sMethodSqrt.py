''' finding sqrt of k => solve for x^2 - k = 0
use newtons method: x1 = x0 - f(x0)/f'(x0)'''

from sys import maxsize
def sqrt(k):
	x0 = k
	prev = maxsize
	count = 0

	for i in range(20):
		x0 = x0 - (x0**2-k)/(2*x0)

		if format(prev, '.10f') == format(x0, '.10f'):
			break
		else:
			prev = x0
			count += 1

	print("10 decimal place precision found after %d iterations" %(count) )
	print(x0)

sqrt(3)