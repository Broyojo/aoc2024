from functools import cmp_to_key, lru_cache

with open("5.txt", "r") as f:
    section1, section2 = f.read().split("\n\n")

successors = {}
for line in section1.split("\n"):
    a, b = line.split("|")
    if a in successors:
        successors[a].add(b)
    else:
        successors[a] = {b}


def get_all_successors(start_page, order):
    if start_page not in successors:
        return set()

    visited = set()
    stack = [start_page]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            stack.extend([s for s in successors.get(current, []) if s in order])

    return visited - {start_page}


orders = [line.split(",") for line in section2.split("\n")]


def validate_order(order):
    for i in range(len(order)):
        succs = get_all_successors(order[i], order)
        for j in range(i + 1, len(order)):
            if order[j] not in succs:
                return False
    return True


def lt(a, b, order):
    succs = get_all_successors(a, order)
    return b in succs


def fix(order):
    def compare(a, b):
        if lt(a, b, order):
            return -1
        elif lt(b, a, order):
            return 1
        else:
            return 0

    fixed_order = sorted(order, key=cmp_to_key(compare))
    return fixed_order


sum = 0
for order in orders:
    if not validate_order(order):
        fixed_order = fix(order)
        midpoint = fixed_order[len(fixed_order) // 2]
        sum += int(midpoint)
print(sum)
