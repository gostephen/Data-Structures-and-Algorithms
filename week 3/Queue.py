class Queue:
    """FIFO Queue with fixed storage implementation using Python List"""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._size = 0
        self._data = [None] * Queue.DEFAULT_CAPACITY
        self._front = 0

    def __len__(self):
        return self._size

    def front(self):
        if is_empty():
            return "The Queue is empty"
        return self._data[self._front]

    def enqueue(self, val):
        if self._size < len(self._data):
            avail = (self._front + self._size) % len(self._data)
            self._data[avail] = val
            self._size += 1
        else:
            return "The Queue is full"

    def dequeue(self):
        if is_empty():
            return "The Queue is empty"
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return ans

    def is_empty(self):
        return self._size == 0