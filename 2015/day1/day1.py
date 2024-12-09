with open('2015/day1/input.txt') as f:
    data = f.read()

print('Part 1:', data.count('(') - data.count(')'))

current_floor = 0
for i, c in enumerate(data):
    current_floor += 1 if c == '(' else -1
    if current_floor == -1:
        print('Part 2:', i+1)
        break
