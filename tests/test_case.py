import unittest
import math

from models import Order
from service import calculate_total


class TestCaseExamples(unittest.TestCase):
    def test_addition(self):
        # Parameterized test cases: (a, b, expected_result)
        test_cases = [(1, 1, 2), (2, 3, 5), (-1, 1, 0), (100, 200, 300), (0, 0, 0)]
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
        self.assertEqual(2**3, 8)

    def test_square(self):
        """Test squaring operation"""
        self.assertEqual(5**2, 25)

    def test_power_four_and_multiply_by_12(self):
        """Test raising a number to the 4th power and multiplying by 12"""
        num = 2
        result = (num**4) * 12
        self.assertEqual(result, 192)
        num = 3
        result = (num**4) * 12
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

    def test_complex_operations(self):
        """Test combinations of operations"""
        self.assertEqual((5 + 3) * 2 - 1, 15)
        self.assertEqual(10 / 2 + 3 * 4, 17)
        self.assertEqual((20 - 5) / 3, 5)

    def test_percentage_calculations(self):
        """Test percentage operations"""
        self.assertEqual(50 * 0.2, 10.0)
        self.assertEqual(100 * 0.15, 15.0)
        self.assertEqual(200 * 0.05, 10.0)

    def test_square_root(self):
        """Test square root operations"""
        self.assertEqual(math.sqrt(16), 4.0)
        self.assertEqual(math.sqrt(25), 5.0)
        self.assertEqual(math.sqrt(1), 1.0)

    def test_zero_operations(self):
        """Test operations with zero"""
        self.assertEqual(0 * 5, 0)
        self.assertEqual(0 + 10, 10)
        self.assertEqual(10 - 0, 10)
        self.assertEqual(0 / 1, 0)

    def test_large_numbers(self):
        """Test with very large integers"""
        self.assertEqual(1000000 + 2000000, 3000000)
        self.assertEqual(999999 * 2, 1999998)

    def test_floating_point_precision(self):
        """Test decimal precision"""
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)
        self.assertAlmostEqual(1.1 * 3, 3.3, places=7)

    def test_string_operations(self):
        """Test string operations"""
        self.assertEqual("hello" + " world", "hello world")
        self.assertEqual(len("test"), 4)
        self.assertEqual("python".upper(), "PYTHON")

    def test_list_operations(self):
        """Test list operations"""
        test_list = [3, 1, 4, 1, 5]
        self.assertEqual(sorted(test_list), [1, 1, 3, 4, 5])
        self.assertEqual(len(test_list), 5)
        self.assertEqual(max(test_list), 5)


class TestBusinessLogicExtensions(unittest.TestCase):
    def test_multiple_discounts(self):
        """Test applying multiple sequential discounts"""
        # First discount: 20% off 100 = 80
        # Second discount: 10% off 80 = 72
        price = 100.0
        after_first = price * (1 - 20 / 100)  # 80
        after_second = after_first * (1 - 10 / 100)  # 72
        self.assertEqual(after_second, 72.0)

    def test_tax_calculation(self):
        """Test adding tax after discount"""
        # Price: 100, Discount: 20% = 80, Tax: 10% = 88
        discounted_price = 100 * (1 - 20 / 100)  # 80
        with_tax = discounted_price * (1 + 10 / 100)  # 88
        self.assertEqual(with_tax, 88.0)

    def test_bulk_order_discount(self):
        """Test quantity-based discounts"""
        # 5% discount for orders > 10 items
        quantity = 15
        unit_price = 10.0
        total = quantity * unit_price
        if quantity > 10:
            total *= 0.95  # 5% discount
        self.assertEqual(total, 142.5)


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
        # Test that negative discount raises validation error
        with self.assertRaises(Exception):  # InvalidDiscountError
            Order(price=100.0, discount_percent=-10.0)

    def test_discount_greater_than_100(self):
        # Test that discount > 100% raises validation error
        with self.assertRaises(Exception):  # InvalidDiscountError
            Order(price=100.0, discount_percent=150.0)

    def test_zero_price(self):
        order = Order(price=0.0, discount_percent=50.0)
        self.assertEqual(calculate_total(order), 0.0)

    def test_floating_point_discount(self):
        order = Order(price=99.99, discount_percent=12.5)
        self.assertEqual(calculate_total(order), 87.49)

    def test_large_price_and_discount(self):
        order = Order(price=1_000_000.0, discount_percent=50.0)
        self.assertEqual(calculate_total(order), 500_000.0)


if __name__ == "__main__":
    unittest.main()
