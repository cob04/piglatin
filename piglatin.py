# piglatin.py

class Stack:
    """A class implementation of the Stack data structure."""
    def __init__(self):
        self._items = []

    def push(self, item):
        """Push an item on top of the stack."""
        self._items.append(item)

    def peek(self):
        """Peek (look) at the top item on the stack."""
        return self._items[len(self._items) - 1]
