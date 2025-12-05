with open("2025/day4/input.txt") as f:
    grid = [[char for char in line.strip()] for line in f]


def check_adjascent(pos: tuple[int, int]):
    indexes_to_check = []
    for y in range(-1,2):
        for x in range(-1,2):
            pos_to_check = (pos[0]+y, pos[1]+x)
            if pos_to_check == pos:
                continue
            if 0 <= pos_to_check[0] <= len(grid)-1 and 0 <= pos_to_check[1] <= len(grid[0])-1:
                indexes_to_check.append(pos_to_check)
    return indexes_to_check

def get_roll(pos: tuple[int, int]):
    return grid[pos[0]][pos[1]] == '@'

def remove_roll(pos: tuple[int, int]):
    grid[pos[0]][pos[1]] = '.'

def check_grid():
    accessible_rolls = 0
    rolls_to_remove = []
    for y_pos, line in enumerate(grid):
        for x_pos, element in enumerate(line):
            if element != '@':
                continue
            indexes_to_check = check_adjascent((y_pos, x_pos))
            boxes_adjascent = [get_roll(pos) for pos in indexes_to_check]
            if sum(boxes_adjascent) < 4:
                rolls_to_remove.append((y_pos, x_pos))
                accessible_rolls += 1
    for roll_pos in rolls_to_remove:
        remove_roll(roll_pos)
    return accessible_rolls

total_to_remove = 0
step_to_remove = check_grid()
total_to_remove += step_to_remove
print('Part 1:', total_to_remove)

while step_to_remove:
    step_to_remove = check_grid()
    total_to_remove += step_to_remove

print('Part 2: ', total_to_remove)
