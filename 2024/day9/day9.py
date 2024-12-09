from copy import deepcopy

with open('days/day9/input.txt') as f:
    data = f.read()
    data = [(i//2 + 1 if i%2 else 0, int(d)) for i, d in enumerate(data, 1)]

def move_from_end(data):
    file = data.pop(-1)
    while file == 0:
        file = data.pop(-1)
    return file

def flatten(data):
    return [x for x in data for x in x]

def build_string(data):
    return flatten([[data] * size for data, size in data])

def checksum(data):
    return sum([i*(file-1) for i, file in enumerate(data) if file])


res = []
new_data = deepcopy(build_string(data))
for i, file in enumerate(new_data):
    if file == 0:
        new_data[i] = move_from_end(new_data)


print('Part 1:', checksum(new_data))


def solve(data):
    for i in range(len(data))[::-1]:
        for j in range(i):
            i_data, i_size = data[i]
            j_data, j_size = data[j]
            if i_data and not j_data and i_size <= j_size:
                data[i] = (0, i_size)
                data[j] = (0, j_size - i_size)
                data.insert(j, (i_data, i_size))


solve(data)
print('Part 2:', checksum(build_string(data)))