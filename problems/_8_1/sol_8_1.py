class Stack_Value:
    def __init__(self, v, max):
        self.v = v
        self.max = max

    def __repr__(self):
        return str(self.v)


class Stack:
    def __init__(self):
        self.values = []
        self.max_val = None

    def __len__(self):
        return len(self.values)

    def push(self, v):
        self.values.append(Stack_Value(v, self.max_val))

        if self.max_val is None or v > self.max_val:
            self.max_val = v

    def pop(self):
        ret = self.values.pop()
        self.max_val = ret.max
        return ret.v

    def max(self):
        return self.max_val

    def __repr__(self):
        return str(self.values)
