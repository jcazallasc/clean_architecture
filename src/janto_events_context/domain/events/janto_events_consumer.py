from janto_events_context.application.janto_event_normalizer import JantoEventNormalizer
from janto_events_context.domain.events.janto_event_created import JantoEventCreated
from janto_events_context.domain.events.janto_event_updated import JantoEventUpdated
from shared.domain.exchange.consumer import Consumer


def _on_janto_event(attributes: dict) -> None:
    JantoEventNormalizer()(attributes["base_event_id"])


EVENT_TYPES = {
    JantoEventCreated.schema()["properties"]["type"]["default"]: _on_janto_event,
    JantoEventUpdated.schema()["properties"]["type"]["default"]: _on_janto_event,
}


class JantoEventsConsumer(Consumer):

    def consume(self, event_id: str, event_type: str, attributes: dict) -> None:
        EVENT_TYPES[event_type](attributes)
