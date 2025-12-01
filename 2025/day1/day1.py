def solve():
    with open("2025/day1/input.txt") as f:
        pos = 50
        counter = 0
        last_overlap = 0
        overlap_counter = 0
        for line in f:
            line = line.strip()
            direction, distance = 1 if line[:1] == 'R' else -1, int(line[1:])
            old_pos = pos
            pos += direction * distance

            # Part 1
            if pos % 100 == 0:
                counter += 1

            # Part 2
            overlap = pos // 100
            if last_overlap != overlap:
                overlap_counter += abs(last_overlap - overlap)
                # Moving from 0 to the left should not count as an additionnal overlap
                if old_pos % 100 == 0 and direction == 'L':
                    overlap_counter -= 1
                last_overlap = overlap
            # Landing on 0 from the left should count
            if pos % 100 == 0 and direction == 'L':
                overlap_counter += 1
            
        return counter, overlap_counter

counter, overlap_counter = solve()

print('Part 1: ', counter)
print('Part 2: ', overlap_counter)
