class AppointmentBook:
    """Store appointment availability for the example assistant."""

    def __init__(self, open_times):
        self.open_times = open_times

    def find_day(self, text):
        import re

        words = re.findall(r"[a-z]+", text.lower())
        for day in self.open_times:
            if day in words:
                return day
        return None

    def times_for(self, day):
        return self.open_times.get(day)
