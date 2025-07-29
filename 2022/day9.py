from utils import *

# class Board():
#     def __init__(self, width_init:int, height_init:int) -> None:
#         self.width_init = width_init
#         self.height_init = height_init

#         self.board = [["." for _ in range(self.width_init)] for _ in range(height_init)]
#         self.board[0][0] = "s"

#     def print_board(self) -> None:
#         for line in self.board[::-1]:
#             print(line)
#         print("\n")

#     def draw_symbol(self, symbol:str, coord:tuple[int, int]) -> None:
#         """ Draw a symbol at the specified place """
#         x, y = coord
#         self.board[y][x] = symbol


# class Knot():
#     def __init__(self, x:int, y:int) -> None:
#         self.x = 0
#         self.y = 0
#     def move(self, direction:str) -> None:
#         if direction == "U":
#             self.y += 1
#         elif direction == "D":
#             self.y -= 1
#         elif direction == "R":
#             self.x += 1
#         elif direction == "L":
#             self.x -= 1
#         else:
#             raise ValueError(f"{direction} was an incompatible direction.")
#     def calc_distance(self, other: 'Knot') -> tuple[int, int]:
#         x_diff = abs(self.x - other.x)
#         y_diff = abs(self.y - other.y)
#         return (x_diff, y_diff)

#     def get_position(self) -> tuple[int, int]:
#         return (self.x, self.y)


def sign(x: int) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def main():
    data = get_data(get_script_name())
    directions: list[tuple[str, int]] = []
    for line in data.splitlines():
        if line:
            direc, steps = line.split()
            directions.append((direc, int(steps)))

    # initialize the head and tail on (0,0)
    rope: list[list[int]] = [[0, 0] for _ in range(10)]
    dirs = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}
    tail_visited: set[list[int]] = set()  # hash set of visited coords

    # Loop through directions
    for dir, steps in directions:
        for __ in range(steps):
            # Move the head:
            move_x, move_y = dirs[dir]
            rope[0][0] += move_x
            rope[0][1] += move_y

            for i in range(1, len(rope)):
                fx, fy = rope[i - 1]
                bx, by = rope[i]
                dx = fx - bx
                dy = fy - by
                # print(f"dx = {dx} dy = {dy}")
                if (dx == 0) or (dy == 0):
                    if abs(dy) >= 2:
                        rope[i][1] += sign(dy)
                    if abs(dx) >= 2:
                        rope[i][0] += sign(dx)
                elif (abs(dx), abs(dy)) != (1, 1):
                    rope[i][0] += sign(dx)
                    rope[i][1] += sign(dy)

            # print(f"Tail at: {tail.get_position()}")
            # board.print_board()
            # print(rope)
            tail_visited.add(tuple(rope[-1]))

    print(f"num visited = {len(tail_visited)}")


if __name__ == "__main__":
    main()
