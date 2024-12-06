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


sum = 0
for order in orders:
    if validate_order(order):
        midpoint = order[len(order) // 2]
        sum += int(midpoint)
print(sum)
