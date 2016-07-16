''' given an integer, return a string that represents the hex of that integer '''

def toHex(num):
	dic = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
	for i in range(1,11):
		dic[i] = str(i)

	power = 1
	while num / (16**power) >= 1:
		power += 1

	res = '0x'
	power -= 1
	while power >= 0:
		quotient = num//(16**power)
		remainder = num%(16**power)
		if quotient == 0:
			res += '0'			
		else:
			res += dic[quotient]
			num = remainder
		power -= 1

	print(res)

toHex(1000)






