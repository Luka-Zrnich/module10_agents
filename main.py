# Luka Zrnich

from chatbot import SupportChatbot
from order_tool import OrderLookup

ORDERS = {"A100": "shipped", "A101": "processing", "A102": "delivered"}

order_tool = OrderLookup(ORDERS)
bot = SupportChatbot(
    "Sunny",
    "You are a friendly support assistant for Bayside Outfitters.",
    order_tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
