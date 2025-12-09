import math
from copy import deepcopy

with open("2025/day8/input.txt") as f:
    boxes = [list(map(int,line.split(','))) for line in f]

# @lru_cache(maxsize=None)
def euclidian_distance(box1, box2):
    x = math.pow(box1[0] - box2[0], 2)
    y = math.pow(box1[1] - box2[1], 2)
    z = math.pow(box1[2] - box2[2], 2)
    return math.sqrt(x + y + z)


def closest_box():
    return [[euclidian_distance(boxes[j], other), i, j] for i, other in enumerate(boxes) for j in range(i, len(boxes)) if i != j]


sorted_mins = sorted(closest_box())
def connect():
    part_1_set = []
    sets = []
    for i in range(0, len(sorted_mins)):
        _, box1, box2 = sorted_mins[i]
        box_1_set = None
        box_2_set = None
        for j, s in enumerate(sets):
            if box1 in s:
                box_1_set = j
            if box2 in s:
                box_2_set = j
        
        # Both boxes are currently not in any sets, create a new set
        if box_1_set is None and box_2_set is None:
            sets.append(set([box1, box2]))
        # The boxes are already in different sets, we need to merge
        elif box_1_set is not None and box_2_set is not None and box_1_set != box_2_set:
            sets[box_1_set] = sets[box_1_set] | sets[box_2_set]
            sets.pop(box_2_set)
        # Box 1 exists but no box 2
        elif box_1_set is not None:
            sets[box_1_set].add(box2)
        # Box 2 exists but not box 1
        else:
            sets[box_2_set].add(box1)

        # 1000 connections
        if i == 999:
            print(sets)
            part_1_set = deepcopy(sets)
        
        if len(sets) == 1 and len(sets[0]) == len(boxes):
            return part_1_set, box1, box2
        
        print(len(sets))

part1, box1, box2 = connect()
set_len = sorted([len(s) for s in part1], reverse=True)
print('Part 1: ', math.prod(set_len[:3]))
print(box1, box2)
print(boxes[box1], boxes[box2])
print('Part 2: ', boxes[box1][0] * boxes[box2][0])
