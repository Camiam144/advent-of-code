""" The engineer explains that an engine part seems to be missing from the
engine, but nobody can figure out which one. If you can add up all the part
numbers in the engine schematic, it should be easy to work out which part is
missing.

The engine schematic (your puzzle input) consists of a visual representation of
the engine. There are lots of numbers and symbols you don't really understand,
but apparently any number adjacent to a symbol, even diagonally, is a "part
number" and should be included in your sum. (Periods (.) do not count as a
symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..

In this schematic, two numbers are not part numbers because they are not
adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number
is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of
the part numbers in the engine schematic?

----- PART TWO ----
The missing part wasn't the only issue - one of the gears in the engine is
wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its
gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so
that the engineer can figure out which gear needs to be replaced.
"""

def is_valid_num(row_idx:int, col_idx:int, number_end:int, schem_split:list[str]) -> bool:
    """ Check if a number in the schematic is valid.

    A number is valid if it has a symbol in any adjacent square, including
    diagonally.
    """

    def is_symbol(val:str) -> bool:
        if val.isdigit() or (val == '.'):
            return False
        return True

    squares_to_check = [[r, c]
                        for r in range(row_idx - 1, row_idx + 2, 1)
                        for c in range(col_idx - 1, number_end + 1)
                        ]
    
    for square in squares_to_check:
        try:
            if is_symbol(schem_split[square[0]][square[1]]):
                return True
        except IndexError:
            pass
    return False


with open("day3_input.txt", 'r') as f:
    schematic = f.read()

# First we break the schematic into an array
schem_split = str.splitlines(schematic)

# Scan the entire array
answer = 0
for row_idx, row in enumerate(schem_split):
    col_idx = 0
    while col_idx < len(row):
        if row[col_idx].isdigit():
            # Get end of digit
            number_end = col_idx + 1
            while (number_end < len(row)) and row[number_end].isdigit():
                number_end += 1
            number = row[col_idx:number_end]
            # If the number is valid, add it to the total
            if is_valid_num(row_idx, col_idx, number_end, schem_split):
                answer += int(number)
            
            # increment to the end of the digit and move on
            col_idx = number_end

        else: col_idx += 1
        
print(answer)