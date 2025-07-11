# service.py
"""Business logic services for order processing."""

from typing import List, Optional
from models import Order
from utils import apply_discount
from exceptions import CalculationError
from logger import setup_logger

logger = setup_logger(__name__)


def calculate_total(order: Order) -> float:
    """
    Calculate the final total for the given order.

    Args:
        order: Order instance with price and discount information

    Returns:
        Final price after applying discount, rounded to 2 decimal places

    Raises:
        CalculationError: If calculation fails
        TypeError: If order is not an Order instance
    """
    if not isinstance(order, Order):
        raise TypeError("Expected Order instance")

    try:
        logger.info(
            f"Calculating total for order: price={order.price}, discount={order.discount_percent}%"
        )
        total = apply_discount(order.price, order.discount_percent)
        logger.info(f"Calculated total: {total}")
        return total
    except Exception as e:
        logger.error(f"Failed to calculate total: {e}")
        raise CalculationError(f"Calculation failed: {e}") from e


def calculate_bulk_total(orders: List[Order]) -> float:
    """
    Calculate total for multiple orders.

    Args:
        orders: List of Order instances

    Returns:
        Combined total of all orders

    Raises:
        CalculationError: If any calculation fails
        TypeError: If orders is not a list
    """
    if not isinstance(orders, list):
        raise TypeError("Expected list of orders")

    if not orders:
        return 0.0

    try:
        logger.info(f"Calculating bulk total for {len(orders)} orders")
        total = sum(calculate_total(order) for order in orders)
        logger.info(f"Bulk total calculated: {total}")
        return total
    except Exception as e:
        logger.error(f"Failed to calculate bulk total: {e}")
        raise CalculationError(f"Bulk calculation failed: {e}") from e


def apply_tax(amount: float, tax_rate: float) -> float:
    """
    Apply tax to an amount.

    Args:
        amount: Base amount
        tax_rate: Tax rate as percentage (e.g., 10.0 for 10%)

    Returns:
        Amount with tax applied

    Raises:
        ValueError: If tax_rate is negative
    """
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")

    return round(amount * (1 + tax_rate / 100), 2)
