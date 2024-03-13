"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""

import unittest
from circle import Circle


class TestCircle(unittest.TestCase):
    """ Tests of the Circle class"""

    def setUp(self):
        """ set up for circle radius"""
        self.circle1 = Circle(3)
        self.circle2 = Circle(4)
        self.circle3 = Circle(0)

    def test_positive_add_area(self):
        """Test add_area with two circles having positive radius."""
        combined_circle = self.circle1.add_area(self.circle2)
        self.assertEqual(combined_circle.get_radius(), 5.0)
        self.assertAlmostEqual(combined_circle.get_area(), 78.53981633974483)

    def test_zero_radius(self):
        """ Test add_area where one circle has radius 0."""
        combined_circle = self.circle3.add_area(self.circle2)
        self.assertEqual(combined_circle.get_radius(), 4.0)
        self.assertAlmostEqual(combined_circle.get_area(), 50.26548245743669)

    def test_circle_constructor(self):
        """ Test for circle constructor"""
        with self.assertRaises(ValueError):
            Circle(-1)
