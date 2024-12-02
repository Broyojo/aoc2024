with open("2.txt", "r") as f:
    reports = [list(map(int, line.strip().split())) for line in f.readlines()]


def is_safe(report):
    diffs = []
    for i in range(len(report) - 1):
        d = report[i + 1] - report[i]
        diffs.append(d)
    return all(-3 <= d <= -1 for d in diffs) or all(1 <= d <= 3 for d in diffs)


def is_safe_problem_dampener(report):
    if is_safe(report):
        print(report)
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1 :]
        if is_safe(modified_report):
            print(report, "remove", report[i])
            return True

    return False


num_safe_reports = 0
for report in reports:
    if is_safe_problem_dampener(report):
        num_safe_reports += 1
print(num_safe_reports)
