from utils import *


def main():
    data = get_data(get_script_name())
    lines = data.splitlines()
    # Basically we can either reconstruct a tree or just kinda wing it
    # I don't want to rebuild a tree so let's wing it :D
    dir_contents = {"/":[]}
    curr_dir = "/"
    for line in lines[1:]:
        content = line.split()
        if content[0] == "$":
            # Parse the command
            if content[1] == "cd" and content[2] == "..":
                curr_dir = curr_dir.rsplit("/", 2)[0] + "/"  #type:ignore
            elif content[1] == "cd":
                curr_dir += content[2] + "/"
            else:
                continue
        else:
            # It's not a command & we have stuff in the directory
            if curr_dir not in dir_contents:
                dir_contents[curr_dir] = []
            try: dir_contents[curr_dir].append(int(content[0]))
            except ValueError: pass
            if content[0] == 'dir':
                dir_contents[curr_dir].append(curr_dir + content[1] + "/")
    
    # print(dir_contents)
    
    limit = 100000
    
    final_dict = {}
    final_sum = 0
    for k, v in dir_contents.items():
        final_dict[k] = accum(k, v, dir_contents)
        if final_dict[k] <= limit:
            final_sum += final_dict[k]
    print("Part 1")
    print(final_sum)
    
    # Part 2, need to free up space:
    total_space = 70000000
    free_space_required = 30000000
    total_used_space:int = final_dict["/"]
    unused_space = total_space - total_used_space
    smallest_valid_dir = free_space_required - unused_space
    current_smallest_dir = final_dict["/"]
    for k, v in final_dict.items():
        
        if v >= smallest_valid_dir and v < current_smallest_dir:
            current_smallest_dir = v
    
    print("Part 2")
    print(current_smallest_dir)
    
    
    
def accum(curr_dir, dir_cont, dir_dict):
    
    # listdir = dir_dict[curr_dir]
    curr_sum = 0
    for item in dir_cont:
        if type(item) == int:
            curr_sum += int(item)
        else:
            curr_sum += accum(item, dir_dict[item], dir_dict)
    # sum_dict[curr_dir] = curr_sum
    # return sum_dict
    return curr_sum


if __name__ == "__main__":
    main()