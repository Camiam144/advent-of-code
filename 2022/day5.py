from utils import *
import re
import string


def main():
    data = get_data(get_script_name())
    crates, directions = data.split("\n\n")
    splitcrates = crates.splitlines()
    cratenums = splitcrates[-1]
    stacks = {}
    idx_map = {}
    for idx, char in enumerate(cratenums):
        if char != " ":
            stacks[idx] = []
            idx_map[int(char)] = idx
    
    # Init our stacks:
    for line in splitcrates[-2::-1]:
        for idx, char in enumerate(line):
            if char in string.ascii_uppercase:
                stacks[idx].append(char)
    
    # Comment out part 1 cuz I'm too lazy to write an init_stacks(data) function lol 
    # for line in directions.splitlines():
    #     iters, start_stack_num, end_stack_num = [int(x) for x in re.findall(r'\d+', line)]
    #     start_stack_idx = idx_map[start_stack_num]
    #     end_stack_idx = idx_map[end_stack_num]
    #     for _ in range(iters):
    #         stacks[end_stack_idx].append(stacks[start_stack_idx].pop())

    # # Get the actual answer
    # part_1 = ""
    # for k, v in stacks.items():
    #     part_1 += v.pop()
        
    # print("Part 1")
    # print(part_1)
    
    # Part 2, we can move multiple crates at one time
    # Re init stacks cuz we're lazy
    for line in directions.splitlines():
        iters, start_stack_num, end_stack_num = [int(x) for x in re.findall(r'\d+', line)]
        start_stack_idx = idx_map[start_stack_num]
        end_stack_idx = idx_map[end_stack_num]
        # move multiple crates onto new stack
        crates_to_move = stacks[start_stack_idx][-iters:]
        stacks[end_stack_idx].extend(crates_to_move)
        # Remove crates from original stack
        stacks[start_stack_idx] = stacks[start_stack_idx][:-iters]

    part_2 = ""
    for k, v in stacks.items():
        part_2 += v.pop()
    print("Part 2")
    print(part_2)

if __name__ == "__main__":
    main()