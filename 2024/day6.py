from itertools import cycle

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


def main():
    input_text = get_data(get_script_name())
    # Find the character (we know there is exactly 1)
    idx = input_text.replace("\n", "").find("^")
    # Break the puzzle into a grid:
    grid = [list(x) for x in input_text.splitlines()]
    # Get character coord:
    row_guard = idx // len(grid[0])
    col_guard = idx % len(grid[0])

    directions = cycle("urdl")

    current_direction = next(directions)

    points_visited = set()
    current_row = row_guard
    current_col = col_guard
    point = (current_row, current_col)
    points_visited.add(point)
    guard_path = {}
    guard_path[point] = [current_direction]

    while (
        (current_row + 1 < len(grid))
        and (current_row >= 0)
        and (current_col + 1 < len(grid[current_row]))
        and (current_col >= 0)
    ):
        # Check if the step is clear
        if current_direction == "u":
            next_row = current_row - 1
            next_col = current_col
        elif current_direction == "d":
            next_row = current_row + 1
            next_col = current_col
        elif current_direction == "r":
            next_row = current_row
            next_col = current_col + 1
        elif current_direction == "l":
            next_row = current_row
            next_col = current_col - 1

        if grid[next_row][next_col] != "#":
            # Step is clear
            current_row = next_row
            current_col = next_col
            point = (current_row, current_col)
            guard_path.setdefault(point, []).append(current_direction)
            if point not in points_visited:
                points_visited.add(point)

        elif grid[next_row][next_col] == "#":
            current_direction = next(directions)

    pt1 = len(points_visited)

    print(f"Part 1: {pt1}")

    # I don't think we can do part 2 unless we've already walked the entire grid
    # I think we re-walk the path, and at every point, check if placing an object
    # in front of the guard would cause a loop (entering an existing point moving
    # in the same direction we were previously moving).


if __name__ == "__main__":
    main()
