import unittest

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
        self.assertEqual(max(5), 5)
        self.assertEqual(min(5), 5)

if __name__ == '__main__':
    unittest.main()