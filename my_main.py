from my_assistant import OrderAssistant
from my_tool import OrderBook
from ollama_model import OllamaModel

INSTRUCTIONS = """You are Coach, an assistant for the fictional All-Star Sports store.
Answer in one short sentence.
All-Star Sports sells soccer balls, basketballs, and tennis rackets.
Customers need their order number to check an order status.
Only state facts provided in these instructions.
If you do not know, say so and refer the customer to customer service.
Never invent an order status or claim to change an order."""

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
        INSTRUCTIONS,
        order_book,
        OllamaModel("granite4.1:3b"),
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
