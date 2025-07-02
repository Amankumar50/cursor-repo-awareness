# service.py
from models import Order
from utils import apply_discount

def calculate_total(order: Order) -> float:
    """
    Calculate the final total for the given order using apply_discount().
    """
    return apply_discount(order.price, order.discount_percent)
