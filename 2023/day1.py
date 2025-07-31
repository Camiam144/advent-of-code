#!/usr/bin/env python
"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take
a look. The Elves have even given you a map; on it, they've used stars to mark
the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you 
need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day
in the Advent calendar; the second puzzle is unlocked when you complete the
first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough")
and where they're even sending you ("the sky") and why your map looks mostly
blank ("you sure ask a lot of questions") and hang on did you just say the sky
("of course, where do you think snow comes from") when you realize that the
Elves are already loading you into a trebuchet ("please hold still, we need to
strap you in").

As they're making the final adjustments, they discover that their calibration
document (your puzzle input) has been amended by a very young Elf who was
apparently just excited to show off her art skills. Consequently, the Elves are
having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line
originally contained a specific calibration value that the Elves now need to
recover. On each line, the calibration value can be found by combining the first
digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and
77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the
calibration values?

--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are
actually spelled out with letters: one, two, three, four, five, six, seven,
eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last
digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
Adding these together produces 281.

N.B. line two "eightwothree" should parse as 823 -> 83. This is not mentioned
*anywhere* in the notes, keep this in mind for future puzzles.

"""
import re

def get_cal_vals(input:str) -> int:
    """Get the cal vals from an input string"""
    # digits = [s for s in input if s.isdigit()]
    digits = []

    replace_dict = {
        "zero" : "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }

    #Loop through each word and log the indices for each match
    for word, value in replace_dict.items():
        for m in re.finditer(word, input):
            digits.append((value, m.start()))
    # Also find just numbers
    for m in re.finditer("\d", input):
        digits.append((m.group(0), m.start()))

    # Sort the values
    digits = sorted(digits, key=lambda x:int(x[1]))

    if len(digits) > 1:
        cal = int(digits[0][0] + digits[-1][0])
    elif len(digits) == 1:
        cal = int(digits[0][0] + digits[0][0])
    else:
        raise ValueError("No integers found")
    return cal


def get_total_cal(input:list[str]) -> int:
    """Get the total cal val from a list of input strings"""
    total = 0
    for line in input:
        cal = get_cal_vals(line)
        total += cal

    return total


if __name__ == "__main__":

    with open("day1_input.txt", 'r') as f:
        text = f.read()
    input = text.splitlines()
    total = get_total_cal(input)
    print(total)
