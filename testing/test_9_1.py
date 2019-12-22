from typing import List
from .test_utils.read_tsv import read_tsv

import problems._9_1.sol as solution
from problems.utils.binary_tree import BinaryTreeNode as BTN, grow_binary_tree

sol_dict = {"true": True, "false": False}


class test_schema:
    def __init__(self, test: List[int], sol: str, desc: str = ""):
        self.test = [int(v) for v in test]
        self.sol = sol_dict[sol]
        self.desc = desc


def test():
    test_data = read_tsv("9_1.tsv", test_schema)
    for test in test_data:
        tree = BTN(test.test[0])
        for value in test.test[1:]:
            grow_binary_tree(tree, value)
        assert solution.sol(tree) == test.sol, test.desc
