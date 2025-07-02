# main.py
from models import Order
from service import calculate_total

def main():
    order = Order(price=100.0, discount_percent=15.0)
    total = calculate_total(order)
    print(f"Total price after discount: ${total}")

if __name__ == "__main__":
    main()
