# Tests for piglatin module.

import unittest

from piglatin import Stack


class StackTests(unitetest.TestCase):

    def setUp(self):
        self.stack = Stack()
