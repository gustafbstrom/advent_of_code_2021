#!env python3


def day3A(input):
	wl = len(input[0:input.index('\n')])
	res = [0 for _ in range(len(input[0:wl]))]
	for line in input.splitlines():
		for i, bit in enumerate(line):
			res[i] = res[i]+1 if bit == '1' else res[i]-1
	res = ''.join(['1' if a > 0 else '0' for a in res])
	return int(res, 2) * (int(res, 2)^2**wl-1)


def day3B(input):
	raise NotImplementedError('zZz')


test_data = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''

assert day3A(test_data) == 198
assert day3B(test_data) == 230

with open('day3_input.txt', 'r') as fp:
    real_data = fp.read()
print(day3A(real_data))
print(day3B(real_data))
