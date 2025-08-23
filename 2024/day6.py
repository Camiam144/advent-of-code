from utils import get_data, get_script_name

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

# input_text = """...........#.....#......
# ...................#....
# ...#.....##.............
# ......................#.
# ..................#.....
# ..#.....................
# ....................#...
# ........................
# .#........^.............
# ..........#..........#..
# ..#.....#..........#....
# ........#.....#..#......"""


def main():
    input_text = get_data(get_script_name())
    # Find the character (we know there is exactly 1)
    idx = input_text.replace("\n", "").find("^")
    # Break the puzzle into a grid:
    grid = [list(x) for x in input_text.splitlines()]
    # Get character coord:
    row_guard = idx // len(grid[0])
    col_guard = idx % len(grid[0])

    directions = {"u": "r", "r": "d", "d": "l", "l": "u"}
    moves = {"u": [-1, 0], "r": [0, 1], "d": [1, 0], "l": [0, -1]}

    current_direction = "u"

    current_row = row_guard
    current_col = col_guard
    points_visited = {}  # Ordered dict for easier debugging
    # points_visited.add((current_row, current_col))

    while True:
        dr, dc = moves[current_direction]
        # print(f"At loc {current_row}, {current_col} pointing {current_direction}")

        next_row = current_row + dr
        next_col = current_col + dc

        if (
            next_row >= len(grid)
            or next_row < 0
            or next_col >= len(grid[current_row])
            or next_col < 0
        ):
            # Our next step leaves the grid, so we're done
            points_visited.setdefault((current_row, current_col), []).append(
                [current_row, current_col]
            )
            break

        if grid[next_row][next_col] != "#":
            # Step is clear
            # Can we check for a loop here?
            points_visited.setdefault((current_row, current_col), []).append(
                [current_row, current_col]
            )
            current_row = next_row
            current_col = next_col

        elif grid[next_row][next_col] == "#":
            current_direction = directions[current_direction]
            # print(f"Next step is blocked, turning {current_direction}")

    pt1 = len(points_visited.keys())

    print(f"Part 1: {pt1}")

    # Brute force part 2 along path?
    pt2 = 0
    # remove starting point as a valid point
    points_visited.pop((row_guard, col_guard), None)
    for block_row, block_col in points_visited:
        prev_symbol = grid[block_row][block_col]
        grid[block_row][block_col] = "#"

        current_direction = "u"
        current_row = row_guard
        current_col = col_guard
        visited = set()

        while True:
            if (current_row, current_col, current_direction) in visited:
                pt2 += 1
                break

            dr, dc = moves[current_direction]
            next_row = current_row + dr
            next_col = current_col + dc

            if (
                next_row >= len(grid)
                or next_row < 0
                or next_col >= len(grid[current_row])
                or next_col < 0
            ):
                break

            if grid[next_row][next_col] != "#":
                # Step is clear
                # Can we check for a loop here?
                visited.add((current_row, current_col, current_direction))
                current_row = next_row
                current_col = next_col

            elif grid[next_row][next_col] == "#":
                current_direction = directions[current_direction]
                # print(f"Next step is blocked, turning {current_direction}")
        grid[block_row][block_col] = prev_symbol

    print(f"Part 2: {pt2}")


if __name__ == "__main__":
    main()
