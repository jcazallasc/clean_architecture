import abc
from datetime import datetime
from typing import List

from events_context.domain.entities import EventEntity
from janto_events_context.domain.entities import JantoEventEntity
from shared.domain.enums.event_provider import EventProvider


class EventRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_or_update(self, event_entity: JantoEventEntity) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def search(self, starts_at: datetime, ends_at: datetime) -> List[EventEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    def deactivate_events(self, exclude_event_ids: List[int], provider: EventProvider) -> None:
        raise NotImplementedError
