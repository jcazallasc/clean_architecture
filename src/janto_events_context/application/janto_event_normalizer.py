import inject

from events_context.domain.repositories.event_repository import EventRepository
from janto_events_context.domain.repositories.janto_repository import JantoRepository


class JantoEventNormalizer:

    @inject.autoparams()
    def __init__(self, janto_repository: JantoRepository, event_repository: EventRepository):
        self.janto_repository = janto_repository
        self.event_repository = event_repository

    def __call__(self, base_event_id: int) -> None:
        _janto_entity = self.janto_repository.retrieve_by_event_id(base_event_id)

        self.event_repository.create_or_update(_janto_entity)
