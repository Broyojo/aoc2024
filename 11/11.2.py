from functools import lru_cache

with open("11.txt", "r") as f:
    stones = [int(s) for s in f.read().split() if s.isalnum()]

"""
   125
    |
  253000
   /   \
 253    0
  |     |  
512072  1

etc.
"""


@lru_cache(maxsize=None)
def num_stones(stones, times):
    if times == 0:
        return len(stones)

    total_num = 0
    for stone in stones:
        children = []
        if stone == 0:
            children.append(1)
        else:
            digits = str(stone)
            if len(digits) % 2 == 0:
                left = digits[: len(digits) // 2]
                right = digits[len(digits) // 2 :]
                children.append(int(left))
                children.append(int(right))
            else:
                children.append(stone * 2024)

        num = num_stones(tuple(children), times - 1)
        total_num += num

    return total_num


print(num_stones(tuple(stones), times=75))
