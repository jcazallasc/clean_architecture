from datetime import datetime
from unittest.mock import Mock, patch

import requests
from django.test import TestCase

from janto_events_context.application.janto_feeder import JantoFeeder
from janto_events_context.models import JantoEvent
from shared.domain.enums import JantoEventStatus
from tests.janto_events_context.application.fixtures import JANTO_FETCH_RESPONSE


class JantoEventFeederTestCase(TestCase):

    def setUp(self) -> None:
        self.use_case = JantoFeeder()

    def create_janto_event(self, n: int) -> None:
        for _i in range(n):
            JantoEvent.objects.create(
                base_event_id=_i,
                event_id=_i,
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

    @patch("janto_events_context.infrastructure.services.janto_service.process_janto_event")
    @patch.object(requests, "get")
    def test_given_janto_feeder_when_retrieving_events_then_async_task_called(self, mock_get, mock_process_event_async):
        _response_mock = Mock()
        _response_mock.content = JANTO_FETCH_RESPONSE

        mock_get.return_value = _response_mock

        mock_process_event_async.return_value = Mock()

        self.use_case()

        self.assertTrue(mock_get.called)
        self.assertTrue(mock_process_event_async.delay.called)

    @patch("janto_events_context.infrastructure.services.janto_service.process_janto_event")
    @patch.object(requests, "get")
    def test_given_janto_feeder_when_retrieving_events_then_desactivate_non_present_events(
        self,
        mock_get,
        mock_process_event_async,
    ):
        _response_mock = Mock()
        _response_mock.content = JANTO_FETCH_RESPONSE

        mock_get.return_value = _response_mock

        mock_process_event_async.return_value = Mock()

        self.create_janto_event(10)

        _pre_count = JantoEvent.objects.filter(status=JantoEventStatus.Inactive.value).count()

        self.use_case()

        _post_count = JantoEvent.objects.filter(status=JantoEventStatus.Inactive.value).count()

        self.assertTrue(mock_get.called)
        self.assertTrue(mock_process_event_async.delay.called)
        self.assertEqual(0, _pre_count)
        self.assertEqual(10, _post_count)
