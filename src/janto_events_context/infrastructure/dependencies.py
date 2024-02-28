import inject

from janto_events_context.domain.repositories import JantoRepository
from janto_events_context.infrastructure.repositories import DjangoJantoRepository


def janto_events_dependencies(binder: inject.Binder) -> None:
    binder.bind(JantoRepository, DjangoJantoRepository())
