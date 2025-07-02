import unittest
from utils import apply_discount

class TestUtils(unittest.TestCase):
    def test_apply_discount_basic(self):
        self.assertEqual(apply_discount(100, 20), 80.00)
    def test_apply_discount_rounding(self):
        self.assertEqual(apply_discount(99.99, 15), round(99.99*0.85, 2))

if __name__ == '__main__':
    unittest.main()
