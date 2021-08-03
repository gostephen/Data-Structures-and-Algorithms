# Stack implementation using singly linked list


class LinkedStack:

    # Nested Node class for linked list
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def is_empty(self):
        """Checks whether a stack is empty or populated
        Returns True is the stack size is 0 and False otherwise"""
        return self._size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            return "Stack is empty."
        popped = self._head._element
        self._head = self._head._next
        self._size -= 1
        return popped

    def top(self):
        """Returns the element value of the Node at the top of the Stack without removing it"""
        if self.is_empty():
            return "Stack is empty."
        return self._head._element

    def length(self):
        return self._size
