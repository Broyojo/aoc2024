from tqdm import tqdm

with open("6.txt", "r") as f:
    grid = [[c for c in line.strip()] for line in f.readlines()]


def find_guard(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return (i, j)
    raise ValueError("couldn't find guard")


def print_grid(grid):
    for row in grid:
        for item in row:
            print(item, end=" ")
        print()


def step(grid, i, j):
    guard = grid[i][j]
    match guard:
        case "^":
            if i > 0:
                if grid[i - 1][j] in ["#", "O"]:
                    grid[i][j] = ">"
                    return i, j, grid[i][j]
                else:
                    grid[i][j] = "."
                    grid[i - 1][j] = "^"
                    return i - 1, j, grid[i - 1][j]
        case ">":
            if j < len(grid[0]) - 1:
                if grid[i][j + 1] in ["#", "O"]:
                    grid[i][j] = "v"
                    return i, j, grid[i][j]
                else:
                    grid[i][j] = "."
                    grid[i][j + 1] = ">"
                    return i, j + 1, grid[i][j + 1]
        case "v":
            if i < len(grid) - 1:
                if grid[i + 1][j] in ["#", "O"]:
                    grid[i][j] = "<"
                    return i, j, grid[i][j]
                else:
                    grid[i][j] = "."
                    grid[i + 1][j] = "v"
                    return i + 1, j, grid[i + 1][j]
        case "<":
            if j > 0:
                if grid[i][j - 1] in ["#", "O"]:
                    grid[i][j] = "^"
                    return i, j, grid[i][j]
                else:
                    grid[i][j] = "."
                    grid[i][j - 1] = "<"
                    return i, j - 1, grid[i][j - 1]
    grid[i][j] = "."
    # print_grid(grid)


cycles = 0
gi_o, gj_o = find_guard(grid)
for i in tqdm(range(len(grid))):
    for j in range(len(grid[0])):
        if grid[i][j] != ".":
            continue

        grid_copy = [row[:] for row in grid]
        grid_copy[i][j] = "O"

        gi, gj = gi_o, gj_o
        visits = {(gi, gj): {"^"}}

        while c := step(grid_copy, gi, gj):
            gi, gj, guard = c
            if (gi, gj) not in visits:
                visits[(gi, gj)] = {guard}
            else:
                if guard in visits[(gi, gj)]:
                    cycles += 1
                    break
                else:
                    visits[(gi, gj)].add(guard)

print(cycles)
