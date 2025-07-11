import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import from the main test_pipeline module
import test_pipeline


class TestPipelineFunctionality(unittest.TestCase):
    """Test cases for pipeline testing."""

    def test_pipeline_function(self):
        """Test the basic pipeline function."""
        result = test_pipeline.pipeline_test_function()
        self.assertEqual(result, "Pipeline is working!")

    def test_fibonacci_calculation(self):
        """Test fibonacci calculation."""
        test_cases = [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 3),
            (5, 5),
        ]
        
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(test_pipeline.calculate_fibonacci(n), expected)

    def test_fibonacci_edge_cases(self):
        """Test fibonacci edge cases."""
        self.assertEqual(test_pipeline.calculate_fibonacci(0), 0)
        self.assertEqual(test_pipeline.calculate_fibonacci(1), 1)


if __name__ == "__main__":
    unittest.main()