import re


with open("2025/day2/input.txt") as f:
    ids = f.read().split(',')
    invalid_ids_part_1 = 0
    invalid_ids_part_2 = 0
    for id in ids:
        start, stop = id.split('-')
        for i in range(int(start), int(stop)+1):
            i = str(i)
            part_1_match = re.match(r'^(.+)\1$', i)
            if part_1_match:
                invalid_ids_part_1 += int(i)
            part_2_match = re.match(r'^(.+)\1+$', i)
            if part_2_match:
                invalid_ids_part_2 += int(i)

print('Part 1: ', invalid_ids_part_1)
print('Part 2: ', invalid_ids_part_2)
