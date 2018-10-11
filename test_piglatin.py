# Tests for piglatin module.

import unittest

from piglatin import Stack


class StackTests(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
    
    def test_initialized_stack_has_list(self):
        """Test that an empty list is an attribute of the new initialized
        stack.
        """
        self.assertEqual(self.stack._items, [])

    def test_pushing_item_to_stack(self):
        """Test the push method of our stack adds a new item to the list."""
        self.stack.push("A")
        self.assertIn("A", self.stack._items)

    def test_peeking_at_the_top_of_the_stack(self):
        """Test the peek method returns the top item on the stack."""
        self.stack.push("B")
        self.assertEqual(self.stack.peek(), "B")

    def test_popping_an_item_from_the_stack(self):
        """Test the pop method removes the top item from the stack
        and returns it.
        """
        self.assertEqual(self.stack.pop(), "B")
        self.assertEqual(self.stack.peek(), "A")



if __name__ == "__main__":
        unittest.main(warnings="ignore")
