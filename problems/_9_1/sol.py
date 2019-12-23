"""
EoPI pg 114
A binary tree is said to be height-balanced if for each node in the tree, the difference in the height of
its left and right subtrees is at most one. A perfect binary tree is height-balanced, as is a complete
binary tree. A height-balanced binary tree does not have to be perfect or complete-see Figure 9.2
on the next page for an example.
Write a program that takes as input the root of a binary tree and checks whether the tree is height-balanced.
"""


from ..utils.binary_tree import BinaryTreeNode as BTN


class UnbalancedTree(Exception):
    """
    an exception to be caught when the tree is unbalanced
    """

    pass


def balance_check(root: BTN) -> int:
    """
    the function that does all the work for sol
    recursively check heights of subtrees and report up 
    **unless** the height of the left and right subtrees of some node in the tree differ by more than 1
    """
    # if the current parent is None then we are at a leaf so no depth added -0
    if root is None:
        return 0
    # get the left and right heights
    lh = balance_check(root.left_child)
    rh = balance_check(root.right_child)
    # if the heights differ by more than 1 (2+) then we have an unbalanced tree. We throw an error to save collapsing the stack from the recursion
    if abs(lh - rh) > 1:
        raise UnbalancedTree
    # if the subtrees are balanced we can report up the current height necessary to check larger subtrees earlier in the recursion stack
    return 1 + max(lh, rh)


def sol(root: BTN):
    # since we throw an error if a subtree is unbalanced we need to catch it to report an unbalanced tree back as the solution
    try:
        # we do the check and either an error will be thrown and we will check if it is unbalanced tree
        # or we will get the height of the tree but we dont care so just say we didnt get an error so the tree is balanced - True
        balance_check(root)
        return True
    except UnbalancedTree:
        # if unbalanced tree error is thrown we know the tree is unbalanced - False
        return False
