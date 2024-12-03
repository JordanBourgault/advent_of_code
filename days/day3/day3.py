import re

with open('days/day3/input.txt') as f:
    data = f.read()

def match_operation(string: str) -> list[str]:
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))'
    return re.findall(pattern, string)

total = total_enabled = 0
enabled = True
for mul_a, mul_b, do, dont in match_operation(data):
    if do or dont:
        enabled = bool(do)
        continue

    mul = int(mul_a) * int(mul_b)
    total += mul
    if enabled:
        total_enabled += mul

print('Part 1 answer:', total)
print('Part 2 answer:', total_enabled)