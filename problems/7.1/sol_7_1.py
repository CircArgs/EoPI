from utils_7_1 import Linked_List


def sol(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
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
