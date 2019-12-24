"""
EoPI pg 134

Write a program that takes as input a set of sorted sequences and computes the union of these
sequences as a sorted sequence. For example, if the input is <3,5,7>, (0,5), and <0,6,28>, then the
output is (0, 0, 3, 5, 6, 6,7, 28)
"""
import copy
import heapq


def sol(*args):
    heaps = copy.deepcopy(list(args))
    for h in heaps:
        heapq.heapify(h)
    ret = []
    heapq.heapify(ret)

    while heaps:
        delete = []
        for i in range(len(heaps)):
            if heaps[i]:
                heapq.heappush(ret, heapq.heappop(heaps[i]))
            else:
                delete.append(i)
        for d in delete[::-1]:
            del heaps[d]

    return ret
