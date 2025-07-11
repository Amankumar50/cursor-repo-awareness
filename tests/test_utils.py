import unittest
from utils import apply_discount


class TestUtils(unittest.TestCase):
    def test_apply_discount_basic(self):
        self.assertEqual(apply_discount(100, 20), 80.00)

    def test_apply_discount_rounding(self):
        self.assertEqual(apply_discount(99.99, 15), round(99.99 * 0.85, 2))

    def test_calculate_median_odd(self):
        from utils import calculate_median
        self.assertEqual(calculate_median([1, 3, 5]), 3.0)
        self.assertEqual(calculate_median([1, 2, 3, 4, 5]), 3.0)

    def test_calculate_median_even(self):
        from utils import calculate_median
        self.assertEqual(calculate_median([1, 2, 3, 4]), 2.5)
        self.assertEqual(calculate_median([10, 20]), 15.0)


if __name__ == "__main__":
    unittest.main()
