from utils import *


def main():
    data = get_data(get_script_name())
    
    lines = data.splitlines()
    num_contained = 0
    num_overlap = 0
    for line in lines:
        range1, range2 = line.split(",")
        # find when one range is fully contained in the other:
        range1_1, range1_2 = int(range1.split("-")[0]), int(range1.split("-")[1])
        range2_1, range2_2 = int(range2.split("-")[0]), int(range2.split("-")[1])
        if (range1_1 <= range2_1 <= range2_2 <= range1_2) or (range2_1 <= range1_1 <= range1_2 <= range2_2):
            num_contained += 1
            num_overlap += 1
        elif (range1_1 <= range2_1 <= range1_2) or (range1_1 <= range2_2 <= range1_2):
            num_overlap += 1
                
    print("Part 1")
    print(num_contained)
    
    # Determine if there is any overlap at all
    print("Part 2")
    print(num_overlap)
        


if __name__ == "__main__":
    main()