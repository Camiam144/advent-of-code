#! /usr/bin/env python

# import numpy as np
import time

# input_text = """O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#...."""

with open("day14.txt", 'r') as f:
    input_text = f.read()

grid = [[y for y in x] for x in input_text.splitlines()]

def roll_grid(grid: list[list[str]]) -> list[list[str]]:
    """ Roll the grid all the way north """
    max_row = len(grid)
    max_col = len(grid[0])

    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            # If the space is full, go to the next space
            if (col != "."):
                continue
            # If the space is empty, scan to the next rock:
            i = 1
            while (r + i < max_row):
                current_char = grid[r+i][c]
                if current_char == ".":
                    i += 1
                    continue
                if current_char == "#": break
                if current_char == "O":
                    # Pull it down to the current spot
                    grid[r][c] = "O"
                    # Empty the old spot
                    grid[r+i][c] = '.'
                    break
    return grid


def score(grid: list[list[str]]) -> int:
    """ Score the grid """

    total = 0
    for i, row in enumerate(grid[::-1]):
        for col in row:
            if col == "O":
                total += i+1
    return total


# Part two: roll rocks north, then west, then south, then east. That is 1 cycle.
# Run one billion cycles.

# Clever bit I picked up (read: stole): like a few days ago, this is probably
# going to be cyclical. Store *every* grid we see, and when we get a repeat, skip
# that many cycles until we have to manually simulate the remaining cycles.

cycles = 1000000000
current_cycle = 0
all_grids = {}
start = time.time()

while current_cycle < cycles:

    for j in range(4):
        # Roll W,S,E
        grid = roll_grid(grid)
        grid = [list(row) for row in zip(*reversed(grid))]

    current_cycle += 1

    grid_tuples = tuple(tuple(row) for row in grid)
    if grid_tuples in all_grids:
        length_cycle = current_cycle - all_grids[grid_tuples]
        num_to_skip = (cycles - current_cycle) // length_cycle
        current_cycle += length_cycle * num_to_skip

    all_grids[grid_tuples] = current_cycle
  
    
part_1 = score(grid)
end=time.time()

# for row in grid:
#     print(row)
# print("#"*20)

print(part_1)
print(f"Finished in {end-start:.2f} seconds wall time")
seconds_per_cycle = (end-start)/cycles
time_for_all = 1000000000 * seconds_per_cycle
seconds_for_all = time_for_all % 60
minutes_for_all = time_for_all // 60
hours_for_all = minutes_for_all // 60

print(f"Billion cycles in {minutes_for_all} min {seconds_for_all} sec")
