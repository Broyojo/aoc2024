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


def explore(grid, coord, trail_ends):
    height = grid[coord[0]][coord[1]]

    if height == 9:
        trail_ends.add(coord)
        return

    next_positions = [
        n for n in get_neighbors(grid, coord) if grid[n[0]][n[1]] == height + 1
    ]

    for pos in next_positions:
        explore(grid, pos, trail_ends)


starts = find_starts(grid)
total_score = 0
for start in starts:
    trail_ends = set()
    explore(grid, start, trail_ends)
    score = len(trail_ends)
    total_score += score
print(total_score)
