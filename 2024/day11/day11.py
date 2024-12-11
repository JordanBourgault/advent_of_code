import time
from functools import cache

stones = {stone: 1 for stone in open('2024/day11/input.txt').read().strip().split(' ')}
start = time.time()


@cache
def process_stone(stone):
    if stone == '0':
        ret = '1'
    elif not len(stone) % 2:
        half = len(stone)//2
        ret = [stone[:half], str(int(stone[half:]))]
    else:
        ret = [str(int(stone) * 2024)]
    return ret

def blink(stones:dict, n):
    for _ in range(n):
        new_stones = dict()
        for stone, num in stones.items():
            for new_stone in process_stone(stone):
                value = new_stones.get(new_stone, 0)
                new_stones[new_stone] = value + num
        stones = new_stones
    return stones


stones = blink(stones, 25)
print('Part 1:', sum(stones.values()))
stones = blink(stones, 50)
print('Part 2:', sum(stones.values()))

print(time.time() - start)