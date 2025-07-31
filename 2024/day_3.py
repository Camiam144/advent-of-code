""" It seems like the goal of the program is just to multiply some numbers. It
does that with instructions like mul(X,Y), where X and Y are each 1-3 digit
numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024.
Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many
invalid characters that should be ignored, even if they look like part of a mul
instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

Only the four highlighted sections are real mul instructions. Adding up the
result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).
"""
import re

with open("2024\inputs\day_3.txt", 'r') as f:
        input = f.read()

# input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
input = input.replace("\n", "")

first_re = re.findall(r"mul\((\d+),(\d+)\)", input)

pt_1 = 0
for a, b in first_re:
    pt_1 += int(a) * int(b)

print(f"Part 1 answer: {pt_1}")

""" There are two new instructions you'll need to handle:

    The do() instruction enables future mul instructions.
    The don't() instruction disables future mul instructions.

Only the most recent do() or don't() instruction applies. At the beginning of
the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

This corrupted memory is similar to the example from before, but this time the
mul(5,5) and mul(11,8) instructions are disabled because there is a don't()
instruction before them. The other mul instructions function normally,
including the one at the end that gets re-enabled by a do() instruction.
"""

# positive match: (?<=do\(\)).+?(?=don't\(\))
# start of string to first don't(): ^.*?don't\(\)

# Grab first part of string:
first_part = re.search(r"^.*?don't\(\)", input)
rest_regex = r"(?<=do\(\)).+?(?=don't\(\))"
rest_of_parts = re.findall(rest_regex, input)

fixed_string = first_part.group(0) + "".join(rest_of_parts)

pt_2 = 0
matches = re.findall(r"mul\((\d+),(\d+)\)", fixed_string)
for a, b in matches:
    pt_2 += int(a) * int(b)


print(f"Part 2 answer: {pt_2}")