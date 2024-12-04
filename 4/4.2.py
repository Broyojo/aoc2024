with open("4.txt", "r") as f:
    grid = [[c for c in line.strip()] for line in f.readlines()]

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
            continue
        if grid[i][j] == "A":
            ld = grid[i - 1][j - 1] + grid[i + 1][j + 1]
            rd = grid[i - 1][j + 1] + grid[i + 1][j - 1]
            if ld in ["MS", "SM"] and rd in ["MS", "SM"]:
                count += 1
print(count)
