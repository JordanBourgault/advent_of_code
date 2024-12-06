from datetime import datetime
from multiprocessing import Pool

startTime = datetime.now()

with open('days/day5/input.txt') as f:
    rules = dict()
    reports = []
    for line in f:
        if '|' in line:
            rule = list(map(int, line.strip().split('|')))
            current_rules = rules.get(rule[0], [])
            current_rules.append(rule[1])
            rules[rule[0]] = current_rules

        elif ',' in line:
            reports.append(list(map(int, line.strip().split(','))))


def sort_report(report):
    fixed = False
    for i in range(1, len(report)):
        for page in report[:i]:
            if page in rules.get(report[i], []):
                fixed = True
                report[i], report[i-1] = report[i-1], report[i]
                report, _ = sort_report(report)
                break
    return report, fixed


def count_report(report):
    ordered_report = sort_report(report)
    return ordered_report[0][len(ordered_report[0])//2], ordered_report[1]


with Pool() as pool:
    res = pool.map(count_report, reports)
    total = 0
    total_fixed = 0
    for element in res:
        if element[1]:
            total_fixed += element[0]
        else:
            total += element[0]


print('Part 1:', total)
print('Part 2:', total_fixed)

print(datetime.now() - startTime)