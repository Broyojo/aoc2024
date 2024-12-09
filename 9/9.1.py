with open("9.txt", "r") as f:
    data = f.read().strip()


def format(data):
    disk = []
    block_id = 0
    for i in range(len(data)):
        if i % 2 == 0:
            for _ in range(int(data[i])):
                disk.append(block_id)
            block_id += 1
        else:
            for _ in range(int(data[i])):
                disk.append(-1)
    return disk


def compact(disk):
    i = 0
    j = len(disk) - 1
    while i <= j:
        if disk[j] == -1:
            j -= 1
            continue
        if disk[i] != -1:
            i += 1
            continue
        disk[i], disk[j] = disk[j], disk[i]
        i += 1
        j -= 1
    return disk


def checksum(disk):
    s = 0
    for i, id in enumerate(disk):
        if id == -1:
            break
        s += i * id
    return s


disk = format(data)
print(disk)
disk = compact(disk)
print(disk)
print(checksum(disk))
