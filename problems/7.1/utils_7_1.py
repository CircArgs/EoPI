class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "Node(" + str(self.val) + ")"


def iter_linked_list(l):
    curr = l.head
    for i in range(l.length):
        yield curr
        curr = curr.next


class Linked_List:
    def __init__(self, head=None):
        self.length = 1
        self.head = head
        self.tail = head

    def __len__(self):
        return self.length

    def __bool__(self):
        return bool(self.length)

    def push_list(self, l):
        if not isinstance(l, Linked_List):
            raise TypeError(f"Can only push lists using this method not type {type(l)}")
        self.tail.next = l.head
        self.tail = l.tail
        self.length += l.length

    def push(self, node):
        if not isinstance(node, Node):
            raise TypeError(
                f"Can only push Nodes onto the linked list not {type(node)}"
            )
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1

    def pop(self):
        curr = self.head
        for i in range(self.length - 1):
            curr = curr.next
        self.tail = curr
        ret = curr.next
        curr.next = None
        length -= 1
        return ret.value

    def __repr__(self):
        return (
            "Linked_List("
            + ", ".join(list(map(lambda x: str(x.val), iter_linked_list(self))))
            + ")"
        )

    @classmethod
    def from_list(cls, l):
        ret = cls(Node(l[0]))
        for i in range(1, len(l)):
            ret.push(Node(l[i]))
        return ret

    @staticmethod
    def Node(*args):
        return Node(*args)

    def iter(self):
        return iter_linked_list(self)
