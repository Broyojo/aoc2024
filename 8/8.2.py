from math import gcd

with open("8.txt", "r") as f:
    grid = [[c for c in line.strip()] for line in f.readlines()]

freq_to_pos = {}
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == ".":
            continue
        freq_to_pos.setdefault(grid[i][j], []).append((i, j))

print(freq_to_pos)


def in_bounds(r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])


antinodes = set()
for freq, pos in freq_to_pos.items():
    n = len(pos)
    if n < 2:
        continue
    for i in range(n):
        r1, c1 = pos[i]
        for j in range(i + 1, n):
            r2, c2 = pos[j]

            dr = r2 - r1
            dc = c2 - c1
            g = gcd(dr, dc)
            dr //= g
            dc //= g

            rr, cc = r1, c1
            while in_bounds(rr, cc):
                antinodes.add((rr, cc))
                rr += dr
                cc += dc

            rr, cc = r1, c1
            while in_bounds(rr, cc):
                antinodes.add((rr, cc))
                rr -= dr
                cc -= dc


print(len(antinodes))
