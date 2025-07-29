from utils import *

# A = rock
# B = paper
# C = scissors
#
# X = rock (1 pt)
# Y = paper (2 pt)
# Z = scissors (3 pt)

score_dict = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

win_dict = {
    "A" : "Y",
    "B" : "Z",
    "C" : "X"
}

tie_dict = {
    "A" : "X",
    "B" : "Y",
    "C" : "Z"
}

lose_dict = {
    "A" : "Z",
    "B" : "X",
    "C" : "Y"
}

# Instead of these dicts, could just do a grid with opp on one axis and player on the other axis
# 0 pts for loss, 3 pts for tie, 6 pts for win
# 1 pt for X, 2 pt for y, 3 pts for z
#       Player
#       X Y Z
# O  A  4 8 3
# P  B  1 5 9
# P  C  7 2 6
#
# Then pull this out of a grid: [[4, 8, 3],[1, 5, 9],[7,2,6]] with 1st index being opp and 2nd index being player

def part_1():
    data = get_data(get_script_name())
    
    total_score = 0
    for line in data.splitlines():
        opp, player = line.split()
        if win_dict[opp] == player:
            total_score += 6
        elif tie_dict[opp] == player:
            total_score += 3
        total_score += score_dict.get(player, 0)
        
    print(total_score)
    
# Pt 2
# Instead of this we could just make a new grid like in part 1 except with the new scores.
result_dict = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

def main():
    data = get_data(get_script_name())
    
    total_score = 0
    for line in data.splitlines():
        opp, player = line.split()
        total_score += result_dict[player]
        if player == "X":
            total_score += score_dict[lose_dict[opp]]
        elif player == "Y":
            total_score += score_dict[tie_dict[opp]]
        else:
            total_score += score_dict[win_dict[opp]]
        
    print(total_score)


if __name__ == "__main__":
    main()