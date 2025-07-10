import unittest

from models import Order
from service import calculate_total

class TestCaseExamples(unittest.TestCase):
    def test_addition(self):
        # Parameterized test cases: (a, b, expected_result)
        test_cases = [
            (1, 1, 2),
            (2, 3, 5),
            (-1, 1, 0),
            (100, 200, 300),
            (0, 0, 0)
        ]
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(a + b, expected)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    def test_multiplication(self):
        self.assertEqual(3 * 4, 12)

    def test_division(self):
        self.assertEqual(10 / 2, 5)

    def test_modulo(self):
        self.assertEqual(9 % 4, 1)

    def test_exponent(self):
        """Test exponentiation operation"""
        self.assertEqual(2 ** 3, 8)

    def test_square(self):
        """Test squaring operation"""
        self.assertEqual(5 ** 2, 25)

    def test_power_four_and_multiply_by_12(self):
        """Test raising a number to the 4th power and multiplying by 12"""
        num = 2
        result = (num ** 4) * 12
        self.assertEqual(result, 192)
        num = 3
        result = (num ** 4) * 12
        self.assertEqual(result, 972)

    def test_floor_division(self):
        """Test floor division operation"""
        self.assertEqual(17 // 5, 3)
        self.assertEqual(20 // 6, 3)
        self.assertEqual(15 // 3, 5)

    def test_absolute_value(self):
        """Test absolute value operation"""
        self.assertEqual(abs(-5), 5)
        self.assertEqual(abs(5), 5)
        self.assertEqual(abs(0), 0)
        self.assertEqual(abs(-10.5), 10.5)

    def test_negation(self):
        """Test negation operation"""
        self.assertEqual(-5, -5)
        self.assertEqual(-(-5), 5)
        self.assertEqual(-0, 0)
        self.assertEqual(-10.5, -10.5)
        self.assertEqual(-(-10.5), 10.5)

    def test_max_min_operations(self):
        """Test max and min operations"""
        self.assertEqual(max(1, 2, 3), 3)
        self.assertEqual(min(1, 2, 3), 1)
        self.assertEqual(max(-1, -2, -3), -1)
        self.assertEqual(min(-1, -2, -3), -3)

class TestDiscountCalculation(unittest.TestCase):
    def test_no_discount(self):
        order = Order(price=100.0, discount_percent=0.0)
        self.assertEqual(calculate_total(order), 100.0)

    def test_full_discount(self):
        order = Order(price=100.0, discount_percent=100.0)
        self.assertEqual(calculate_total(order), 0.0)

    def test_typical_discount(self):
        order = Order(price=200.0, discount_percent=25.0)
        self.assertEqual(calculate_total(order), 150.0)

    def test_negative_discount(self):
        order = Order(price=100.0, discount_percent=-10.0)
        # Depending on business logic, this could be 110.0 or raise an error. Here, we check for 110.0
        self.assertEqual(calculate_total(order), 110.0)

    def test_discount_greater_than_100(self):
        order = Order(price=100.0, discount_percent=150.0)
        # Depending on business logic, this could be -50.0 or raise an error. Here, we check for -50.0
        self.assertEqual(calculate_total(order), -50.0)

    def test_zero_price(self):
        order = Order(price=0.0, discount_percent=50.0)
        self.assertEqual(calculate_total(order), 0.0)

    def test_floating_point_discount(self):
        order = Order(price=99.99, discount_percent=12.5)
        self.assertEqual(calculate_total(order), 87.49)

    def test_large_price_and_discount(self):
        order = Order(price=1_000_000.0, discount_percent=50.0)
        self.assertEqual(calculate_total(order), 500_000.0)

if __name__ == '__main__':
    unittest.main()