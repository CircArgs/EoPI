"""
an implementation of binary trees for use in EoPI problems

includes several utilities
"""

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


# def height_from_list(l: list) -> int:
#     """
#     given a list of elements describing ALL breadth first elements of a tree, return the depth of the tree

#     Args:
#         l: list of elements

#     Returns:
#         height of tree made of l
#     """
#     # from geometric series formula with base 2
#     return math.ceil(math.log2(len(l) + 1))


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
    # we will be popping and dont want to destroy original list
    l = l.copy()
    # d is the current depth we're working on. 1 is root's children
    d = 1
    # prev will represent the nodes at the current depth. start with root
    prev = [BinaryTreeNode(l.pop(0))]
    # store the root to return
    root = prev[0]
    # we will be popping values off of the list. when it is empty we have nothing more to add to the tree
    while l:
        # n is the current node of the depth we are working on
        n = 0
        # level will store the children we add at this depth and will become the next prev
        level = []
        # we are done with the current depth if either we have added a whole level (2**d nodes) or we have no more values in l to add
        while (n < 2 ** d) and l:
            # temp stores the current parent
            temp = prev[n // 2]
            # check if we will be adding the next element as left or right child 0-left 1-right
            l_or_r = n % 2
            # if the temp parent is None then it cannot take children so we say the current level has two blanks in this node's children spot
            # and increment the counter passed this parent's 2 children
            if temp is None:
                n += 2
                level.append(None)
                level.append(None)
                continue
            else:
                # otherwise we will add this child and move to the next
                n += 1
            # get the value to add
            val = l.pop(0)
            # create a node if the value isnt None
            child = BinaryTreeNode(val, temp) if not val is None else None
            # add as the appropriate child
            if l_or_r == 0:
                temp.left_child = child
            else:
                temp.right_child = child
            # add it to the level
            level.append(child)
        # once the level is done we increment our depth and set the level to be the previous as we move on to the next level
        d += 1
        prev = level
    # return the root
    return root


# TODO: for future use in heaps
# def grow_binary_tree(root: BinaryTreeNode, value: int):
#     """
#     grow a binary heap given a root and a value

#     Args:
#         root to add to. can be any binary tree node in a tree i.e. root of a subtree

#     Returns:
#         None- operates inplace
#     """
#     if value > root.value:
#         if root.right_child is None:
#             root.right_child = BinaryTreeNode(value, root)
#         else:
#             grow_binary_tree(root.right_child, value)
#     else:
#         if root.left_child is None:
#             root.left_child = BinaryTreeNode(value, root)
#         else:
#             grow_binary_tree(root.left_child, value)
