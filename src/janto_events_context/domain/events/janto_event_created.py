from shared.domain.exchange.event import Event
from shared.domain.exchange.event_attributes import EventAttributes


class JantoEventCreated(Event):
    type: str = "clean_architecture.events.1.event.created"


class JantoEventCreatedAttributes(EventAttributes):
    base_event_id: int
