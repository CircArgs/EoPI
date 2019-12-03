from utils_7_1 import Linked_List


def sol(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    l1_iter = l1.iter()
    l2_iter = l2.iter()
    i1 = 0
    i2 = 0
    ret = Linked_List()
    t1 = next(l1_iter)
    t2 = next(l2_iter)
    while True:
        try:
            if t1.val <= t2.val:
                ret.push(t1)
                i1 += 1
                t1 = next(l1_iter)

            else:
                ret.push(t2)
                i2 += 1
                t2 = next(l2_iter)

        except StopIteration:
            break

    if i1 < len(l1):
        for n in l1_iter:
            ret.push(n)
    if i2 < len(l2):
        for n in l2_iter:
            ret.push(n)

    return ret
