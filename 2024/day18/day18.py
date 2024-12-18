from collections import defaultdict

grid_size = 71
grid = defaultdict(lambda: '#')
for i in range(grid_size):
    for j in range(grid_size):
        grid[complex(i, j)] = '.'
start, end = complex(0, 0), complex(grid_size-1, grid_size-1)

with open("2024/day18/input.txt") as f:
    data = [complex(*map(int, line.split(','))) for line in f.read().split('\n')]

def bfs(num_bytes = 1024):
    bytes = set(data[:num_bytes])
    seen = set()
    t = 0
    # Heap with (dist, tie-breaker, pos)
    queue = [(0, t, complex(0, 0))]
    for dist, _, pos in queue:
        if pos == end:
            return dist
        for move in [pos+1, pos-1, pos+1j, pos-1j]:
            if grid[move] != '#' and move not in bytes and move not in seen:
                seen.add(move)
                queue.append((dist + 1, t := t+1, move))
    return False

print('Part 1:', bfs())

for num_byte in range(1024, len(data)):
    if not bfs(num_byte):
        byte = data[num_byte-1]
        print('Part 2:', f'{int(byte.real)},{int(byte.imag)}')
        break
