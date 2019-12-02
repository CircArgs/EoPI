"""
EoPI pg 39

Implement quicksort s.t. at each partitioning elements equal to the pivot are 
grouped into a central area and teh recurse steps focus only on the left and right elements 
i.e. elements less than and elements grater than the pivot respectively

Example:
sol([3,1,2]) -> [1,2,3]
"""


def swap(l: list, a: int, b: int) -> None:
    """
    Args:
        l: list to swap in
        a: index of first element
        b: index of second element

    Returns:
        None
    simple helper to swap in list l indices a and b
    """
    temp = l[a]
    l[a] = l[b]
    l[b] = temp


def shift_elements(a: list, s: int, e: int, p: int) -> list:
    """
    Quicksort partitioning function. The heart of quicksort. Allows arbitrary pivot.
    Uses Dutch National Flag Style Partitioning:

    partition the array a so that all elements equal to p are contiguous around p
    all elements less than p are left of said contiguous region 
    and all elements greater than p are right of said contiguous region

    Args:
        a: list to partition
        s: index start range of partitioning
        e: index end range of partitioning
        p: index pivot to partition around

    Returns:
        a sorted inplace

    """
    # if the start and end have passed one another we stop
    if s >= e:
        return
    # some sanity checkers
    assert s <= p <= e, "Invalid Pivot"
    assert s < e, f"Invalid start: {s} and end: {e}. Must have Start<=End."
    # c counts how many times we've appended to the right working on the left half
    c = 0
    # i is the current index we're looking at
    i = 0
    # bp will keep track of the pivot moving left as a result of appending
    # when we move begin to move from the right it will give us where the pivot is after we moved from the left
    # after we've been moving it
    bp = p
    # we start on the left
    while i < p:
        # if we the current element is greater value than pivot it needs to be moved to after it (here we move to end of cur range e)
        if a[i] > a[p]:
            a.insert(e + 1, a[i])
            del a[i]
            p -= 1
            bp -= 1
            c += 1
        # equal elements from the left will be juxtaposed with the pivot to the left
        # we'll use this as the new pivot for the time being so continue to juxtapose further equal elements we encounter
        elif a[i] == a[p]:
            swap(a, i, p - 1)
            p -= 1  # note no change to bp as this is not the original pivot
        # if the element is less than the pivot value we dont need to do anything and just move to the next index
        else:

            i += 1
    # just before where the contiguous region starts
    # is the end of the left partition
    left_end = p - 1
    # we could start at e but we already know that the c elements we appended are in the right spot for this partitioning
    i = -c + e
    # remind p to be the original pivot
    p = bp
    # we do the same thing as about except from the right
    while i > p:
        # move elements that are less than the pivot's value to the start of this partitioning s
        if a[i] < a[p]:
            a.insert(s, a[i])
            del a[i + 1]
            p += 1
        # contiguous region extending to the right this time instead of left
        elif a[i] == a[p]:
            swap(a, i, p + 1)
            p += 1
        else:
            i -= 1
    # from above we made the left_end after working from the left
    # it has moved now since working from the right having appended new elements less than pivot value to the left start
    # so we need to move it over by this number that we have appended
    left_end += p - bp
    # the new left start is just the current start
    left_start = s
    # the new right end is just the current end
    right_end = e
    right_start = p + 1

    # recurse left and right
    shift_elements(a, left_start, left_end, left_start + (left_end - left_start) // 2)
    shift_elements(
        a, right_start, right_end, right_start + (right_end - right_start) // 2
    )

    return a


def sol(l: list) -> list:
    """
    inplace quicksort

    Args:
        l: list to sort inplace

    Returns:
        l sorted inplace
    """
    return shift_elements(l, 0, len(l) - 1, len(l) // 2)


def extra_space_sol(a: list) -> list:
    """
    out of place quicksort

    Args:
        a: list to sort out of place
    
    Returns:
        sorted list. a remains the same
    """
    if not a:
        return []
    p = a[len(a) // 2]
    return (
        extra_space_sol([i for i in a if i < p])
        + [i for i in a if i == p]
        + extra_space_sol([i for i in a if i > p])
    )

