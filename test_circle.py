"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""

import unittest
from circle import Circle


class TestCircle(unittest.TestCase):
    """ Tests of Circle class"""

    def test_circle_constructor(self):
        with self.assertRaises(ValueError):
            Circle(-1)
