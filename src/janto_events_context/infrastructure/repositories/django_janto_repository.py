from typing import List, Tuple

from janto_events_context.domain.entities import JantoEventEntity
from janto_events_context.domain.events.janto_event_created import JantoEventCreated, JantoEventCreatedAttributes
from janto_events_context.domain.events.janto_event_updated import JantoEventUpdated, JantoEventUpdatedAttributes
from janto_events_context.domain.repositories import JantoRepository
from janto_events_context.models import JantoEvent
from shared.domain.enums.janto_event_status import JantoEventStatus
from shared.infrastructure.exchange.in_memory_event_storage import InMemoryEventStorage


class DjangoJantoRepository(InMemoryEventStorage, JantoRepository):

    def create_or_update(self, entity: JantoEventEntity) -> Tuple[JantoEventEntity, bool]:
        _django_event, _created = JantoEvent.objects.update_or_create(
            base_event_id=entity.base_event_id,
            defaults=entity.dict(),
        )

        if _created:
            _event = JantoEventCreated(
                attributes=JantoEventCreatedAttributes(
                    base_event_id=_django_event.base_event_id,
                ),
            )
        else:
            _event = JantoEventUpdated(
                attributes=JantoEventUpdatedAttributes(
                    base_event_id=_django_event.base_event_id,
                ),
            )

        self.record(_event)

        return (JantoEventEntity.from_orm(_django_event), _created)

    def retrieve_by_event_id(self, base_event_id: int) -> JantoEventEntity:
        _event = JantoEvent.objects.get(base_event_id=base_event_id)

        return JantoEventEntity.from_orm(_event)

    def deactivate_events(self, exclude_base_event_ids: List[int]) -> None:
        JantoEvent.objects.exclude(base_event_id__in=exclude_base_event_ids).update(
            status=JantoEventStatus.Inactive.value
        )
