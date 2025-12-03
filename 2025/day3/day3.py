def find_allowed_max(line: list, values_remaining: int):
    if values_remaining == 0:
        battery_val = max(line)
    else:
        battery_val = max(line[:-values_remaining])
    battery_ind = line.index(battery_val)
    
    if not values_remaining:
        return str(battery_val)
    
    next_batteries = find_allowed_max(line[battery_ind+1:], values_remaining-1)
    battery = str(battery_val) + next_batteries
    return battery

with open("2025/day3/input.txt") as f:
    part1_total = 0
    part2_total = 0
    for line in f:
        line = [int(v) for v in line.strip()]
        part1_total += int(find_allowed_max(line, 1))
        part2_total += int(find_allowed_max(line, 11))

print('Part 1 :', part1_total)
print('Part 2 :', part2_total)
