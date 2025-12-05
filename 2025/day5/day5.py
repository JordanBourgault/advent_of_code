with open("2025/day5/input.txt") as f:
    fresh_ranges, ingredients = f.read().split('\n\n')

fresh = [list(map(int, (r.split('-')))) for r in fresh_ranges.split('\n')]
sorted_fresh = sorted(fresh, key=lambda x: x[0])
offset = 0
for i in range(len(sorted_fresh)):
    i += offset
    try:
        # Start of next range is contained in current range
        if sorted_fresh[i][0] <= sorted_fresh[i+1][0] <= sorted_fresh[i][1]:
            # Next range finishes outside current range
            if sorted_fresh[i+1][1] > sorted_fresh[i][1]:
                sorted_fresh[i] = [sorted_fresh[i][0], sorted_fresh[i+1][1]]
                sorted_fresh.pop(i+1)
                offset -= 1
            # Next range is within current range
            else:
                sorted_fresh.pop(i+1)
                offset -= 1
    except IndexError:
        pass

good_ingredients = 0
for ingredient in list(map(int, ingredients.strip().split('\n'))):
    if any([f[0] <= ingredient <= f[1] for f in sorted_fresh]):
        good_ingredients += 1
        continue

print('Part 1: ', good_ingredients)
total_fresh = sum([el[1] - el[0] + 1 for el in sorted_fresh])
print('Part 2: ', total_fresh)
