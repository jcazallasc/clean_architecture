import inject
from django.apps import AppConfig

from janto_events_context.domain.events.janto_events_consumer import EVENT_TYPES, JantoEventsConsumer
from shared.domain.exchange.subscriber_exchange import SubscriberExchange


class JantoEventsContextConfig(AppConfig):
    name = 'janto_events_context'

    def ready(self):
        self._subscribe_consumers()

    def _subscribe_consumers(self) -> None:
        _subscriber = inject.instance(SubscriberExchange)

        _consumer = JantoEventsConsumer()

        for _event_type in EVENT_TYPES.keys():
            _subscriber.subscribe(_event_type, _consumer)
