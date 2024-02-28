from datetime import datetime

from django.test import TestCase

from events_context.models import Event
from janto_events_context.application.janto_event_normalizer import JantoEventNormalizer
from janto_events_context.models import JantoEvent
from shared.domain.enums import EventProvider


class JantoEventNormalizerTestCase(TestCase):

    def setUp(self) -> None:
        self.use_case = JantoEventNormalizer()

        self.janto_event = JantoEvent.objects.create(
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

    def test_given_janto_event_normalizer_when_janto_event_sent_then_event_normalized_and_stored(self):
        _pre_exists = Event.objects.filter(
            original_id=self.janto_event.base_event_id,
            provider=EventProvider.Janto.value,
        ).exists()

        self.use_case(self.janto_event.base_event_id)

        _post_exists = Event.objects.filter(
            original_id=self.janto_event.base_event_id,
            provider=EventProvider.Janto.value,
        ).exists()

        self.assertFalse(_pre_exists)
        self.assertTrue(_post_exists)
