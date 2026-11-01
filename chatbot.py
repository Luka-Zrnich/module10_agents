# Luka Zrnich

HANDOFF_WORDS = ["address", "payment", "card"]


class SupportChatbot:
    def __init__(self, name, instructions, order_tool):
        self.name = name
        self.instructions = instructions
        self.order_tool = order_tool
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a human agent."
        if "order" in text:
            return self.order_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. I can check an order status for you."
        return "I'm not sure how to help with that. I can check an order status."

    def needs_human(self, text):
        for word in HANDOFF_WORDS:
            return word in text

    def order_reply(self, user_message):
        order_id = self.order_tool.find_order_id(user_message)
        if order_id is None:
            return "Which order? Please send an order ID like A100."
        status = self.order_tool.find_status(order_id)
        return f"Order {order_id} is {status}."

    def count_user_messages(self):
        count = 0
        for message in self.history:
            if message["role"] == "user":
                count += 1
        return count
