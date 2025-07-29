from utils import *


def main():
    data = get_data(get_script_name())
    data = data.splitlines()
    
    data = [[int(i) for i in line] for line in data]
    
    # total_visible = 0
    total_visible = 2 * len(data) + 2 * len(data[0]) - 4  # don't doublecount corners
    
    # Brute force a double for loop:
    max_scenic = 1
    for i in range(1, len(data)-1):
        for j in range(1, len(data[i])-1):
            curr_tree = data[i][j]
            curr_scenic = 1
            vis_left = True
            vis_right = True
            vis_up = True
            vis_down = True
            scenic_left = 0
            scenic_right = 0
            scenic_up = 0
            scenic_down = 0
            # Scan from start of row to current tree
            for x in range(j-1, -1, -1):
                scenic_left += 1
                if data[i][x] >= curr_tree:
                    vis_left = False
                    break
            # Scan from current tree to end of row
            for x in range(j+1, len(data[i])):
                scenic_right += 1
                if data[i][x] >= curr_tree:
                    vis_right = False
                    break
            # Scan from top down to current tree
            for y in range(i-1, -1, -1):
                scenic_up += 1
                if data[y][j] >= curr_tree:
                    vis_up = False
                    break
            # Scan from current tree to bottom
            for y in range(i+1, len(data)):
                scenic_down += 1
                if data[y][j] >= curr_tree:
                    vis_down = False
                    break
            if vis_down or vis_up or vis_left or vis_right:
                total_visible += 1
            curr_scenic = scenic_left * scenic_right * scenic_up * scenic_down
            if curr_scenic > max_scenic:
                max_scenic = curr_scenic
            
    
    print(f"Part 1: Total visible trees = {total_visible}")
    print(f"Part 2: Maximum scenic tree = {max_scenic}")

if __name__ == "__main__":
    main()
