"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    """Test of Counter class"""

    def setUp(self):
        """ set up for Counter class"""
        self.counter1 = Counter()
        self.counter2 = Counter()

    def test_share_same_count(self):
        """Test for verify that all instances share the same count."""
        self.counter1.increment()
        self.assertEqual(self.counter1, self.counter2)

    def test_counter_is_singleton(self):
        """Test for verify that Counter is a singleton."""
        self.assertIs(self.counter1, self.counter2)

    def test_not_reset_to_zero(self):
        """Test for the count is not reset to 0 when invoke
           count = Counter() after the first time."""
        self.counter1.increment()
        new_counter = Counter()
        self.assertEqual(self.counter1.count, new_counter.count)

