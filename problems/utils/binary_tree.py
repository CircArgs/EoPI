class BinaryTreeNode:
    def __init__(
        self,
        value: object,
        parent: BinaryTreeNode = None,
        left_child: BinaryTreeNode = None,
        right_child: BinaryTreeNode = None,
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
