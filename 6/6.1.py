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
                if grid[i - 1][j] == "#":
                    grid[i][j] = ">"
                    return i, j
                else:
                    grid[i][j] = "X"
                    grid[i - 1][j] = "^"
                    return i - 1, j
        case ">":
            if j < len(grid[0]) - 1:
                if grid[i][j + 1] == "#":
                    grid[i][j] = "v"
                    return i, j
                else:
                    grid[i][j] = "X"
                    grid[i][j + 1] = ">"
                    return i, j + 1
        case "v":
            if i < len(grid) - 1:
                if grid[i + 1][j] == "#":
                    grid[i][j] = "<"
                    return i, j
                else:
                    grid[i][j] = "X"
                    grid[i + 1][j] = "v"
                    return i + 1, j
        case "<":
            if j > 0:
                if grid[i][j - 1] == "#":
                    grid[i][j] = "^"
                    return i, j
                else:
                    grid[i][j] = "X"
                    grid[i][j - 1] = "<"
                    return i, j - 1
    grid[i][j] = "X"


def count_xs(grid):
    count = 0
    for row in grid:
        for item in row:
            if item == "X":
                count += 1
    return count


i, j = find_guard(grid)

while c := step(grid, i, j):
    i, j = c

print_grid(grid)
print(count_xs(grid))
