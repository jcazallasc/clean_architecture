import abc
from typing import List, Tuple

from janto_events_context.domain.entities.janto_event_entity import JantoEventEntity
from shared.domain.exchange.event_storage import EventStorage


class JantoRepository(EventStorage, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_or_update(self, entity: JantoEventEntity) -> Tuple[JantoEventEntity, bool]:
        raise NotImplementedError

    @abc.abstractmethod
    def retrieve_by_event_id(self, base_event_id: int) -> JantoEventEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def deactivate_events(self, exclude_base_event_ids: List[int]) -> None:
        raise NotImplementedError
