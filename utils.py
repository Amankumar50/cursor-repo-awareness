# utils.py
def apply_discount(price: float, discount_percent: float) -> float:
    """
    Apply a percentage discount to the price.
    Returns the discounted price, rounded to two decimals.
    """
    discounted = price * (1 - discount_percent / 100)
    return round(discounted, 2)
