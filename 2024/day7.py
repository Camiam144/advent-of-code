from itertools import product
from operator import add, mul

from utils import get_data, get_script_name

# input_text = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""


def main():
    input_text = get_data(get_script_name())
    data = input_text.splitlines()
    data_list = []
    for line in data:
        target, nums = line.split(":")
        nums = nums.split()
        data_list.append((int(target), tuple(int(x) for x in nums)))

    def apply_ops(op_list, num_list):
        subtotal = num_list[0]
        for op, num in zip(op_list, num_list[1:], strict=True):
            subtotal = op(subtotal, num)

        return subtotal

    # Operator for part 2, concats the left and right ops as strings
    def concat_op(left, right):
        return int(str(left) + str(right))

    pt1 = 0
    # Pt1 only uses mul and add
    ops = (mul, add, concat_op)

    for target, subs in data_list:
        all_ops = product(ops, repeat=(len(subs) - 1))
        for oplist in all_ops:
            total = apply_ops(oplist, subs)
            if total == target:
                pt1 += target
                break

    print(f"Points: {pt1}")


if __name__ == "__main__":
    main()
