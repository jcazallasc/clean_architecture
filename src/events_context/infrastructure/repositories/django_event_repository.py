from datetime import datetime
from typing import List

from events_context.domain.entities import EventEntity
from events_context.domain.repositories import EventRepository
from events_context.models import Event
from janto_events_context.domain.entities import JantoEventEntity
from shared.domain.enums.event_provider import EventProvider
from shared.domain.enums.event_status import EventStatus


class DjangoEventRepository(EventRepository):

    def create_or_update(self, event_entity: JantoEventEntity) -> None:
        _data = event_entity.normalize()

        _event, _created = Event.objects.update_or_create(
            original_id=_data["original_id"],
            provider=_data["provider"],
            defaults=_data,
        )

        if not _created:
            _event.status = EventStatus.PendingReview.value
            _event.save()

    def deactivate_events(self, exclude_event_ids: List[int], provider: EventProvider) -> None:
        Event.objects.exclude(original_id__in=exclude_event_ids, provider=provider).update(
            status=EventStatus.Inactive.value
        )

    def search(self, starts_at: datetime, ends_at: datetime) -> List[EventEntity]:
        _events = (Event.objects.filter(start_date__gte=starts_at,
                   end_date__lte=ends_at).exclude(status=EventStatus.Inactive.value))

        _data = [
            EventEntity.from_orm(_event)
            for _event in _events
        ]

        return _data
