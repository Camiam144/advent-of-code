#! /usr/bin/env python
import re

# input_text = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

with open('day15.txt', 'r') as f:
    input_text = f.read()

input_steps = input_text.split(",")

def get_hash(chars:str) -> int:
    """ Return the hash of a given string """
    current_value = 0
    for char in chars:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value

# hashes = []
boxes = {i:[] for i in range(256)}

# Lenses will be a tuple ('label', 'power')

for step in input_steps:

    label = re.match("^[a-z]+", step).group(0)
    hash = get_hash(label)
    box = boxes[hash]

    if (step[-1] == "-") and (len(box) > 0):
        box = [x for x in box if x[0] != label]

    if step[-2] == "=":
        lens = (label, int(step[-1]))
        if len(box) == 0:
            box = [lens]
        else:
            for i, x in enumerate(box):
                if x[0] == label:
                    box[i] = lens
                    break
            else:
                box.append(lens)

    boxes[hash] = box

    # hashes.append(get_hash(step))

def calc_focus(all_boxes:dict) -> int:
    total = 0
    for k, v in all_boxes.items():
        first_val = k + 1
        for i, lens in enumerate(v):
            pos = i + 1
            val = lens[1]

            total += first_val * pos * val

    return total

# print(sum(hashes))
# for k, v in boxes.items():
#     if len(v)>0:
#         print(f"Box {k}: {v}")

sum = calc_focus(boxes)
print(sum)