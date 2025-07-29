import string

import utils


def bfs(
    grid: list[list[str]],
    start: tuple[int, int],
    target: int,
) -> list[tuple[int, int]]:
    """Does a BFS of the grid from start to end and return the path length"""
    queue = []
    visited = set()
    # The queue needs to hold (node, path_to_node) to return shortest path
    queue.append((start, []))
    visited.add(start)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        curr_node, curr_path = queue.pop(0)
        curr_val = grid[curr_node[0]][curr_node[1]]
        curr_path.append(curr_node)
        visited.add(curr_node)

        if curr_val == target:
            return curr_path

        for dr, dc in directions:
            nr = curr_node[0] + dr
            nc = curr_node[1] + dc

            if (
                (0 <= nr < len(grid))
                and (0 <= nc < len(grid[0]))
                and ((nr, nc) not in visited)
                and (grid[nr][nc] <= curr_val + 1)
            ):
                # curr_path.append((nr, nc))
                queue.append(((nr, nc), curr_path[:]))
                visited.add((nr, nc))

    return []


def main():
    data = utils.get_data(utils.get_script_name())

    # I think this question is a BFS graph traversal? We can only go up one step,
    # but can go down as many steps as we want. Goal is to find the shortest path from S to E
    # We need to build the graph, assign values, and then write our algorithim to traverse it.

    vals = {letter: i for i, letter in enumerate(string.ascii_lowercase)}
    vals["S"] = -1
    vals["E"] = 26

    start_coord = None
    end_coord = None

    grid = [[vals[char] for char in line] for line in data.splitlines()]
    for row, line in enumerate(grid):
        for col, val in enumerate(line):
            if val == -1:
                start_coord = (row, col)
            if val == 26:
                end_coord = (row, col)

    # Here we do our bfs?
    final_path = bfs(grid, start_coord, vals["E"])
    print(f"Length of final path = {len(final_path) - 1}")

    p2_scores = {letter: i for i, letter in enumerate(reversed(string.ascii_lowercase))}
    p2_scores["E"] = p2_scores["z"]
    p2_scores["S"] = p2_scores["a"]
    p2_grid = [[p2_scores[char] for char in line] for line in data.splitlines()]
    p2_path = bfs(p2_grid, end_coord, p2_scores["a"])
    print(f"Length of shortest path p2 = {len(p2_path) - 1}")


if __name__ == "__main__":
    main()
