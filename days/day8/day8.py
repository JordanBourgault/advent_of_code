from math import lcm
import numpy as np

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
            positions.append(np.array([i, j]))
            antennas[val] = positions
    return antennas

antenna_data = get_antennas(data)


def bigger_or_equal(a, vector):
    return a >= max(vector)


def check_bounds(map_bounds, pos):
    return 0 <= pos[0] < map_bounds[0] and 0 <= pos[1] < map_bounds[1]


def check_harmonics(antinodes, pos, vector):
    i = 1
    while True:
        node = pos - i * vector
        if check_bounds(map_bounds, node):
            antinodes.add(tuple(node))
        else:
            break
        i += 1


def propagate_point(nodes, pos, vector, harmonics):
    antinode_a = pos - vector
    if check_bounds(map_bounds, antinode_a):
        nodes.add(tuple(antinode_a))
        if harmonics and check_harmonics:
            check_harmonics(nodes, pos, vector)


def get_antinodes(nodes, data, harmonics=False):
    for i, pos_a in enumerate(data):
        for j, pos_b in enumerate(data):
            if i == j:
                continue
            vector = pos_a - pos_b

            propagate_point(nodes, pos_a, -vector, harmonics)
            propagate_point(nodes, pos_b, vector, harmonics)


antinodes = set()
antinodes_harmonics = set()

for key, values in antenna_data.items():
    get_antinodes(antinodes, antenna_data[key], False)
    get_antinodes(antinodes_harmonics, antenna_data[key], harmonics=True)
    if len(values):
        for value in values:
            antinodes_harmonics.add(tuple(value))
    

print('Part1:', len(antinodes))
print('Part2:', len(antinodes_harmonics))


def build_grid(map_bounds, antinodes):
    grid = [['.' for _ in range(map_bounds[1])] for _ in range(map_bounds[0])]
    for antinode in antinodes:
        grid[antinode[0]][antinode[1]] = '#'
    
    with open('output.txt', 'w') as f:
        for row in grid:
            f.write(''.join(row) + '\n')

build_grid(map_bounds, antinodes)