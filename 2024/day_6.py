""" Similar to a previous puzzle from last year kind of:

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...

The map shows the current position of the guard with ^ (to indicate the guard is
currently facing up from the perspective of the map). Any obstructions - crates,
desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves
repeatedly following these steps:

If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.

In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit
before leaving the mapped area?
"""

from itertools import cycle

# input_text = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

with open("inputs/day_6.txt", 'r') as f:
    input_text = f.read()

# Find the character (we know there is exactly 1)
idx = input_text.replace("\n","").find("^")
# Break the puzzle into a grid:
grid = [[y for y in x] for x in input_text.splitlines()]
# Get character coord:
row_guard = idx // len(grid[0])
col_guard = idx % len(grid[0])

##### This doesn't count unique places, only counts total steps
# pt1 = 1
# # We're going to rotate the frame of reference so we're always walking "right"
# grid = list(zip(*grid[::-1]))
# grid = [list(x) for x in grid]
# current_row = col_guard
# current_col = len(grid[0]) - row_guard - 1

# # Walk until we fall off:

# while current_col + 1 < len(grid[current_row]):
#     to_step = grid[current_row][current_col + 1]
#     if to_step != "#":
#         grid[current_row][current_col] = "."
#         pt1 += 1
#         current_col += 1
#         grid[current_row][current_col] = "^"

#     elif to_step == "#":
#         # Rotate the grid to the left (so we keep walking right)
#         grid = list(zip(*grid))[::-1]
#         grid = [list(x) for x in grid]
#         rotated_row = len(grid[current_row]) - current_col - 1
#         rotated_col = current_row
#         current_row = rotated_row
#         current_col = rotated_col

# print(f"Total steps taken = {pt1}")

directions = cycle('urdl')

current_direction = next(directions)

points_visited = []
current_row = row_guard
current_col = col_guard
points_visited.append([current_row, current_col])

while (current_row + 1 < len(grid)) and (current_row >= 0)\
      and (current_col + 1 < len(grid[current_row])) and (current_col >= 0):
    # Check if the step is clear
    if current_direction == "u":
        next_row = current_row - 1
        next_col = current_col
    elif current_direction == 'r':
        next_row = current_row 
        next_col = current_col + 1
    elif current_direction == 'd':
        next_row = current_row + 1
        next_col = current_col
    elif current_direction == 'l':
        next_row = current_row
        next_col = current_col - 1

    if grid[next_row][next_col] != "#":
        # Make the step and log it
        current_row = next_row
        current_col = next_col
        point = [current_row, current_col]
        if point not in points_visited:
            points_visited.append(point)

    elif grid[next_row][next_col] == "#":
        current_direction = next(directions)

pt1 = len(points_visited)

print(f"Part 1: {pt1}")

