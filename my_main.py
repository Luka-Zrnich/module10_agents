from my_assistant import OrderAssistant
from my_tool import OrderBook

ORDERS = {
    "1001": "Processing - your soccer ball is being packed",
    "1002": "Shipped - your basketball has left our store",
    "1003": "Delivered - your tennis racket was delivered",
}


def main():
    """Accept messages until quit and report the conversation length."""
    order_book = OrderBook(ORDERS)
    helper = OrderAssistant(
        "Coach",
        "Help All-Star Sports customers check their order status.",
        order_book,
    )

    print("Type a message, or type quit to stop.")

    while True:
        user_message = input("You: ")

        if user_message.strip().lower() == "quit":
            break

        print(f"{helper.name}: {helper.respond(user_message)}")

    print(f"Messages in this conversation: {len(helper.history)}")


if __name__ == "__main__":
    main()
