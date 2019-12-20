from .test_utils.read_tsv import read_tsv

import problems._8_1.sol as solution


class test_schema:
    def __init__(self, *args):
        ops = args[0]
        self.stack = solution.Stack()
        self.ops = ops[1:-1]
        self.desc = args[-1]


def test():
    test_data = read_tsv("8_1.tsv", test_schema)
    for test in test_data:
        if not test:
            continue
        for op_name, op_val in test.ops:
            if op_name == "push":
                test.stack.push(op_val)
            elif op_name == "pop":
                assert test.stack.pop() == op_val, test.desc
            elif op_name == "empty":
                assert bool(op_val) == test.stack.empty
            elif op_name == "max":
                assert test.stack.max() == op_val

            else:
                raise ValueError(f'Unknown op: "{op_name}" with value {op_val}')
