import random
from datetime import datetime

from django.test import TestCase
from pydantic import ValidationError

from events_context.application.event_searcher import EventSearcher
from events_context.models import Event
from shared.domain.enums import EventProvider


class EventSearcherTestCase(TestCase):

    def setUp(self) -> None:
        for _i in range(10):
            Event.objects.create(
                original_id="test_id",
                provider=EventProvider.Janto.value,
                title="Testing",
                start_date=datetime(2010, 1, 1, 10, 10, 10),
                end_date=datetime(2011, 1, 1, 10, 10, 10),
                min_price=random.randint(1, 50),
                max_price=random.randint(50, 100),
            )

        self.use_case = EventSearcher()

    def test_given_event_searcher_when_valid_params_then_return_event_list(self):
        starts_at = datetime(2001, 1, 1, 10, 10, 10)
        ends_at = datetime(2022, 1, 1, 10, 10, 10)

        _result = self.use_case(starts_at, ends_at)

        self.assertEqual(Event.objects.all().count(), len(_result))

    def test_given_search_viewset_when_invalid_starts_at_param_then_return_400(self):
        starts_at = "2001/12-01"
        ends_at = datetime(2022, 1, 1, 10, 10, 10)

        with self.assertRaises(ValidationError):
            self.use_case(starts_at, ends_at)
