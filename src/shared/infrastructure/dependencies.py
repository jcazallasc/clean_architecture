import inject

from events_context.infrastructure.dependencies import events_dependencies
from janto_events_context.infrastructure.dependencies import janto_events_dependencies
from shared.domain.exchange.publisher_exchange import PublisherExchange
from shared.domain.exchange.subscriber_exchange import SubscriberExchange
from shared.infrastructure.exchange.in_memory_exchange import InMemoryExchange


def dependencies_config(binder: inject.Binder) -> None:
    _exchange = InMemoryExchange()

    binder.bind(PublisherExchange, _exchange)
    binder.bind(SubscriberExchange, _exchange)

    events_dependencies(binder)
    janto_events_dependencies(binder)


# Configure a shared injector.
def configure_injector() -> None:
    inject.configure_once(dependencies_config)
