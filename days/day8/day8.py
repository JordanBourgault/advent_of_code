from math import lcm

with open('days/day8/input_test.txt') as f:
    data = [list(line.strip()) for line in f]

map_bounds = len(data), len(data[0])

def get_antennas(data):
    antennas = dict()
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val == '.':
                continue
            
            positions = antennas.get(val, [])
            positions.append((i, j))
            antennas[val] = positions
    return antennas

antenna_data = get_antennas(data)

def subtract(pos_a, pos_b):
    return (pos_a[0] - pos_b[0], pos_a[1] - pos_b[1])

def add(pos_a, pos_b):
    return (pos_a[0] + pos_b[0], pos_a[1] + pos_b[1])

def invert(vector):
    return multiply(-1, vector)

def multiply(a, vector):
    return (a*vector[0], a*vector[1])

def div(a, vector):
    return (vector[0]//a, vector[1]//a)

def bigger_or_equal(a, vector):
    return a >= vector[0] or a >= vector[1]

def check_bounds(map_bounds, pos):
    return 0 <= pos[0] <= map_bounds[0] and 0 <= pos[1] <= map_bounds[1]

def check_harmonics(antinodes, pos, vector):
    i = 0
    while True:
        node = add(pos, multiply(i, vector))
        if check_bounds(map_bounds, node):
            antinodes.add(node)
        else:
            break
        i += 1


def get_antinodes(antinodes, data, harmonics=False):
    for i, pos_a in enumerate(data):
        for j, pos_b in enumerate(data):
            if i == j:
                continue
            vector = subtract(pos_a, pos_b)
            print('AAAAAAAa')
            print(vector)
            mul = lcm(*vector)
            if not bigger_or_equal(mul, vector):
                vector = div(lcm(*vector), vector)
            print(vector)

            antinode_a = subtract(pos_a, invert(vector))
            if check_bounds(map_bounds, antinode_a):
                antinodes.add(antinode_a)
                if check_harmonics:
                    check_harmonics(antinodes, pos_a, invert(vector))
            antinode_b = subtract(pos_b, vector)
            if check_bounds(map_bounds, antinode_b):
                antinodes.add(antinode_b)
                if check_harmonics:
                    check_harmonics(antinodes, pos_a, vector)
                


antinodes = set()
for key, values in antenna_data.items():
    get_antinodes(antinodes, antenna_data[key], True)
    if len(values):
        for value in values:
            antinodes.add(value)
    
print(len(antinodes))