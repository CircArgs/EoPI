def swap(l, a, b):
    temp = l[a]
    l[a] = l[b]
    l[b] = temp


def shift_elements(a, s, e, p):

    if s >= e:
        return
    assert s <= p <= e, "Invalid Pivot"
    assert s < e, f"Invalid start: {s} and end: {e}. Must have Start<=End."
    c = 0
    i = 0
    bp = p
    while i < p:
        if a[i] > a[p]:
            a.insert(e + 1, a[i])
            del a[i]
            p -= 1
            bp -= 1
            c += 1
        elif a[i] == a[p]:
            swap(a, i, p - 1)
            p -= 1
        else:
            i += 1
    left_end = p

    i = -c + e
    p = bp
    while i > p:
        if a[i] < a[p]:
            a.insert(s, a[i])
            del a[i + 1]
            p += 1
        elif a[i] == a[p]:
            swap(a, i, p + 1)
            p += 1
        else:
            i -= 1

    left_end += p - bp
    left_start = s
    right_end = e
    right_start = p

    left_end -= 1
    right_start += 1
    shift_elements(a, left_start, left_end, left_start + (left_end - left_start) // 2)
    shift_elements(
        a, right_start, right_end, right_start + (right_end - right_start) // 2
    )

    return a


def sol(l):
    return shift_elements(l, 0, len(l) - 1, len(l) // 2)


def extra_space_sol(a):
    if not a:
        return []
    p = a[len(a) // 2]
    return (
        extra_space_sol([i for i in a if i < p])
        + [i for i in a if i == p]
        + extra_space_sol([i for i in a if i > p])
    )

