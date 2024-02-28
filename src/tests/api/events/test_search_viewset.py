import random
from datetime import datetime
from urllib.parse import urlencode

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from events_context.models import Event
from shared.domain.enums import EventProvider


SEARCH_VIEWSET = "api:events:search"


class SearchViewsetTestCase(APITestCase):

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

    def test_given_search_viewset_when_valid_params_then_return_200(self):
        _query_params = urlencode({
            "starts_at": datetime(2001, 1, 1, 10, 10, 10),
            "ends_at": datetime(2022, 1, 1, 10, 10, 10),
        })

        _response = self.client.get(f"{reverse(SEARCH_VIEWSET)}?{_query_params}")

        self.assertEqual(status.HTTP_200_OK, _response.status_code)
        self.assertTrue("error" in _response.json())
        self.assertTrue("data" in _response.json())
        self.assertTrue("events" in _response.json()["data"])
        self.assertEqual(Event.objects.all().count(), len(_response.json()["data"]["events"]))

    def test_given_search_viewset_when_missing_ends_at_param_then_return_400(self):
        _query_params = urlencode({
            "starts_at": datetime(2001, 1, 1, 10, 10, 10),
        })

        _response = self.client.get(f"{reverse(SEARCH_VIEWSET)}?{_query_params}")

        self.assertEqual(status.HTTP_400_BAD_REQUEST, _response.status_code)
        self.assertTrue("error" in _response.json())
        self.assertTrue("data" in _response.json())

    def test_given_search_viewset_when_missing_starts_at_param_then_return_400(self):
        _query_params = urlencode({
            "ends_at": datetime(2022, 1, 1, 10, 10, 10),
        })

        _response = self.client.get(f"{reverse(SEARCH_VIEWSET)}?{_query_params}")

        self.assertEqual(status.HTTP_400_BAD_REQUEST, _response.status_code)
        self.assertTrue("error" in _response.json())
        self.assertTrue("data" in _response.json())

    def test_given_search_viewset_when_invalid_starts_at_param_then_return_400(self):
        _query_params = urlencode({
            "starts_at": "2001/12-01",
            "ends_at": datetime(2022, 1, 1, 10, 10, 10),
        })

        _response = self.client.get(f"{reverse(SEARCH_VIEWSET)}?{_query_params}")

        self.assertEqual(status.HTTP_400_BAD_REQUEST, _response.status_code)
        self.assertTrue("error" in _response.json())
        self.assertTrue("data" in _response.json())
