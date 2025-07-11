# models.py
"""Data models for the application."""

from dataclasses import dataclass
from typing import Optional
from validators import validate_price, validate_discount_percent
from constants import DEFAULT_DISCOUNT_PERCENT


@dataclass
class Order:
    """Represents an order with a price and discount percentage.

    Attributes:
        price: The base price of the order (must be non-negative)
        discount_percent: The discount percentage to apply (0-100)

    Raises:
        InvalidPriceError: If price is negative
        InvalidDiscountError: If discount_percent is outside valid range
    """

    price: float
    discount_percent: float = DEFAULT_DISCOUNT_PERCENT

    def __post_init__(self) -> None:
        """Validate order data after initialization."""
        validate_price(self.price)
        validate_discount_percent(self.discount_percent)

    def get_discount_amount(self) -> float:
        """Calculate the discount amount.

        Returns:
            The discount amount in currency units
        """
        return self.price * (self.discount_percent / 100)

    def get_discounted_price(self) -> float:
        """Calculate the price after discount.

        Returns:
            The final price after applying discount
        """
        return self.price - self.get_discount_amount()
