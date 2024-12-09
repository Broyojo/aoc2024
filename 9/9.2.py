from tqdm import tqdm

with open("9.txt", "r") as f:
    data = f.read().strip()


def format(data):
    disk = []
    block_id = 0
    for i in range(len(data)):
        if i % 2 == 0:
            disk.append((block_id, int(data[i])))
            block_id += 1
        else:
            disk.append((-1, int(data[i])))
    return disk


def compact(disk: list):
    for id in tqdm(range(max(disk, key=lambda x: x[0])[0], -1, -1)):
        for j in range(len(disk)):
            if disk[j][0] == id:
                break
        for i in range(j + 1):
            if disk[i][0] != -1:
                continue
            if disk[i][1] >= disk[j][1]:
                if disk[i][1] > disk[j][1]:
                    left_over = (-1, disk[i][1] - disk[j][1])
                    empty = (-1, disk[j][1])
                    disk[i] = disk[j]
                    disk[j] = empty
                    disk.insert(i + 1, left_over)
                else:
                    disk[i], disk[j] = disk[j], disk[i]
                break
    return disk


def flatten(disk):
    flat = []
    for id, size in disk:
        for _ in range(size):
            flat.append(id)
    return flat


def pretty_print(disk):
    for id in flatten(disk):
        if id == -1:
            print(".", end="")
        else:
            print(id, end="")
    print(flush=True)


def checksum(disk):
    s = 0
    for i, id in enumerate(disk):
        if id != -1:
            s += i * id
    return s


disk = format(data)
disk = compact(disk)
pretty_print(disk)
print(checksum(flatten(disk)))
