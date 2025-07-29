from utils import *


def main():
    data = get_data(get_script_name())
    # Find index of first four non repeated characters
    # Check if str[i] is in set(str[i-3:i-1])
    for leader in range(13, len(data) - 1):
        chars = set(data[leader-14:leader])
        if len(chars) == 14:
            break
        
    print("Part 1")
    print(leader)


if __name__ == "__main__":
    main()