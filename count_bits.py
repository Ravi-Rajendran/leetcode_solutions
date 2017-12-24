'''
Given n = 5, return [0, 1, 1, 2, 1, 2] # no of 1's in numbers from 0 to n
'''


def count_bits(num):
	res = [0]*(num+1)
	for i in range(1, num+1):
		res[i] += res[i & (i-1)] + 1
	return res

print(count_bits(5))
