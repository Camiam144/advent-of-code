from utils import get_data, get_script_name


def main():
    data = get_data(get_script_name())
    
    outlist = []
    
    subsum = 0
    for line in data.splitlines():
        if line.strip():
            subsum += int(line)
        else:
            outlist.append(subsum)
            subsum = 0
    else:
        outlist.append(subsum)
        subsum = 0
            
    print(sum(sorted(outlist)[-3:]))
    
if __name__ == "__main__":
    main()