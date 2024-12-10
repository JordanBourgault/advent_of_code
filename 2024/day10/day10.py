import numpy as np


with open('2024/day10/input.txt') as f:
    data = [list(map(int, line.strip())) for line in f]

rows, cols = len(data), len(data[0])
trail_heads = [np.array([i, j])  for i, d in enumerate(data) for j, e in enumerate(d) if e == 0]
possible_directions = [
    np.array([0, 1]),
    np.array([0, -1]),
    np.array([1, 0]),
    np.array([-1, 0])
]

def move(start, trails):
    val = data[start[0]][start[1]]
    for direction in possible_directions:
        next_pos = start + direction
        if 0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols:
            if val+1 == data[next_pos[0]][next_pos[1]]:
                if val+1 == 9: trails.append(tuple(map(int, next_pos)))
                move(next_pos, trails)

total = 0
rating = 0
for trail_head in trail_heads:
    trails = list()
    move(trail_head, trails)
    total += len(set(trails))
    rating += len(trails)


print('Part 1:', total)
print('Part 2:', rating)