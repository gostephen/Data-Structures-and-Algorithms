# LIFO Stack implementation using array


class ArrayStack:

    def __init__(self):
        self._stack = []

    def is_empty(self):
        return len(self._stack) == 0

    def length(self):
        return len(self._stack)

    def push(self, e):
        self._stack.append(e)

    def pop(self):
        # removes the last item from the array
        if self.is_empty():
            return "Stack is empty."
        self._stack.pop()

    def top(self):
        if is_empty():
            return "Stack is empty."
        return self._stack[-1]