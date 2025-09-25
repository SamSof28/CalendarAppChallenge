from dataclasses import dataclass, field
from datetime import datetime, date, time
from typing import ClassVar, Optional

from app.services.util import generate_unique_id, date_lower_than_today_error, event_not_found_error, \
    reminder_not_found_error, slot_not_available_error

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
    reminders: list[Reminder] = field(default_factory=list)
    id: Optional[str] = generate_unique_id()

    def add_reminder(self, date_time: datetime, type_: str):
        new_reminder = Reminder(date_time, type_)
        self.reminders.append(new_reminder)

    def delete_reminder(self, reminder_index: int):
        if reminder_index in self.reminders:
            self.reminders.pop(reminder_index)
        else:
            reminder_not_found_error()

    def __str__(self):
        return f"ID: {id}\nEvent title: {self.title}\nDescription: {self.description}\nTime: {self.start_at} - {self.end_at}"

class Day:
    def __init__(self, date_: datetime):
        self.date_ = date_
        self.slots: dict[time, str | None] = {}
        self._init_slots()

    def _init_slots(self):
        for minutes in range(0, 24 * 60, 15):  # De 0 a 1440 minutos, paso de 15
            hour = minutes // 60
            minute = minutes % 60
            self.slots[time(hour, minute)] = None

    def add_event(self, event_id: str, start_at: time, end_at: time):
        if event_id in self.slots:
            slot_not_available_error()

    def delete_event(self, event_id: str):
        deleted = False
        for slot, saved_id in self.slots.items():
            if saved_id == event_id:
                self.slots[slot] = None
                deleted = True
        if not deleted:
            event_not_found_error()

    def update_event(self, event_id: str, start_at: time, end_at: time):
        for slot in self.slots:
            if self.slots[slot] == event_id:
                self.slots[slot] = None

        for slot in self.slots:
            if start_at <= slot < end_at:
                if self.slots[slot]:
                    slot_not_available_error()
                else:
                    self.slots[slot] = event_id

class Calendar:
    def __init__(self, ):
        self.days: dict[date, Day] = {}
        self.events: dict[str, Event] = {}

    def add_event(self, title: str, description: str, date_: date, start_at: time, end_at: time ):
        if date_ not in self.days:
            datetime.now().date()
