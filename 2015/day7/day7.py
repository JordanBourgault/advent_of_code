import ctypes

with open("2015/day7/input.txt") as f:
    data = [line.strip().split(' -> ') for line in f]
    # print(data)

bit_mask = 0xffff

res = dict()
for operation, destination in data:
    try:
        split_op = operation.split(' ')

        if split_op[0].isnumeric():
            op = int(split_op[0])
        else:
            op = split_op[0] if split_op[0] == 'NOT' else res[split_op[0]]

        if len(split_op) == 1:
            res[destination] = op & bit_mask
            continue
        elif len(split_op) == 2:
            res[destination] = (~ res[split_op[1]]) & bit_mask
            continue

        if split_op[2].isnumeric():
            operand = int(split_op[2])
        else:
            operand = res[split_op[2]]
        
        if split_op[1] == 'AND':
            res[destination] = (op & operand) & bit_mask
        elif split_op[1] == 'OR':
            res[destination] = (op | operand) & bit_mask
        elif split_op[1] == 'LSHIFT':
            res[destination] = (op << operand) & bit_mask
        elif split_op[1] == 'RSHIFT':
            res[destination] = (op >> operand) & bit_mask
    except KeyError:
        data.append((operation, destination))


print(dict(sorted(res.items())))