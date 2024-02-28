from typing import TYPE_CHECKING, List

from shared.domain.exchange.event_storage import EventStorage


if TYPE_CHECKING:
    from shared.domain.exchange.event import Event


class InMemoryEventStorage(EventStorage):

    def __init__(self):
        self._events = []

    def record(self, event: "Event") -> None:
        self._events.append(event)

    def pull_events(self) -> List["Event"]:
        _result = self._events

        self._events = []

        return _result
