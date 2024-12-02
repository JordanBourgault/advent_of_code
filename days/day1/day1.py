from collections import Counter

with open('days/day1/input.txt') as f:
    line_a = []
    line_b = []
    for line in f:
        lines = line.strip().split('   ')
        line_a.append(int(lines[0]))
        line_b.append(int(lines[1]))

line_a.sort()
line_b.sort()

total_distance = 0
for i in range(0, len(line_a)):
    total_distance += abs(line_b[i] - line_a[i])

# Part 1
print(total_distance)

counter = Counter(line_b)
similarity = 0
for num in line_a:
    occurence_num = counter.get(num, 0)
    similarity += num * occurence_num

# Part 2
print(similarity)