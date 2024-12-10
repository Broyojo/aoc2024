with open("10.txt", "r") as f:
    grid = [[int(c) for c in line.strip()] for line in f.readlines()]


def find_starts(grid):
    coords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                coords.append((i, j))
    return coords


def get_neighbors(grid, coord):
    neighbors = []
    if coord[0] > 0:
        neighbors.append((coord[0] - 1, coord[1]))
    if coord[0] < len(grid) - 1:
        neighbors.append((coord[0] + 1, coord[1]))
    if coord[1] > 0:
        neighbors.append((coord[0], coord[1] - 1))
    if coord[1] < len(grid[0]) - 1:
        neighbors.append((coord[0], coord[1] + 1))
    return neighbors


def rate(grid, coord):
    height = grid[coord[0]][coord[1]]

    if height == 9:
        return 1

    next_positions = [
        n for n in get_neighbors(grid, coord) if grid[n[0]][n[1]] == height + 1
    ]

    ratings = [rate(grid, pos) for pos in next_positions]

    return sum(ratings)


starts = find_starts(grid)
total_rating = 0
for start in starts:
    rating = rate(grid, start)
    total_rating += rating
print(total_rating)
