from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


CHECK_VIEWSET = "api:check:check"


class CheckViewsetTestCase(APITestCase):

    def test_given_checker_then_return_200(self):
        _response = self.client.get(reverse(CHECK_VIEWSET))

        self.assertEqual(status.HTTP_200_OK, _response.status_code)
        self.assertEqual({}, _response.json())
