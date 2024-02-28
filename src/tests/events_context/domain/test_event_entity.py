from datetime import datetime
from uuid import uuid4

from django.test import TestCase

from events_context.domain.entities import EventEntity
from events_context.models import Event
from shared.domain.enums import EventProvider, EventStatus


class EventEntityTestCase(TestCase):

    def setUp(self) -> None:
        self.event = Event.objects.create(
            id=uuid4(),
            original_id="1",
            provider=EventProvider.Janto.value,
            title="Testing",
            start_date=datetime(2010, 1, 1, 10, 10, 10),
            end_date=datetime(2011, 1, 1, 10, 10, 10),
            min_price=10.00,
            max_price=50.00,
            status=EventStatus.Active.value,
        )

        self.entity = EventEntity.from_orm(self.event)     

    def test_given_event_entity_then_valid_serialization(self):
        _data = self.entity.dict()

        self.assertTrue("id" in _data)
        self.assertTrue("title" in _data)
        self.assertTrue("start_date" in _data)
        self.assertTrue("start_time" in _data)
        self.assertTrue("end_date" in _data)
        self.assertTrue("end_time" in _data)
        self.assertTrue("min_price" in _data)
        self.assertTrue("max_price" in _data)
