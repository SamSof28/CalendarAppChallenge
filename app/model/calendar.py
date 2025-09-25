from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar, Optional

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_availableim
from dataclasses import dataclass, field

@dataclass
class Reminder:
    EMAIL: ClassVar[str] = "email"
    SYSTEM: ClassVar[str] = "system"

    date_time: datetime
    type: Optional[str] = EMAIL


    def __str__(self):
        return f"Reminder on {self.date_time} of type {type}"




@dataclass
class Event:
    title: str
    description: str
    date_: date
    start_at: time
    end_at: time
    reminders: ClassVar[list[Reminder]] = []
    id: Optional[str] = generate_unique_id()

    def add_reminder(self, date_time: datetime, type_: str):
        new_reminder = Reminder(date_time, type_)
        self.reminders.append(new_reminder)

    def delete_reminder(self, reminder_index: int):
        if reminder_index in self.reminders:
            self.reminders.pop(reminder_index)
        else:
            reminder_not_found_error()

    def
# TODO: Implement Day class here


# TODO: Implement Calendar class here
