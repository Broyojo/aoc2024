with open("2.txt", "r") as f:
    reports = [list(map(int, line.strip().split())) for line in f.readlines()]

num_safe_reports = 0
for report in reports:
    diffs = []
    for i in range(len(report) - 1):
        d = report[i + 1] - report[i]
        diffs.append(d)

    if all(-3 <= d <= -1 for d in diffs) or all(1 <= d <= 3 for d in diffs):
        num_safe_reports += 1

print(num_safe_reports)
