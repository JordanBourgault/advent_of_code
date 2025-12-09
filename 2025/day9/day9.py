from queue import Queue

with open("2025/day9/input.txt") as f:
    boxes = [tuple(map(int, coord.strip().split(','))) for coord in f]

x_coords = list({box[0] for box in boxes})
compressed_x_map = {i+1: val  for i, val in enumerate(sorted(x_coords))}
compressed_x_reverse_map = {val: i+1  for i, val in enumerate(sorted(x_coords))}

y_coords = list({box[1] for box in boxes})
compressed_y_map = {i+1: val  for i, val in enumerate(sorted(y_coords))}
compressed_y_reverse_map = {val: i+1  for i, val in enumerate(sorted(y_coords))}

compressed_boxes = [(compressed_x_reverse_map[x], compressed_y_reverse_map[y]) for x,y in boxes]


def get_box_diff(box1, box2):
    return box1[0] - box2[0], box1[1] - box2[1]

def get_grid_size(grid):
    max_x, max_y = max([int(v.real) for v in grid.keys()])+1, max([int(v.imag) for v in grid.keys()])+1
    return max_x, max_y

def draw_grid(grid):
    max_x, max_y = get_grid_size(grid)
    for y in range(max_y+1):
        for x in range(max_x+1):
            if complex(x, y) not in grid:
                print('.', end='')
            else:
                print(grid[complex(x, y)], end='')
        print('')


def draw_line(last_box, box, grid):
    diff = get_box_diff(last_box, box)
    if diff[0] and diff[1]:
        raise Exception('Having two different values is not allowed')
    if diff[0]:
        direction = 1 if diff[0] < 0 else -1
        for x in range(last_box[0], box[0], direction):
            if complex(x, box[1]) not in grid:
                grid[complex(x, box[1])] = 'G'
                # draw_grid(grid)
    else:
        direction = 1 if diff[1] < 0 else -1
        for y in range(last_box[1], box[1], direction):
            if complex(box[0], y) not in grid:
                grid[complex(box[0], y)] = 'G'
                # draw_grid(grid)

def build_outline(boxes):
    grid = dict()
    first_box = None
    last_box = None
    for box in boxes:
        if not last_box:
            grid[complex(*box)] = 'R'
            first_box = box
            last_box = box
            continue
        grid[complex(*box)] = 'R'
        draw_line(last_box, box, grid)
        last_box = box
    draw_line(last_box, first_box, grid)
    return grid


def get_start_pos(grid):
    max_x, max_y = get_grid_size(grid)
    inside = False
    start_y = max_y//2
    for x in range(max_x):
        if complex(x, start_y) in grid:
            inside = True
        if inside and complex(x, start_y) not in grid:
            return complex(x, start_y)


def fill_grid(grid, coords_to_check: Queue, checked_coords: set):
    start = coords_to_check.get()
    checked_coords.add(start)
    grid[start] = 'I'
    # up, down, left, right
    directions = [start-1j, start+1j, start-1, start+1]
    for d in directions:
        if d not in grid:
            grid[d] = 'I'
            # draw_grid(grid)
            if d not in checked_coords:
                checked_coords.add(d)
                coords_to_check.put(d)
            # print('')


def check_box_contents(box1, box2, grid):
    x_coord = sorted([box1[0], box2[0]])
    y_coord = sorted([box1[1], box2[1]])
    x_coord[1] += 1
    y_coord[1] += 1
    for x in range(*x_coord):
        for y in range(*y_coord):
            if not complex(x, y) in grid:
                return False
    return True

def get_box_size(box1, box2):
    return (abs((compressed_x_map[box1[0]] - compressed_x_map[box2[0]]))+1) * (abs(compressed_y_map[box1[1]] - compressed_y_map[box2[1]])+1)

def get_biggest_box(grid):
    checked_boxes = 0
    largest_box = 0
    largest_part2_box = 0
    for box1 in compressed_boxes:
        for box2 in compressed_boxes:
            checked_boxes += 1
            box_size = get_box_size(box1, box2)
            box_valid = check_box_contents(box1, box2, grid)
            if largest_box < box_size:
                largest_box = box_size
            if box_valid and largest_part2_box < box_size:
                largest_part2_box = box_size
    return largest_box, largest_part2_box



grid = build_outline(compressed_boxes)

coords_to_check = Queue()
checked_coords = set()
start = get_start_pos(grid)
coords_to_check.put(start)
while not coords_to_check.empty():
    fill_grid(grid, coords_to_check, checked_coords)

res = get_biggest_box(grid)
print('Part 1: ', res[0])
print('Part 2: ', res[1])
