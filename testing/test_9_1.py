from typing import List
from .test_utils.read_tsv import read_tsv

import problems._9_1.sol as solution
import problems.utils.binary_tree as bt

sol_dict = {"true": True, "false": False}


class test_schema:
    def __init__(self, test: List[int], sol: str, desc: str = ""):
        self.test = [int(v) if v != "null" else None for v in test]
        self.sol = sol_dict[sol]
        self.desc = desc


def test():
    test_data = read_tsv("9_1.tsv", test_schema)
    for test in test_data:
        tree = bt.tree_from_list(test.test)
        assert solution.sol(tree) == test.sol, f"{test.test}; {test.sol}"
