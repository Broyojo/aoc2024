import re

with open("3.txt", "r") as f:
    memory = f.read()

instructions = re.findall("(mul\\(\\d+,\\d+\\)|do\\(\\)|don't\\(\\))", memory)

sum = 0
enabled = True
for instr in instructions:
    match instr:
        case "don't()":
            enabled = False
        case "do()":
            enabled = True
        case mul:
            if enabled:
                nums = re.findall("\\d+", mul)
                sum += int(nums[0]) * int(nums[1])

print(sum)
