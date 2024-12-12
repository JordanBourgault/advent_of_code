from collections import defaultdict

with open('2024/day12/input.txt') as f:
    data = [[col for col in row.strip()] for row in f]

def get_neighbours(coord):
    return [coord+1, coord-1, coord+1j, coord-1j]

plot_dict = defaultdict(lambda:[])
for row_num, row in enumerate(data):
    for col_num, col in enumerate(row):
        coord = complex(row_num, col_num)
        neihgbours = get_neighbours(coord)
        matched = None
        added = False
        i = 0
        while i < (len(plot_dict[col])):
            plot = plot_dict[col][i]
            if any([neihgbour in plot for neihgbour in neihgbours]):
                added = True
                if matched is not None:
                    plot_dict[col][matched].update(plot)
                    plot_dict[col].pop(i)
                else:
                    plot.add(coord)
                    matched = i
            i += 1

        if not added:
            plot_dict[col].append(set([coord]))


def get_num_neighbours(coord, plot):
    return sum([1 if neighbour in plot else 0 for neighbour in get_neighbours(coord)])

def get_range(plot:complex):
    real = [int(p.real) for p in plot]
    imag = [int(p.imag) for p in plot]
    return (min(real), max(real)+1), (min(imag), max(imag)+1)

def scan_sides(plot):
    row_range, col_range = get_range(plot)
    num_sides = 0
    for row in range(*row_range):
        up_row = set()
        down_row = set()
        for col in range(*col_range):
            coord = complex(row, col) 
            if coord in plot:
                if (coord - 1) not in plot:
                    up_row.add(coord)
                    if not get_num_neighbours(complex(row, col), up_row):
                        num_sides += 1
                if (coord + 1) not in plot:
                    down_row.add(coord)
                    if not get_num_neighbours(complex(row, col), down_row):
                        num_sides += 1

    for col in range(*col_range):
        left_col = set()
        right_col = set()
        for row in range(*row_range):
            coord = complex(row, col) 
            if coord in plot:
                if (coord - 1j) not in plot:
                    left_col.add(coord)
                    if not get_num_neighbours(complex(row, col), left_col):
                        num_sides += 1
                if (coord + 1j) not in plot:
                    right_col.add(coord)
                    if not get_num_neighbours(complex(row, col), right_col):
                        num_sides += 1
    return num_sides


total = 0
total_bulk = 0
for key, values in plot_dict.items():
    for plot in values:
        fence_len = 0
        for value in plot:
            num_neighbours = get_num_neighbours(value, plot)
            fence_len += 4 - num_neighbours
        total += len(plot) * fence_len
        total_bulk += len(plot) * scan_sides(plot)
        # print(key, len(plot), fence_len, scan_sides(plot))


print('Part 1:', total)
print('Part 2:', total_bulk)
