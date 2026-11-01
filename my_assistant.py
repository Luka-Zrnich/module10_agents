import re

HANDOFF_WORDS = {"cancel", "cancellation", "refund", "return", "exchange"}
STATUS_WORDS = {"order", "status", "track", "tracking", "package"}


class OrderAssistant:
    """Answer mock status questions and refer changes to a person."""

    def __init__(self, name, instructions, order_book):
        """Store the assistant's name, instructions, tool, and history."""
        self.name = name
        self.instructions = instructions
        self.order_book = order_book
        self.history = []

    def respond(self, user_message):
        """Record both sides of a turn and return the assistant's reply."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply using simple keywords, not AI."""
        text = user_message.lower().strip()
        words = set(re.findall(r"[a-z]+", text))

        if self.needs_human(words):
            return (
                "Please contact customer service for refunds, returns, "
                "cancellations, or address changes. A person must verify "
                "your order before making changes. "
                "This demo has not contacted anyone."
            )

        if words & STATUS_WORDS or re.fullmatch(r"#?[0-9]+", text):
            return self.status_reply(user_message)

        if words & {"hello", "hi", "hey"}:
            return (
                f"Hello! I'm {self.name} from All-Star Sports. "
                "Ask me for an order status using your order number."
            )

        return (
            "I'm not sure how to help with that. "
            "I can check an order status using an order number."
        )

    def needs_human(self, words):
        """Send requests involving changes or money to customer service."""
        return bool(words & HANDOFF_WORDS) or "address" in words

    def status_reply(self, user_message):
        """Use the order tool and handle missing or unknown numbers."""
        number = self.order_book.find_order_number(user_message)

        if number is None:
            return "Please provide one order number, such as 1001."

        status = self.order_book.status_for(number)

        if status is None:
            return (
                f"I couldn't find order {number}. Please check the number "
                "or contact customer service."
            )

        return f"Order {number}: {status}."
