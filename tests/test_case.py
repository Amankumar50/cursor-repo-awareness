import unittest

class TestCaseExamples(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(1 + 1, 2)

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

if __name__ == '__main__':
    unittest.main() 