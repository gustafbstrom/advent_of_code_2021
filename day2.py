#!env python3


def day2A(input):
    pos = {'h': 0, 'v': 0}
    for com, step in (line.split() for line in input.splitlines()):
        step = int(step)
        match com:
            case 'forward':
                pos['h'] += step
            case 'down':
                pos['v'] += step
            case 'up':
                pos['v'] -= step
            case _:
                raise Exception('what...?')
    return pos['h'] * pos['v']


def day2B(input):
    pos = {'h': 0, 'v': 0, 'a': 0}
    for com, step in (line.split() for line in input.splitlines()):
        step = int(step)
        match com:
            case 'forward':
                pos['h'] += step
                pos['v'] += step*pos['a']
            case 'down':
                pos['a'] += step
            case 'up':
                pos['a'] -= step
            case _:
                raise Exception('what...?')
    return pos['h'] * pos['v']


# Tests
test_data = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''
assert day2A(test_data) == 150
assert day2B(test_data) == 900

# Real results
with open('day2_input.txt', 'r') as fp:
    real_data = fp.read()
print(day2A(real_data))
print(day2B(real_data))
