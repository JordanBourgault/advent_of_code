with open('2015/day3/input.txt') as f:
    data = f.read()

moves = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

def create_or_increment(d, key):
    if d.get(key, None):
        d[key] += 1
    else:
        d[key] = 1

current_pos = (0, 0)
presents = dict()
create_or_increment(presents, current_pos)

for i, move in enumerate(data):
    move = moves[move]
    current_pos = current_pos[0] + move[0], current_pos[1] + move[1]
    create_or_increment(presents, current_pos)

print('Part 1:', len(presents.keys()))

pos_a = (0,0)
pos_b = (0,0)
presents = dict()
create_or_increment(presents, pos_a)

for i, move in enumerate(data):
    move = moves[move]
    if i%2:
        pos_a = pos_a[0] + move[0], pos_a[1] + move[1]
        create_or_increment(presents, pos_a)
    else:
        pos_b = pos_b[0] + move[0], pos_b[1] + move[1]
        create_or_increment(presents, pos_b)

print('Part 2:', len(presents.keys()))