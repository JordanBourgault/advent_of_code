import hashlib

secret = "ckczppom"

res = part_1 = ''
val = -1
while res[:6] != '000000':
    val += 1
    res = hashlib.md5((secret + str(val)).encode()).hexdigest()
    if not part_1 and res[:5] == '00000':
        part_1 = val

print('Part 1:', part_1)
print('Part 2:', val)