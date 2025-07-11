# utils.py
"""Utility functions for calculations and data processing."""

from typing import Union, List
from constants import PRICE_DECIMAL_PLACES
from validators import validate_price, validate_discount_percent

def apply_discount(price: float, discount_percent: float) -> float:
    """
    Apply a percentage discount to the price.
    
    Args:
        price: Original price (must be non-negative)
        discount_percent: Discount percentage (0-100)
        
    Returns:
        Discounted price, rounded to specified decimal places
        
    Raises:
        InvalidPriceError: If price is negative
        InvalidDiscountError: If discount_percent is outside valid range
    """
    validate_price(price)
    validate_discount_percent(discount_percent)
    
    discounted = price * (1 - discount_percent / 100)
    return round(discounted, PRICE_DECIMAL_PLACES)

def calculate_percentage(part: float, whole: float) -> float:
    """
    Calculate what percentage 'part' is of 'whole'.
    
    Args:
        part: The part value
        whole: The whole value
        
    Returns:
        Percentage value
        
    Raises:
        ZeroDivisionError: If whole is zero
    """
    if whole == 0:
        raise ZeroDivisionError("Cannot calculate percentage of zero")
    
    return round((part / whole) * 100, 2)

def format_currency(amount: float, currency_symbol: str = "$") -> str:
    """
    Format amount as currency string.
    
    Args:
        amount: Amount to format
        currency_symbol: Currency symbol to use
        
    Returns:
        Formatted currency string
    """
    return f"{currency_symbol}{amount:.2f}"

def calculate_average(values: List[Union[int, float]]) -> float:
    """
    Calculate average of a list of numbers.
    
    Args:
        values: List of numeric values
        
    Returns:
        Average value
        
    Raises:
        ValueError: If list is empty
        TypeError: If values contains non-numeric types
    """
    if not values:
        raise ValueError("Cannot calculate average of empty list")
    
    if not all(isinstance(v, (int, float)) for v in values):
        raise TypeError("All values must be numeric")
    
    return round(sum(values) / len(values), PRICE_DECIMAL_PLACES)
