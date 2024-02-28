from datetime import datetime

from django.test import TestCase

from janto_events_context.domain.entities import JantoEventEntity
from janto_events_context.models import JantoEvent


class JantoEventEntityTestCase(TestCase):

    def setUp(self) -> None:
        self.janto_event = JantoEvent.objects.create(
            base_event_id=1,
            event_id=1,
            title="Testing",
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

        self.entity = JantoEventEntity.from_orm(self.janto_event)

    def test_given_janto_event_entity_then_valid_min_price(self):
        _min_price = self.entity.get_min_price()

        self.assertEqual(10.00, _min_price)

    def test_given_janto_event_entity_then_valid_max_price(self):
        _max_price = self.entity.get_max_price()

        self.assertEqual(50.00, _max_price)        

    def test_given_janto_event_entity_then_valid_normalization(self):
        _data = self.entity.normalize()

        self.assertTrue("original_id" in _data)
        self.assertTrue("provider" in _data)
        self.assertTrue("title" in _data)
        self.assertTrue("start_date" in _data)
        self.assertTrue("end_date" in _data)
        self.assertTrue("min_price" in _data)
        self.assertTrue("max_price" in _data)
