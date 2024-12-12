with open("11.txt", "r") as f:
    stones = [int(s) for s in f.read().split() if s.isalnum()]


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        else:
            digits = str(stone)
            if len(digits) % 2 == 0:
                left = digits[: len(digits) // 2]
                right = digits[len(digits) // 2 :]
                new_stones.append(int(left))
                new_stones.append(int(right))
            else:
                new_stones.append(stone * 2024)
    return new_stones


for i in range(25):
    stones = blink(stones)

print(len(stones))
