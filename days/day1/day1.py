with open('days/day1/input.txt') as f:
    data = [*map(int, f.read().split())]
    line_a, line_b = sorted(data[0::2]), sorted(data[1::2])


total_distance = 0
for i in range(0, len(line_a)):
    total_distance += abs(line_b[i] - line_a[i])

# Part 1
print('Part 1 solution:', total_distance)

similarity = 0
for num in line_a:
    similarity += num * line_b.count(num)

# Part 2
print('Part 2 solution:', similarity)