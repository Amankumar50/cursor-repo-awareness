# models.py
from dataclasses import dataclass

@dataclass
class Order:
    """Represents an order with a price and discount percentage."""
    price: float
    discount_percent: float
