with open('days/day2/input.txt') as f:
    levels = [[int(element) for element in line.strip().split(' ')] for line in f]


def check_safe(arr: list) -> bool:
    def check_diff(a, b):
        diff = abs(a - b)
        return 1 <= diff <= 3
    
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        for i in range(0, len(arr)):
            if i == len(arr) - 1:
                break
            if not check_diff(arr[i], arr[i + 1]):
                return False
        return True
    return False


safe_reports = 0
for level in levels:
    if check_safe(level):
        safe_reports += 1

# Part 1 answer
print('Part 1 answer:', safe_reports)


def check_safe_damper(arr: list) -> bool:
    if check_safe(arr):
        return True

    for i in range(0, len(arr)):
        temp = arr.copy()
        temp.pop(i)
        if check_safe(temp):
            return True
    
    return False

safe_reports_damper = 0
for level in levels:
    if check_safe_damper(level):
        safe_reports_damper += 1

# Part 2 answer
print('Part 2 answer:', safe_reports_damper)