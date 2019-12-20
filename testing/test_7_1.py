from typing import List
from .test_utils.read_tsv import read_tsv

import problems._7_1.sol as solution
from problems._7_1.utils import Linked_List


class test_schema:
    def __init__(self, l1: List[int], l2: List[int], sol: List[int], desc: str = ""):
        self.l1 = Linked_List.from_list(l1)
        self.l2 = Linked_List.from_list(l2)
        self.sol = sol
        self.desc = desc


def test():
    test_data = read_tsv("7_1.tsv", test_schema)
    for test in test_data:
        assert solution.sol(test.l1, test.l2).to_list() == test.sol, test.desc
