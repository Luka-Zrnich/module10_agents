from appointment_bot import AppointmentHelper
from appointment_tool import AppointmentBook
from mock_model import MockModel


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_helper():
    """Build a fresh helper with its own tool for each test."""
    book = AppointmentBook({"monday": "9:00 am and 2:30 pm", "friday": "none"})
    return AppointmentHelper("Robin", "Be clear.", book, MockModel())
