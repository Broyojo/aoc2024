list1, list2 = [], []
with open("1.txt", "r") as f:
    for line in f.readlines():
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

list1.sort()
list2.sort()

total_distance = 0
for num1, num2 in zip(list1, list2):
    diff = abs(num1 - num2)
    total_distance += diff
print(total_distance)
