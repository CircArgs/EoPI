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
    # a simple calculation tells us how deep the tree will be
    height = height_from_list(l)
    # we pad the given list to the number of nodes that would be in a perfect tree
    l += [None] * (2 ** height - 1 - len(l))
    # starting at the leaves i.e. layer height
    i = height
    curr = None
    # we will go until we reach the root
    while i > 0:
        # get the values of the current layer
        layer = l[2 ** (i - 1) - 1 : 2 ** i - 1]
        # make them tree nodes
        layer = [BinaryTreeNode(v) if not v is None else None for v in layer]
        if not curr:
            # if we are at the greatest depth i.e. the leaves we have nothing to hookup
            # so we set current layer to leave and continue looping
            curr = layer
        else:
            # a incrementor will keep track of which child we're connecting
            l_or_r = 0
            for n, node in enumerate(curr):
                # get the parent node
                temp = layer[n // 2]
                if not node is None:
                    # if the node we're looking to hook up were null we wouldnt want to do anything
                    node.parent = temp
                if temp is None:
                    # if the current parent we're looking to hook up to is None then there cant be any children
                    pass
                elif l_or_r % 2 == 0:
                    temp.left_child = node
                else:
                    temp.right_child = node
                l_or_r += 1
            curr = layer
        i -= 1
    return curr[0]


# BTN = BinaryTreeNode


# def tfl(l):
#     height = height_from_list(l)
#     root = BTN(l[0])
#     l = l[1:]
#     depth = 0
#     while l:
#         for i in range(2 ** depth):
#             if not l:
#                 break
#             v = l[0]
#             l = l[1:]


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
