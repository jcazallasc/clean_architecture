from typing import TYPE_CHECKING, Dict, Iterable, List

from shared.domain.exchange.consumer import Consumer
from shared.domain.exchange.publisher_exchange import PublisherExchange
from shared.domain.exchange.subscriber_exchange import SubscriberExchange


if TYPE_CHECKING:
    from shared.domain.exchange.event import Event


class InMemoryExchange(PublisherExchange, SubscriberExchange):

    def __init__(self):
        self._consumers: Dict[str, List["Consumer"]] = {}

    def publish(self, event: "Event") -> None:
        for _consumer in self._consumers.get(event.type, []):
            _consumer.consume(event.id.hex, event.type, event.get_attributes())

    def publish_all(self, events: Iterable["Event"]) -> None:
        for _event in events:
            self.publish(_event)

    def subscribe(self, event_type: str, consumer: "Consumer") -> None:
        if event_type not in self._consumers:
            self._consumers[event_type] = []

        if consumer not in self._consumers[event_type]:
            self._consumers[event_type].append(consumer)
