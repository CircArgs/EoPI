def swap(l, a, b):
    temp=l[a]
    l[a]=l[b]
    l[b]=temp

def shift_elements(a, s, e, p):
    assert s<=p<=e, "Invalid Pivot"
    if s==e:
        return a
    assert s<e, f"Invalid start: {s} and end: {e}"
    for i in range(s, e):


