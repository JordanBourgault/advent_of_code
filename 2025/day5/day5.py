with open("2025/day5/input.txt") as f:
    fresh_ranges, ingredients = f.read().split('\n\n')

fresh = [list(map(int, (r.split('-')))) for r in fresh_ranges.split('\n')]

good_ingredients = 0
for ingredient in list(map(int, ingredients.strip().split('\n'))):
    if any([f[0] <= ingredient <= f[1] for f in fresh]):
        good_ingredients += 1
        continue

print('Part 1: ', good_ingredients)


len_strikes = 0
while True:
    replaced = False
    last_len = len(fresh)
    for i, fresh_range in enumerate(fresh):
        for j, sub_range in enumerate(fresh):
            if i == j:
                continue
            if sub_range[0] <= fresh_range[0] <= sub_range[1]:
                if fresh_range[1] >= sub_range[1]:
                    fresh[j] = [sub_range[0], fresh_range[1]]
                    fresh.pop(i)
                    replaced = True
                    break
                else:
                    fresh.pop(i)
                    replaced = True
                    break
        if replaced:
            break
    current_len = len(fresh)
    if last_len == current_len:
        break

total_fresh = sum([el[1] - el[0] + 1 for el in fresh])
print('Part 2: ', total_fresh)
