""" Maybe the lists are only off by a small amount! To find out, pair up the
numbers and measure how far apart they are. Pair up the smallest number in the
left list with the smallest number in the right list, then the second-smallest
left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to 
add up all of those distances. For example, if you pair up a 3 from the left list
with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a
3, the distance apart is 6.

For example:
3   4
4   3
2   5
1   3
3   9
3   3

In the example list above, the pairs and distances would be as follows:

    The smallest number in the left list is 1, and the smallest number in the
    right list is 3. The distance between them is 2.
    The second-smallest number in the left list is 2, and the second-smallest
    number in the right list is another 3. The distance between them is 1.
    The third-smallest number in both lists is 3, so the distance between them is 0.
    The next numbers to pair up are 3 and 4, a distance of 1.
    The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
    Finally, the largest number in the left list is 4, while the largest number
    in the right list is 9; these are a distance 5 apart.

To find the total distance between the left list and the right list, add up the
distances between all of the pairs you found. In the example above, this is
2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

"""

# Load data
first_list = []
second_list = []

with open('2024\inputs\day_1.txt', 'r') as f:
    for line in f:
        l = line.strip().split()
        first_list.append(int(l[0]))
        second_list.append(int(l[1]))

sort_first = sorted(first_list)
sort_second = sorted(second_list)

total = 0
for first, second in zip(sort_first, sort_second):
    total += (first - second) if (first - second) >= 0 else (second - first)

print("Part 1 answer:")
print(total)

""" Part 2: 
This time, you'll need to figure out exactly how often each number from the left 
ist appears in the right list. Calculate a total similarity score by adding up
each number in the left list after multiplying it by the number of times that
number appears in the right list.
"""

# We do a little hash map, keys are left list, vals are right list
hash_map = {}
for left in sort_first:
    hash_map[left] = 0

for right in sort_second:
    try:
        hash_map[right] += 1
    except KeyError:
        pass

sim_score = 0

for k, v in hash_map.items():
    sim_score += k * v

print("Part 2 answer:")
print(sim_score)
