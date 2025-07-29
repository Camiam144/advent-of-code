from utils import get_data, get_script_name


def main():
    data = get_data(get_script_name())

    register = 1
    initial_cycle = 20
    mod_cycle = 40
    current_strength = 0
    # Try to reformat the commands to be easier to use:
    new_command_list: list[int] = []
    for line in data.splitlines():
        op = line.split()
        if op[0] == "noop":
            new_command_list.append(0)
        elif op[0] == "addx":
            new_command_list.append(0)
            new_command_list.append(int(op[1]))

    output = ["." for _ in range(240)]
    cycle_count = 1
    for idx, command in enumerate(new_command_list):
        if (
            cycle_count >= initial_cycle
            and (cycle_count - initial_cycle) % mod_cycle == 0
        ):
            current_strength += cycle_count * register
        if idx % 40 in (register - 1, register, register + 1):
            output[idx] = "#"
        cycle_count += 1
        register += command
    #
    print(f"Strength = {current_strength}")
    for i in range(0, len(output), 40):
        print("".join(output[i : i + 40]))


if __name__ == "__main__":
    main()
