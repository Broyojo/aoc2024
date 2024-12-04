import re

with open("4.txt", "r") as f:
    grid = [[c for c in line.strip()] for line in f.readlines()]


def rows(grid):
    return ["".join(row) for row in grid]


def columns(grid):
    cols = []
    for j in range(len(grid[0])):
        col = ""
        for i in range(len(grid)):
            col += grid[i][j]
        cols.append(col)
    return cols


def diagonals(grid):
    left_diag = [[] for _ in range(len(grid) + len(grid[0]) - 1)]
    right_diag = [[] for _ in range(len(grid) + len(grid[0]) - 1)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            left_diag[i + j].append(grid[i][j])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            right_diag[i - j + (len(grid[0]) - 1)].append(grid[i][j])

    return ["".join(d) for d in left_diag], ["".join(d) for d in right_diag]


def num_matches(strings, word):
    count = 0
    for s in strings:
        count += len(re.findall(word, s)) + len(re.findall(word[::-1], s))
    return count


rs = rows(grid)
cs = columns(grid)
ld, rd = diagonals(grid)

total_matches = (
    num_matches(rs, "XMAS")
    + num_matches(cs, "XMAS")
    + num_matches(ld, "XMAS")
    + num_matches(rd, "XMAS")
)

print(total_matches)
