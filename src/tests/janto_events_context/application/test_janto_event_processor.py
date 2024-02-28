from datetime import datetime
from unittest.mock import Mock

from django.test import TestCase
from pydantic import ValidationError

from janto_events_context.application.janto_event_processor import JantoEventProcessor
from janto_events_context.domain.entities import JantoEventEntity
from janto_events_context.models import JantoEvent


class JantoEventProcessorTestCase(TestCase):

    def setUp(self) -> None:
        self.mock_publisher_exchange = Mock()

        self.use_case = JantoEventProcessor(publisher_exchange=self.mock_publisher_exchange)

        self.entity = JantoEventEntity(
            base_event_id=1,
            event_id=1,
            title="Testing",
            sell_mode="online",
            event_start_date=datetime(2010, 1, 1, 10, 10, 10),
            event_end_date=datetime(2011, 1, 1, 10, 10, 10),
            sell_from=datetime(2010, 1, 1, 10, 10, 10),
            sell_to=datetime(2011, 1, 1, 10, 10, 10),
            sold_out=False,
            zones=[
                {
                    "zone_id": 1,
                    "capacity": 200,
                    "price": 10.00,
                    "name": "Platea",
                },
                {
                    "zone_id": 2,
                    "capacity": 200,
                    "price": 50.00,
                    "name": "Palco",
                }
            ],
        )

    def test_given_janto_event_processor_when_processing_event_then_event_stored(self):
        _pre_exists = JantoEvent.objects.filter(base_event_id=self.entity.base_event_id).exists()

        self.use_case(self.entity.dict())

        _post_exists = JantoEvent.objects.filter(base_event_id=self.entity.base_event_id).exists()

        self.assertFalse(_pre_exists)
        self.assertTrue(_post_exists)
        self.assertTrue(self.mock_publisher_exchange.publish_all.called)

    def test_given_janto_event_processor_when_missing_data_then_error(self):
        with self.assertRaises(ValidationError):
            _data = self.entity.dict()

            _data.pop("title")

            self.use_case(_data)
