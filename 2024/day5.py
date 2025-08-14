""" 
https://adventofcode.com/2024/day/5

47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

from functools import cmp_to_key

# input = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

with open("inputs/day_5.txt", 'r') as f:
    input = f.read()

# Parse input

rules, orders = input.split("\n\n")

rule_map = {}

split_rules = []

for rule in rules.splitlines():
    split_rule = rule.split("|")
    split_rules.append((split_rule[0], split_rule[1]))
    try:
        rule_map[split_rule[0]].append(split_rule[1])
    except KeyError:
        rule_map[split_rule[0]] = [split_rule[1]]


def is_subset_good(pg:str, pgs:list[str], mapping:dict[str:list[str]]) -> bool:
    try:
        valid_pgs = mapping[pg]
    except KeyError:
        return False
    for p in pgs:
        if p not in valid_pgs:
            return False
    return True


def is_order_good(order:list[str], mapping:dict[str:list[str]]) -> bool:
    for i, pg in enumerate(order):
        if i == (len(order) - 1):
            return True
        if not is_subset_good(pg, order[i+1:], mapping):
            return False


pt1 = 0
for order in orders.splitlines():
    split_order = [x for x in order.split(",")]
    if is_order_good(split_order, rule_map):
        pt1 += int(split_order[len(split_order)//2])
    
print(f"Part 1 answer: {pt1}")

# There might be a good way to do this, but can we just iterate over each wrong order
# until it is properly sorted?

def custom_comp(item1:str, item2:str) -> int:
    for rule in split_rules:
        if rule[0] == item1 and rule[1] == item2:
            return -1
        elif rule[0] == item2 and rule[1] == item1:
            return 1
        else:
            continue
    return 0

pt2 = 0
for order in orders.splitlines():
    split_order = [x for x in order.split(",")]
    if not is_order_good(split_order, rule_map):
        correct_order = sorted(split_order, key=cmp_to_key(custom_comp))
        pt2 += int(correct_order[len(correct_order)//2])

print(f"Part 2 answer: {pt2}")