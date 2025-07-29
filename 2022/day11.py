import utils


class Monkey:
    def __init__(self, num: int) -> None:
        self.num = num
        self.items = []
        self.op_string = None
        self.test_val = None
        self.true_target = None
        self.false_target = None
        self.num_inspects = 0
        self.supermodulo = None

    def put_item(self, item: int) -> None:
        self.items.append(item)

    def throw_item(self, item: int, new_item: int, target: "Monkey") -> None:
        self.items.remove(item)
        target.put_item(new_item)

    def get_inspect_val(self, item: int) -> int:
        old = item  # noqa
        new = eval(self.op_string)
        new = new % self.supermodulo if self.supermodulo else new // 3
        # return new // 3
        return new  # Part 2 doesn't divide by 3

    def choose_target(self, item_val: int) -> int:
        if item_val % self.test_val == 0:
            return self.true_target
        else:
            return self.false_target

    def inspect_item(self, item: int, monkey_list: list["Monkey"]) -> None:
        """Do the whole round thingo"""
        # print(f"Monkey {self.num} inspecting item {item}")
        new_val = self.get_inspect_val(item)
        # print(f"Worry value now {new_val}")
        target_idx = self.choose_target(new_val)
        # print(f"Throwing to Monkey {target_idx}")
        self.throw_item(item, new_val, monkey_list[target_idx])
        self.num_inspects += 1


def build_monkey(text_chunk: str) -> Monkey:
    """Build a monkey from a chunk of text"""
    monkey_lines = text_chunk.splitlines()
    monkey_number = int(monkey_lines[0][-2])
    new_monkey = Monkey(monkey_number)
    monkey_items = [
        int(x.strip()) for x in monkey_lines[1].split(":")[-1].strip().split(",")
    ]

    for item in monkey_items:
        new_monkey.put_item(item)

    monkey_op = monkey_lines[2].split(":")[-1].strip().split("=")[-1]
    new_monkey.op_string = monkey_op
    new_monkey.test_val = int(monkey_lines[3].split()[-1].strip())
    new_monkey.true_target = int(monkey_lines[4].split()[-1].strip())
    new_monkey.false_target = int(monkey_lines[5].split()[-1].strip())
    return new_monkey


def calc_monkey_business(monkeys: list["Monkey"]) -> int:
    """Calculate the monkey business level"""
    business = [monkey.num_inspects for monkey in monkeys]
    business.sort(reverse=True)
    return business[0] * business[1]


def main():
    data = utils.get_data(utils.get_script_name())

    chunks = data.split("\n\n")
    monkeys: list["Monkey"] = []
    # For part 2, looked up the solution (A + B) % M = (A % M + B % M) % M
    supermodulo = 1
    for chunk in chunks:
        new_monkey = build_monkey(chunk)
        monkeys.append(new_monkey)
        supermodulo *= new_monkey.test_val

    for monkey in monkeys:
        monkey.supermodulo = supermodulo

    num_rounds = 10000  # part 1 is 20, part 2 is 10k
    for i in range(num_rounds):
        for monkey in monkeys:
            for item in monkey.items.copy():
                monkey.inspect_item(item, monkeys)

    print(f"Total monkey business = {calc_monkey_business(monkeys)}")


if __name__ == "__main__":
    main()
