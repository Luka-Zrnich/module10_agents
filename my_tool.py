import re


class OrderBook:
    """Store order data without handling conversations."""

    def __init__(self, orders):
        """Store a dictionary with order numbers as string keys."""
        self.orders = orders

    def find_order_number(self, text):
        """Return one number from the message, or None if unclear."""
        numbers = re.findall(r"\b[0-9]+\b", text)
        if len(numbers) == 1:
            return numbers[0]
        return None

    def status_for(self, order_number):
        """Return a recorded status, or None when no order matches."""
        return self.orders.get(order_number)
