#! /usr/bin/env python
import numpy as np

# input_text = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#"""

with open('day13_input.txt', 'r') as f:
    input_text = f.read()

grids = [x for x in input_text.split("\n\n")]

parsed_grids = []

for grid in grids:
    parsed_grid = np.array([[y for y in x] for x in grid.splitlines()])
    parsed_grids.append(parsed_grid)


def find_horiz_refls(grid: list[list[str]]) -> list[int]:
    """ Return lower idx of all horiz reflections """

    max_rows = grid.shape[0] - 1
    # max_to_check = max_rows//2
    row_mirrors = [0]

    for i in range(max_rows):
        # Check if it's even possible for a mirror
        if (grid[i] == grid[i + 1]).all():
            # Check the shorter side of the grid
            max_range = min(i + 1, max_rows - i)
            for k in range(1, max_range):
                if not (grid[i - k] == grid[i + 1 + k]).all():
                    break
            else:
                if row_mirrors != [0]:
                    row_mirrors.append(i + 1)
                else: row_mirrors = [i + 1]
        else:
            continue
            
    return row_mirrors


all_mirrors = []     
for map in parsed_grids:
    horiz_mirrors = find_horiz_refls(map)
    # all_horiz_mirrors.append(horiz_mirrors)
    vert_mirrors = find_horiz_refls(np.rot90(map, k=-1))
    # all_vert_mirrors.append(vert_mirrors)

    
    all_mirrors.append((horiz_mirrors, vert_mirrors))


def score(mirrors: list[tuple[list[int]]]) -> int:
    total = 0
    for horiz, vert in mirrors:
        horiz_total = sum([100 * h for h in horiz if h])
        vert_total = sum([v for v in vert if v])
        total += horiz_total + vert_total

    return total

ans = score(all_mirrors)

# print(all_mirrors)
print(ans)