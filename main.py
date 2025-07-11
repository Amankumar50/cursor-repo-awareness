# main.py
"""Main application entry point."""

from typing import Optional
from models import Order
from service import calculate_total, calculate_bulk_total, apply_tax
from utils import format_currency
from exceptions import InvalidPriceError, InvalidDiscountError, CalculationError
from logger import setup_logger

logger = setup_logger(__name__)


def create_sample_order() -> Order:
    """
    Create a sample order for demonstration.

    Returns:
        Sample Order instance
    """
    return Order(price=100.0, discount_percent=15.0)


def demonstrate_single_order() -> None:
    """
    Demonstrate single order calculation.
    """
    try:
        logger.info("Creating sample order")
        order = create_sample_order()

        logger.info(f"Order details: {order}")
        total = calculate_total(order)

        print(f"Order Details:")
        print(f"  Original Price: {format_currency(order.price)}")
        print(f"  Discount: {order.discount_percent}%")
        print(f"  Discount Amount: {format_currency(order.get_discount_amount())}")
        print(f"  Final Total: {format_currency(total)}")

    except (InvalidPriceError, InvalidDiscountError, CalculationError) as e:
        logger.error(f"Order processing failed: {e}")
        print(f"Error: {e}")


def demonstrate_bulk_orders() -> None:
    """
    Demonstrate bulk order calculation.
    """
    try:
        orders = [
            Order(price=50.0, discount_percent=10.0),
            Order(price=75.0, discount_percent=20.0),
            Order(price=120.0, discount_percent=5.0),
        ]

        bulk_total = calculate_bulk_total(orders)
        total_with_tax = apply_tax(bulk_total, 8.5)  # 8.5% tax

        print(f"\nBulk Order Summary:")
        print(f"  Number of Orders: {len(orders)}")
        print(f"  Subtotal: {format_currency(bulk_total)}")
        print(f"  Tax (8.5%): {format_currency(total_with_tax - bulk_total)}")
        print(f"  Final Total: {format_currency(total_with_tax)}")

    except Exception as e:
        logger.error(f"Bulk order processing failed: {e}")
        print(f"Error: {e}")


def main() -> None:
    """
    Main application function.
    """
    logger.info("Starting application")

    print("=== Order Processing System ===")

    # Demonstrate single order
    demonstrate_single_order()

    # Demonstrate bulk orders
    demonstrate_bulk_orders()

    logger.info("Application completed")


if __name__ == "__main__":
    main()
