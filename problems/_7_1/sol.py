"""Consider two singly linked lists in which each node holds a number. Assume the lists are sorted,
i.e., numbers in the lists appear in ascending order within each list. The merge of the two lists is a
list consisting of the nodes of the two lists in which numbers appear in ascending order.

Write a program that takes two lists, assumed to be sorted, and returns their merge.
"""


from ..utils.linked_list import Linked_List


def sol(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    # using two destructive iterators to iterate through both lists and add the elements in the proper order to a new list.
    # being destructive preserves constant space
    l1_iter = l1.deathiter()
    l2_iter = l2.deathiter()
    ret = Linked_List()
    t1 = next(l1_iter)
    t2 = next(l2_iter)
    while True:
        try:
            if t1.val <= t2.val:
                ret.push(t1)
                t1 = next(l1_iter)

            else:
                ret.push(t2)
                t2 = next(l2_iter)

        except StopIteration:
            break

    if t1 != ret.tail:
        ret.push(t1)
    else:
        ret.push(t2)
    if l1:
        ret.push_list(l1)
    if l2:
        ret.push_list(l2)

    return ret


# def sol(*args):
#     if len(args) == 1:
#         return args[0]
#     args = list(args)
#     ret = sol_for_two(args.pop(), args.pop())
#     while args:
#         ret = sol_for_two(ret, args.pop())

#     return ret
