from typing import List

import inject
from pydantic import BaseModel

from events_context.domain.entities import EventEntity
from events_context.domain.repositories.event_repository import EventRepository
from events_context.domain.value_objects import EndsAt, StartsAt


class EventSearchParams(BaseModel):
    starts_at: StartsAt
    ends_at: EndsAt


class EventSearcher:

    @inject.autoparams()
    def __init__(self, repository: EventRepository):
        self.repository = repository

    def __call__(self, starts_at: str, ends_at: str) -> List[EventEntity]:
        _params = EventSearchParams(
            starts_at=starts_at,
            ends_at=ends_at,
        )

        return self.repository.search(_params.starts_at, _params.ends_at)
