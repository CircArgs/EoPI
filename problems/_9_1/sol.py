from ..utils.binary_tree import BinaryTreeNode as BTN


class UnbalancedTree(Exception):
    pass


def balance_check(root: BTN) -> int:
    if root is None:
        return 0
    lh = balance_check(root.left_child)
    rh = balance_check(root.right_child)
    if abs(lh - rh) > 1:
        raise UnbalancedTree

    return 1 + max(lh, rh)


def sol(root: BTN):
    try:
        balance_check(root)
        return True
    except UnbalancedTree:
        return False
