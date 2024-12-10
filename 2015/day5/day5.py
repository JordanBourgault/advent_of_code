import re

words = [line.strip() for line in open('2015/day5/input.txt')]
vowels = 'aeiou'
forbidden = ["ab", "cd", "pq", "xy"]

def check_1(word):
    num_vowels = sum([word.count(vowel) for vowel in vowels])
    repeat = any([word[i] == word[i+1] for i in range(len(word)-1)])
    forbid = any([pair in word for pair in forbidden])
    return num_vowels >= 3 and repeat and not forbid

def check_2(word):
    pairs = [word[i:i+2] for i in range(len(word)-1)]
    match = any([pair_a == pair_b for i, pair_a in enumerate(pairs) for j, pair_b in enumerate(pairs) if abs(i - j) > 1])
    repeat = any([word[i] == word[i+2] for i in range(len(word)-2)])
    return match and repeat

total_1 = 0
total_2 = 0
for word in words:
    if check_1(word): total_1 += 1
    if check_2(word):
        total_2 += 1

print('Part 1:', total_1)
print('Part 2:', total_2)