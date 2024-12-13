import re

with open('2015/day6/input.txt') as f:
    instructions = [re.findall(r'(turn off|turn on|toggle) (\d+),(\d+) through (\d+),(\d+)', line) for line in f]

on = set()
off = set([complex(i, j) for i in range(1000) for j in range(1000)])
lights_value = {complex(i, j) : 0 for i in range(1000) for j in range(1000)}

for i, instruction in enumerate(instructions):
    print(i)
    instruction = instruction[0]
    coords = {complex(i, j) for i in range(int(instruction[1]), int(instruction[3])+1) for j in range(int(instruction[2]), int(instruction[4])+1)}
    if instruction[0] == 'turn on':
        on |= coords
        off -= coords
        for coord in coords:
            lights_value[coord] += 1

    elif instruction[0] == 'turn off':
        off |= coords
        on -= coords
        for coord in coords:
            if lights_value[coord] > 0:
                lights_value[coord] -= 1
    else:
        temp_on = coords & on
        temp_off = coords & off
        on |= temp_off
        off -= temp_off
        off |= temp_on
        on -= temp_on
        
        for coord in coords:
            lights_value[coord] += 2

print('Part 1:', len(on))
print('Part 2:', sum(lights_value.values()))