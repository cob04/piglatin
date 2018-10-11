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


if __name__ == "__main__":
        unittest.main(warnings="ignore")
