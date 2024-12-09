with open('days/day4/input.txt') as f:
    grid = [list(row.strip()) for row in f]

grid_size = {
    "row": len(grid),
    "col": len(grid[0])
}

def search(grid, row_num, col_num, row_mul, col_mul):
    if 0 <= col_num + 3*col_mul < grid_size['col'] and 0 <= row_num + 3*row_mul < grid_size['row']:
        if (grid[row_num + 1*row_mul][col_num + 1*col_mul] == 'M' and 
            grid[row_num + 2*row_mul][col_num + 2*col_mul] == 'A' and 
            grid[row_num + 3*row_mul][col_num + 3*col_mul] == 'S'):
            return True

def search_all(grid, row_num, col_num):
    num = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            num += 1 if search(grid, row_num, col_num, i, j) else 0
    return num

total = 0
for row_num in range(grid_size['row']):
    for col_num in range(grid_size['col']):
        if grid[row_num][col_num] == 'X':
            total += search_all(grid, row_num, col_num)

print(total)

def search_diag_x(grid, row_num, col_num, multiplier):
    letters = ('M', 'S')
    return (grid[row_num - 1][col_num - 1*multiplier] in letters and 
            grid[row_num + 1][col_num + 1*multiplier] in letters and
            grid[row_num - 1][col_num - 1*multiplier] != grid[row_num + 1][col_num + 1*multiplier])

def search_x(grid, row_num, col_num):
    if 0 < col_num + 1 < grid_size['col'] and 0 < row_num + 1 < grid_size['row']:
        return search_diag_x(grid, row_num, col_num, 1) and search_diag_x(grid, row_num, col_num, -1)

total = 0
for row_num in range(1, grid_size['row'] - 1):
    for col_num in range(1, grid_size['col'] - 1):
        if grid[row_num][col_num] == 'A':
            total += 1 if search_x(grid, row_num, col_num) else 0

print(total)