# exceptions.py
"""Custom exception classes for the application."""


class InvalidDiscountError(ValueError):
    """Raised when discount percentage is invalid."""

    pass


class InvalidPriceError(ValueError):
    """Raised when price is negative."""

    pass


class CalculationError(Exception):
    """Raised when calculation fails."""

    pass
