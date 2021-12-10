from copy import deepcopy


class Stack:
    def __init__(self, *args):
        if len(args) == 0:
            self._elements = []
        elif len(args) == 1:
            stack = args[0]
            if isinstance(stack, Stack):
                self._elements = deepcopy(stack.elements)
            else:
                raise ValueError(
                    'The single argument of Stack.__init__ should be Stack only')
        else:
            raise ValueError(
                'Stack.__init__ should have have 0 arguments or 1 arguments (only as a Stack)')

    def pop(self):
        return self.elements.pop()

    def push(self, item):
        self.elements.append(item)

    def top(self):
        return self.elements[-1]

    def clear(self):
        self.clear()

    def __len__(self):
        return len(self.elements)

    def __repr__(self):
        return str(self.elements)

    @property
    def elements(self):
        return self._elements
