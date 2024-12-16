from heapq import heappop, heappush

with open('2024/day16/input.txt') as f:
    grid = {complex(i, j): val for i, row in enumerate(f) for j, val in enumerate(row.strip())}
    start = next(z for z in grid if grid[z]=='S')
    end = next(z for z in grid if grid[z]=='E')


def find_path(current_pos):
    seen = set()
    path = set()
    best_score = 1e9
    t = 0
    # Heap with (score, tie-breaker, current_pos, direction, [current_path])
    queue = [(0, t, current_pos, 1j, [current_pos])]

    while queue:
        score, _, pos, previous_dir, current_path = heappop(queue)
        seen.add((pos, previous_dir))
        val = grid[pos]

        if val == 'E' and score <= best_score:
            path |= set(current_path)
            best_score = score
        
        for rotation, points in (1, 1), (1j, 1001), (-1j, 1001):
            new_dir = previous_dir*rotation
            next_pos = pos + new_dir
            if grid[next_pos] != '#' and (next_pos, new_dir) not in seen:
                    heappush(queue, (score + points, t := t+1, next_pos, new_dir, current_path + [next_pos]))
                    
    return best_score, len(path)


res = find_path(start)
print('Part 1:', res[0])
print('Part 2:', res[1])