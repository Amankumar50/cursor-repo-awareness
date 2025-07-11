# test_pipeline.py
"""Test file to verify CI/CD pipeline functionality."""


def pipeline_test_function():
    """Simple function to test pipeline execution."""
    return "Pipeline is working!"


def calculate_fibonacci(n: int) -> int:
    """Calculate fibonacci number to test more complex logic."""
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)


if __name__ == "__main__":
    print(pipeline_test_function())
    print(f"Fibonacci(5) = {calculate_fibonacci(5)}")