import unittest
from models import Order


class TestOrderModel(unittest.TestCase):
    def test_order_dataclass_fields(self):
        order = Order(price=50.0, discount_percent=10.0)
        self.assertEqual(order.price, 50.0)
        self.assertEqual(order.discount_percent, 10.0)


if __name__ == "__main__":
    unittest.main()
