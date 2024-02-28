from shared.domain.exchange.event import Event
from shared.domain.exchange.event_attributes import EventAttributes


class JantoEventUpdated(Event):
    type: str = "clean_architecture.events.1.event.updated"


class JantoEventUpdatedAttributes(EventAttributes):
    base_event_id: int
