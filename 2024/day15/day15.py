import readchar

with open('2024/day15/input.txt') as f:
    data = f.read()
    grid, moves = data.split('\n\n')
    wide_grid = grid.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
    moves = ''.join(moves.split('\n'))
    n_rows_wide, n_cols_wide = len(wide_grid.split('\n')), len(wide_grid.split('\n')[0])
    n_rows, n_cols = len(grid.split('\n')), len(grid.split('\n')[0])
    grid = {complex(i, j): val for i, row in enumerate(grid.split('\n')) for j, val in enumerate(row)}
    wide_grid = {complex(i, j): val for i, row in enumerate(wide_grid.split('\n')) for j, val in enumerate(row)}
    current_pos = list(grid.keys())[list(grid.values()).index('@')]
    current_pos_wide = list(wide_grid.keys())[list(wide_grid.values()).index('@')]


directions = {
        '^': -1,
        'v': 1,
        '<': -1j,
        '>': 1j
        }


def check_space(start, dir):
    pos = start + dir
    i = 1
    while True:
        val = grid[pos]
        if val == '#':
            return False
        if val == '.':
            return start + i*dir
        pos += dir
        i +=1


def move_box(grid, start, dir, move=True):
    def move_vert(grid, pos, dir):
        grid[pos[0]] = '['
        grid[pos[1]] = ']'
        grid[pos[0]-dir] = '.'
        grid[pos[1]-dir] = '.'

    def move_hor(grid, start, next_pos, dir):
        grid[next_pos+dir] = grid[next_pos]
        grid[next_pos] = grid[start]
        grid[start] = '.'

    val = grid[start]
    next_pos = start + dir
    # Moving up or down
    if dir.real:
        if val == '[':
            to_check = [next_pos, complex(next_pos.real, next_pos.imag+1)]
        else:
            to_check = [complex(next_pos.real, next_pos.imag-1), next_pos]
        
        vals = [grid[r] for r in to_check]
        if any([val == '#' for val in vals]):
            return False
        
        elif all([val == '.' for val in vals]):
            if move:
                move_vert(grid, to_check, dir)
            return True
        
        else:
            # Box aligned with other box
            if vals == ['[', ']']:
                if move_box(grid, next_pos, dir, move=move):
                    if move:
                        move_vert(grid, to_check, dir)
                    return True
            else:
                # Check without moving
                if all([(move_box(grid, to_check[row], dir, move=False)) for row, val in enumerate(vals) if val in ['[', ']']]):
                    if move:
                        [(move_box(grid, to_check[row], dir, move=True)) for row, val in enumerate(vals) if val in ['[', ']']]
                        move_vert(grid, to_check, dir)
                    return True
        return False

    # Moving left or right
    else:
        next_box_pos = start + 2*dir
        val = grid[next_box_pos]
        if val == '#':
            return False
        if val == '.':
            move_hor(grid, start, next_pos, dir)
            return True
        else:
            if move_box(grid, next_box_pos, dir):
                move_hor(grid, start, next_pos, dir)
                return True
        return False

def draw(grid, n_rows, n_cols):
    for i in range(n_rows):
        print(''.join(list(grid.values())[i*n_cols:(i+1)*n_cols]))
    print()


def collision(grid, current_pos, next_pos, move):
    if free_space := check_space(next_pos, directions[move]):
        grid[free_space] = 'O'
        grid[next_pos] = '@'
        grid[current_pos] = '.'
        current_pos = next_pos
    return current_pos

def collision_wide(grid, current_pos, next_pos, move):
    if move_box(grid, next_pos, directions[move]):
        grid[next_pos] = '@'
        grid[current_pos] = '.'
        current_pos = next_pos
    return current_pos

def simulate_robot(grid, current_pos, move, collision_fun):
    next_pos = current_pos + directions[move]
    if grid[next_pos] == '.':
        grid[next_pos] = '@'
        grid[current_pos] = '.'
        return next_pos
    elif grid[next_pos] == '#':
        return current_pos
    else:
        return collision_fun(grid, current_pos, next_pos, move)


for move in moves:
    current_pos = simulate_robot(grid, current_pos, move, collision)
    current_pos_wide = simulate_robot(wide_grid, current_pos_wide, move, collision_wide)

draw(grid, n_rows, n_cols)
draw(wide_grid, n_rows_wide, n_cols_wide)


def count_gps(grid, box_key):
    return int(sum([100*key.real + key.imag for key, value in grid.items() if value == box_key]))

print('Part 1:', count_gps(grid, 'O'))
print('Part 2:', count_gps(wide_grid, '['))
