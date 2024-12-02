list1, list2 = [], []
with open("1.txt", "r") as f:
    for line in f.readlines():
        num1, num2 = line.split()
        list1.append(int(num1))
        list2.append(int(num2))

list2_freqs = {}
for num in list2:
    if num not in list2_freqs:
        list2_freqs[num] = 1
    else:
        list2_freqs[num] += 1

similarity_score = 0
for num in list1:
    times = 0
    if num in list2_freqs:
        times = list2_freqs[num]
    similarity_score += num * times

print(similarity_score)
