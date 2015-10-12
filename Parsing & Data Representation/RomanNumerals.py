__author__ = 'Joey'

''' given valid Roman Numeral, convert to integer. '''
def convert(rom):
	val = {
			'I':1,
			'V':5,
			'X':10,
			'L':50,
			'C':100
			}

	if len(rom) == 1:
		return val[rom]

	total = 0
	i = 0
	while True:
		if i > len(rom)-1:
			break
		elif i == len(rom)-1:
			total += val[rom[-1]]
			break

		elif val[rom[i]] < val[rom[i+1]]:
			total += val[rom[i+1]] - val[rom[i]]
			i += 2
		elif val[rom[i]] > val[rom[i+1]]:
			total += val[rom[i]]
			i += 1
		else:
			total += val[rom[i]]
			i += 1

	return total

print(convert('XCIX'))