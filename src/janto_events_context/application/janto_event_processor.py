import inject

from janto_events_context.domain.entities import JantoEventEntity
from janto_events_context.domain.repositories.janto_repository import JantoRepository
from shared.domain.exchange.publisher_exchange import PublisherExchange


class JantoEventProcessor:

    @inject.autoparams()
    def __init__(self, janto_repository: JantoRepository, publisher_exchange: PublisherExchange):
        self.janto_repository = janto_repository
        self.publisher_exchange = publisher_exchange

    def __call__(self, event_data: dict) -> None:
        _entity = JantoEventEntity(**event_data)

        self.janto_repository.create_or_update(_entity)

        self.publisher_exchange.publish_all(self.janto_repository.pull_events())
