""" The unusual data (your puzzle input) consists of many reports, one report
per line. Each report is a list of numbers called levels that are separated by
spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9

This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed
reactor safety systems can only tolerate levels that are either gradually
increasing or gradually decreasing. So, a report only counts as safe if both of
the following are true:

    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

In the example above, the reports can be found safe or unsafe by checking those
rules:

    7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
    1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
    9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
    1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
    8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
    1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.

So, in this example, 2 reports are safe.
"""

reports = []
with open("2024\inputs\day_2.txt", 'r') as f:
    for line in f:
        reports.append([int(x) for x in line.split()])

num_good = 0

for report in reports:
    # Check for all ascending or descending
    if (report != list(sorted(report))) and (report != list(sorted(report, reverse=True))):
        continue
    diffs = []
    for i, val in enumerate(report[1:], start=1):
        prev_val = report[i-1]
        diffs.append(abs(val - prev_val))
    if max(diffs) < 4 and min(diffs) > 0:
        num_good += 1

# print(f"First part solution: {num_good}")

""" The engineers are surprised by the low number of safe reports until they
realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety
systems tolerate a single bad level in what would otherwise be a safe report.
It's like the bad level never happened!

More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

"""

def diff_is_good(diff:list[int]) -> bool:
    """ Return True if a report diff is good """
    diff_dir = all(x > 0 for x in diff) or all(x < 0 for x in diff)
    diff_jump = max([abs(x) for x in diff]) < 4 and min([abs(x) for x in diff]) > 0

    return diff_dir and diff_jump

p2_num_good = 0

for report in reports:
    # P1 Logic: find differences between subsequent numbers. If difference changes
    # sign or if difference is too big or if difference is zero, run is bad.
    diff = [report[i] - report[i-1] for i in range(1, len(report))]
    if all(x == 0 for x in diff):
        continue

    if diff_is_good(diff):
        p2_num_good += 1
    
    else:
        # P2: Find which diffs are bad and try removing numbers on either side
        pos_cnt = sum(1 for x in diff if x > 0)
        neg_cnt = sum(1 for x in diff if x < 0)
        maj_pos = pos_cnt > neg_cnt
        for idx, d in enumerate(diff):
            if abs(d) > 3 or d == 0 or (d < 0 and maj_pos) or (d > 0 and not maj_pos):
                rep1 = [x for i, x in enumerate(report) if i != idx]
                rep2 = [x for i, x in enumerate(report) if i != idx + 1]

                diff1 = [rep1[i] - rep1[i-1] for i in range(1, len(rep1))]
                diff2 = [rep2[i] - rep2[i-1] for i in range(1, len(rep2))]

                if diff_is_good(diff1) or diff_is_good(diff2):
                    p2_num_good+=1
                    break
        

print(f"2nd part solution: {p2_num_good}")