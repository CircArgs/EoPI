import math


class BinaryTreeNode:
    """
    A node in a tree storing a value and references to parent and children if they exist
    """

    def __init__(
        self, value: int, parent=None, left_child=None, right_child=None,
    ):
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    @property
    def sibling(self):
        if self.parent.left_child == self:
            return self.parent.right_child
        else:
            return self.parent.left_child

    def has_children(self):
        return any(self.children)

    @property
    def children(self):
        return self.left_child, self.right_child

    def __repr__(self):
        return f"BinaryTreeNode({self.value})"


def height_from_list(l: list) -> int:
    # from geometric series formula with base 2
    return math.ceil(math.log2(len(l) + 1))


def tree_from_list(l: list) -> BinaryTreeNode:
    """
    Given a list in breadth-first format for a tree create the tree and return the root

    Args:
        l: the list described

    Returns:
        root node of the tree described
    """
    # we will build the tree from the leaves up

    # given an empty list just return nothing
    if not l:
        return None
    l = l.copy()
    d = 1
    prev = [BinaryTreeNode(l.pop(0))]
    root = prev[0]
    while l:
        n = 0
        level = []
        while (n < 2 ** d) and l:
            temp = prev[n // 2]

            l_or_r = n % 2
            if temp is None:
                n += 2
                level.append(None)
                level.append(None)
                continue
            else:
                n += 1
            val = l.pop(0)
            child = BinaryTreeNode(val, temp) if not val is None else None
            if l_or_r == 0:
                temp.left_child = child
            else:
                temp.right_child = child
            level.append(child)
        d += 1
        prev = level
    return root


def grow_binary_tree(root: BinaryTreeNode, value: int):
    if value > root.value:
        if root.right_child is None:
            root.right_child = BinaryTreeNode(value, root)
        else:
            grow_binary_tree(root.right_child, value)
    else:
        if root.left_child is None:
            root.left_child = BinaryTreeNode(value, root)
        else:
            grow_binary_tree(root.left_child, value)
