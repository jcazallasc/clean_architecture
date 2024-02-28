import inject

from events_context.domain.repositories import EventRepository
from events_context.infrastructure.repositories import DjangoEventRepository


def events_dependencies(binder: inject.Binder) -> None:
    binder.bind(EventRepository, DjangoEventRepository())
