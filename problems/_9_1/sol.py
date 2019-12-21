from ..utils.binary_tree import BinaryTreeNode


def height(root: BinaryTreeNode) -> int:
    if root is None:
        return 0

    return 1 + max(height(root.left_child), height(root.right_child))


def sol(root: BinaryTreeNode):
    balanced = True
    if not root.has_children():
        return balanced
