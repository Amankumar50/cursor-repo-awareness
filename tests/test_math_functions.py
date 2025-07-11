import unittest
from math_functions import fibonacci, factorial, is_prime


class TestMathFunctions(unittest.TestCase):
    """Test mathematical functions."""

    def test_fibonacci(self):
        """Test fibonacci calculation."""
        test_cases = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5)]
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(fibonacci(n), expected)

    def test_factorial(self):
        """Test factorial calculation."""
        test_cases = [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120)]
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(factorial(n), expected)

    def test_is_prime(self):
        """Test prime number detection."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        non_primes = [0, 1, 4, 6, 8, 9, 10, 12, 15, 16, 18, 20]
        
        for p in primes:
            with self.subTest(n=p):
                self.assertTrue(is_prime(p))
        
        for np in non_primes:
            with self.subTest(n=np):
                self.assertFalse(is_prime(np))


if __name__ == "__main__":
    unittest.main()