import inject

from events_context.domain.repositories import EventRepository
from janto_events_context.domain.repositories import JantoRepository
from janto_events_context.infrastructure.services.janto_service import JantoService
from shared.domain.enums.event_provider import EventProvider


class JantoFeeder:

    @inject.autoparams()
    def __init__(self, janto_repository: JantoRepository, event_repository: EventRepository):
        self.janto_repository = janto_repository
        self.event_repository = event_repository

        self.service = JantoService()

    def __call__(self) -> None:
        _base_event_ids = self.service.fetch()

        self.janto_repository.deactivate_events(_base_event_ids)

        self.event_repository.deactivate_events(_base_event_ids, EventProvider.Janto.value)
