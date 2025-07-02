import unittest
from models import Order
from service import calculate_total
from unittest.mock import patch

class TestCalculateTotal(unittest.TestCase):
    @patch('service.apply_discount')
    def test_calculate_total_calls_apply_discount(self, mock_apply):
        mock_apply.return_value = 75.0
        order = Order(price=100.0, discount_percent=25.0)
        result = calculate_total(order)
        mock_apply.assert_called_once_with(100.0, 25.0)
        self.assertEqual(result, 75.0)

if __name__ == '__main__':
    unittest.main()
