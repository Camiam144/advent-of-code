""" 
This word search allows words to be horizontal, vertical, diagonal, written
backwards, or even overlapping other words. It's a little unusual, though, as
you don't merely need to find one instance of XMAS - you need to find all of
them. Here are a few ways XMAS might appear, where irrelevant characters have
been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; 
"""

# Can we iterate through and expand from each letter? Slow but will work:

with open("inputs/day_4.txt", 'r') as f:
    input = f.read()

# input = """MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX"""

target = "XMAS"

num_xmas = 0

#make a list of elements in lines:
blocked = [[elem for elem in line] for line in input.splitlines()]

# for r, line in enumerate(blocked):
#     for c, char in enumerate(line):
#         if char != "X":
#             continue
#         # Need to look at all 8 surrounding chars and follow as long as they
#         # spell XMAS
#         surrounding = [
#             [r + 1, c - 1],
#             [r + 1, c],
#             [r + 1, c + 1],
#             [r, c - 1],
#             [r, c + 1],
#             [r - 1, c - 1],
#             [r - 1, c],
#             [r - 1, c + 1]
#         ]

# Rotate by 45 deg
rotate_45_left = []
rotate_45_right = []
for i in range(len(blocked) + len(blocked[0]) - 1):
    new_row_left = []
    new_row_right = []
    for a in range(len(blocked)):
        for b in range(len(blocked[0]) - 1, -1, -1):
            if a + b == i:
                new_row_right.append(blocked[b][a])
                new_row_left.append(blocked[a][len(blocked[0]) - b - 1])
    rotate_45_left.append(new_row_left)
    rotate_45_right.append(new_row_right)

rotate_90_left = list(zip(*blocked[::-1]))

pt1 = 0
for lst in [blocked, rotate_45_left, rotate_45_right, rotate_90_left]:
    for line in lst:
        text = "".join(line)
        pt1 += text.count(target) + text.count(target[::-1])

print(f"Part 1 xmas: {pt1}")

""" 
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this
isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to
find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Here's the same example from before, but this time all of the X-MASes have been
kept instead:
In this example, an X-MAS appears 9 times.
"""

pt2 = 0
# Can we just "brute force" iterate? Check the regular & 90, then check the 45s?
# We can start 1 in from edge of row/col cuz of orientation.
#(x=1, y=1) -> (x=10, y=1)
#(x=1, y=10) -> (x=1, y=1)
#(x=10, y=1) -> (x=10, y=10)
#(x=10, y=10) -> (x=1, y=10)
# for y in range(1, len(blocked) - 1):
#     for x in range(1, len(blocked[0]) - 1):
#         if blocked[y][x] != "A":
#             continue
#         # Do the "square" crosses first
#         if ((blocked[y][x-1] == "S") and (blocked[y][x+1] == "M")) or \
#             ((blocked[y][x-1] == "M") and (blocked[y][x+1] == "S")):
#             # we found SAM or MAS so check the 90 deg rotation
#             up = rotate_90_left[x][len(blocked[0]) - y]
#             down = rotate_90_left[x][len(blocked[0]) - y]
#             if ((up == "S") and (down == "M")) or \
#                 ((down == "S") and (up == "M")):
#                 pt2 += 1
#         # Now check the 45s:
#         if ((rotate_45_right[x+y][1 - (x + y) - 1] == "S") and (rotate_45_right[x+y][1 - (x + y) + 1] == "M")) or \
#             ((rotate_45_right[x+y][1 - (x + y) - 1] == "M") and (rotate_45_right[x+y][1 - (x + y) + 1] == "S")):
#             # Check other diagonal
#             if (rotate_45_left[len(rotate_45_left)//2 - y][x-1] == "S") and (rotate_45_left[len(rotate_45_left)//2 - y][x+1] == "M") or\
#                 (rotate_45_left[len(rotate_45_left)//2 - y][x-1] == "M") and (rotate_45_left[len(rotate_45_left)//2 - y][x+1] == "S"):
#                 pt2 += 1

# too high
for y in range(1, len(blocked) - 1):
    for x in range(1, len(blocked[0]) - 1):
        if blocked[y][x] != "A":
            continue
        ul = blocked[y-1][x-1]
        ur = blocked[y-1][x+1]
        dl = blocked[y+1][x-1]
        dr = blocked[y+1][x+1]
        lets = "SM"

        # Check X:
        if ul in lets and dr in lets and ul != dr:
            if ur in lets and dl in lets and ur != dl:
                pt2 += 1

print(f"Part 2 x-mas: {pt2}")