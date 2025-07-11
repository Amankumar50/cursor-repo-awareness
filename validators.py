# validators.py
"""Input validation functions."""

from typing import Union
from exceptions import InvalidDiscountError, InvalidPriceError
from constants import MIN_DISCOUNT_PERCENT, MAX_DISCOUNT_PERCENT, MIN_PRICE

def validate_price(price: float) -> None:
    """
    Validate price value.
    
    Args:
        price: Price to validate
        
    Raises:
        InvalidPriceError: If price is negative
        TypeError: If price is not a number
    """
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number")
    
    if price < MIN_PRICE:
        raise InvalidPriceError(f"Price cannot be negative: {price}")

def validate_discount_percent(discount_percent: float) -> None:
    """
    Validate discount percentage.
    
    Args:
        discount_percent: Discount percentage to validate
        
    Raises:
        InvalidDiscountError: If discount is outside valid range
        TypeError: If discount is not a number
    """
    if not isinstance(discount_percent, (int, float)):
        raise TypeError("Discount percent must be a number")
    
    if not (MIN_DISCOUNT_PERCENT <= discount_percent <= MAX_DISCOUNT_PERCENT):
        raise InvalidDiscountError(
            f"Discount percent must be between {MIN_DISCOUNT_PERCENT}% and {MAX_DISCOUNT_PERCENT}%: {discount_percent}%"
        )