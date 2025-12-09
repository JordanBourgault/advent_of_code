from functools import lru_cache

with open("2025/day7/input.txt") as f:
    d = {}
    f = f.read().split('\n')
    y_range = len(f)
    for y, line in enumerate(f):
        x_range = len(line)
        for x, char in enumerate(line.strip()):
            d[complex(x, y)] = char

start = list(d.keys())[list(d.values()).index('S')]

splitters = set()
@lru_cache(maxsize=None)
def propagate_beam(start: complex, ends=0):
    beam_pos = start
    try:
        while d[beam_pos] != '^':
            beam_pos += 1j
    except:
        # Beam escapes from the bottom
        if beam_pos.imag >= y_range-1:
            return ends+1
        else:
            print('out of range horizontaly')
            
    splitters.add(beam_pos)
    left_ends = propagate_beam(beam_pos-1, ends)
    right_ends = propagate_beam(beam_pos+1, ends)
    return left_ends + right_ends

res = propagate_beam(start)
print('Part 1: ', len(splitters))
print('Part 2: ', res)
