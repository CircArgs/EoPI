from random import shuffle
from typing import List
from .test_utils.read_tsv import read_tsv

import problems._9_1.sol as solution
import problems.utils.binary_tree as bt

sol_dict = {"true": True, "false": False}


class test_schema:
    def __init__(self, test: List[int], sol: str, desc: str = ""):
        self.test = bt.tree_from_list(test)
        self.sol = sol_dict[sol]
        self.desc = desc


def test():
    test_data = read_tsv("9_1.tsv", test_schema)
    for test_number, test in enumerate(test_data):
        assert (
            solution.sol(test.test) == test.sol
        ), f"test_number: {test_number}: {test.test}; {test.sol}"
