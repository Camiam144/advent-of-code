from utils import *
import string

def main():
    data = get_data(get_script_name())
    
    score_dict = {letter: i + 1 for i, letter in enumerate(string.ascii_letters)}
    
    total = 0
    
    for line in data.splitlines():
        bag1, bag2 = line[:len(line)//2], line[len(line)//2:]
        common = set(bag1).intersection(set(bag2))
        for item in common:
            total += score_dict[item]
    print(total)
    
    print("Part 2")
    print("-"*20)
    
    lines = data.splitlines()
    total2 = 0
    for i in range(0, len(lines), 3):
        line1 = set(lines[i])
        line2 = set(lines[i+1])
        line3 = set(lines[i+2])
        common = line1.intersection(line2).intersection(line3)
        total2 += score_dict[common.pop()]
    print(total2)
    
if __name__ == "__main__":
    main()