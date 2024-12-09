with open('2015/day2/input.txt') as f:
    data = [(l, w, h) for l, w, h in [map(int, line.split('x')) for line in f.read().splitlines()]]

print('Part 1:', sum([2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l) for l, w, h in data]))

print('Part 2:', sum([2*min(l+w, w+h, h+l) + l*w*h for l, w, h in data]))