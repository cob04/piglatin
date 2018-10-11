# Tests for piglatin module.

import unittest

from piglatin import Stack


class StackTests(unittest.TestCase):

    def test_initialized_stack_has_list(self):
        """Test that an empty list is an attribute of the new initialized
        stack.
        """
        s = Stack()
        self.assertEqual(s._items, [])

    def test_pushing_item_to_stack(self):
        """Test the push method of our stack adds a new item to the list."""
        s = Stack()
        s.push("A")
        self.assertIn("A", s._items)

    def test_peeking_at_the_top_of_the_stack(self):
        """Test the peek method returns the top item on the stack."""
        s = Stack()
        s.push("A")
        s.push("B")
        self.assertEqual(s.peek(), "B")

    def test_popping_an_item_from_the_stack(self):
        """Test the pop method removes the top item from the stack
        and returns it.
        """
        s = Stack()
        s.push("A")
        s.push("B")
        s.push("C")
        self.assertEqual(s.pop(), "C")
        self.assertEqual(s.peek(), "B")



if __name__ == "__main__":
        unittest.main(warnings="ignore")
