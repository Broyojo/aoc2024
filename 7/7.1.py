from itertools import product

with open("7.txt", "r") as f:
    equations = []
    for line in f.readlines():
        eq = line.split()
        equations.append([int(eq[0].split(":")[0]), *map(int, eq[1:])])

sum = 0
for eq in equations:
    target = eq[0]
    num_ops = len(eq) - 1
    for p in product(*["+*" for _ in range(num_ops)]):
        result = eq[1]
        for num, op in zip(eq[2:], p):
            if op == "*":
                result *= num
            else:
                result += num

        if result == target:
            sum += result
            break

print(sum)
