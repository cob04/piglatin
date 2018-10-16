# piglatin.py
"""Returns an english word coveted into pig latin.
usage:
    python piglatin <english_word>
"""
import sys


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

    def pop(self):
        """Pop the pop item from the stack."""
        return self._items.pop()

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self._items) == 0

    def size(self):
        """Return the size of the stack."""
        return len(self._items)


def pig_latin_converter(word):
    """Convert english words to pig latin."""
    vowels = {"a", "e", "i", "o", "u"}
    stack = Stack()
    consonant_word = ''
    
    for char in word:
        if char not in vowels:
            stack.push(char)
        else:
            break


    if stack.is_empty():
        return word + 'way'
    
    consonant_word = word[stack.size():]

    while not stack.is_empty():
        consonant_word += stack.pop()

    return  consonant_word + 'ay'


def main(word):
    print(pig_latin_converter(word))


if __name__ == "__main__":
    main(sys.argv[1])
