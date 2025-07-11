# math_functions.py
"""Mathematical functions for testing CI/CD pipeline."""


def fibonacci(n: int) -> int:
    """Calculate fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def is_prime(n: int) -> bool:
    """Check if number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True