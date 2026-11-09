import pytest

from mock_model import MockModel
from my_assistant import OrderAssistant
from my_tool import OrderBook


class SilentModel:
    def reply(self, instructions, history):
        return None


def make_helper():
    """Create a fresh assistant and tool for each test."""
    book = OrderBook({"1001": "Processing", "1002": "Shipped"})
    return OrderAssistant("Coach", "Be clear.", book, MockModel())


def test_status_question_uses_the_supplied_tool():
    book = OrderBook({"4321": "Ready for pickup"})
    helper = OrderAssistant("Coach", "Be clear.", book, MockModel())

    assert helper.order_book is book
    assert helper.respond("Where is order 4321?") == "Order 4321: Ready for pickup."


def test_missing_order_number_asks_for_one():
    reply = make_helper().respond("Where is my order?")
    assert "provide one order number" in reply


def test_unknown_order_has_a_helpful_reply():
    reply = make_helper().respond("Track order 9999")

    assert "couldn't find order 9999" in reply
    assert "check the number" in reply


@pytest.mark.parametrize(
    "message",
    ["Cancel order 1001", "Refund order 1002", "Change my address", "Return this"],
)
def test_changes_go_to_a_person_before_status_lookup(message):
    reply = make_helper().respond(message)

    assert "customer service" in reply
    assert "verify your order" in reply
    assert "has not contacted anyone" in reply


def test_unknown_request_gets_a_safe_reply():
    book = OrderBook({})
    helper = OrderAssistant("Coach", "Be clear.", book, SilentModel())
    assert "try again" in helper.respond("What is your favorite sport?")


def test_history_records_roles_and_content_for_every_turn():
    helper = make_helper()

    first = helper.respond("hello")
    second = helper.respond("Order 1002")

    assert helper.history == [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": first},
        {"role": "user", "content": "Order 1002"},
        {"role": "assistant", "content": second},
    ]


def test_number_only_followup_works():
    helper = make_helper()
    helper.respond("Where is my order?")

    assert helper.respond("1001") == "Order 1001: Processing."


def test_multiple_numbers_ask_for_one():
    reply = make_helper().respond("Track orders 1001 and 1002")
    assert "provide one order number" in reply


def test_greeting_is_not_triggered_by_a_substring():
    reply = make_helper().respond("Which shoes are best?")
    assert "not sure" in reply


def test_other_messages_go_to_the_model():
    assert make_helper().respond("hello") == "Hello! How can I help you today?"


def test_rules_work_when_model_has_no_answer():
    helper = OrderAssistant(
        "Coach", "Be clear.", OrderBook({"1001": "Processing"}), SilentModel()
    )
    assert helper.respond("Order 1001") == "Order 1001: Processing."
    assert "customer service" in helper.respond("Cancel order 1001")
