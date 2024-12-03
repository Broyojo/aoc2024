import re

with open("3.txt", "r") as f:
    memory = f.read()

muls = re.findall("mul\\(\\d+,\\d+\\)", memory)
sum = 0
for mul in muls:
    nums = re.findall("\\d+", mul)
    sum += int(nums[0]) * int(nums[1])
print(sum)
