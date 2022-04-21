from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from airline.models import Airplane
from airline.utils import get_airplane_per_minute_consumption, airplane_max_minutes_fly_capability


class AccountTests(APITestCase):
    def setUp(self) -> None:
        self.multi_request_data = [
            {
                "airplane_id": 1,
                "passenger_assumptions": 100
            },
            {
                "airplane_id": 3,
                "passenger_assumptions": 200
            },
            {
                "airplane_id": 5,
                "passenger_assumptions": 200
            },
        ]
        self.single_obj_request_data = {
            "airplane_id": 1,
            "passenger_assumptions": 100
        }

        self.over_limit_request_data = [
            {
                "airplane_id": 1,
                "passenger_assumptions": 1
            },
            {
                "airplane_id": 2,
                "passenger_assumptions": 2
            },
            {
                "airplane_id": 3,
                "passenger_assumptions": 3
            },
            {
                "airplane_id": 4,
                "passenger_assumptions": 4
            },
            {
                "airplane_id": 5,
                "passenger_assumptions": 5
            },
            {
                "airplane_id": 6,
                "passenger_assumptions": 6
            },
            {
                "airplane_id": 7,
                "passenger_assumptions": 7
            },
            {
                "airplane_id": 8,
                "passenger_assumptions": 8
            },
            {
                "airplane_id": 9,
                "passenger_assumptions": 9
            },
            {
                "airplane_id": 10,
                "passenger_assumptions": 10
            },
            {
                "airplane_id": 11,
                "passenger_assumptions": 11
            }
        ]

    def test_create_multi_airplane(self):
        """
        Ensure we can create a new multiple Airplane.
        """
        url = reverse('airplane-multi-create')
        response = self.client.post(url, self.multi_request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airplane.objects.count(), len(self.multi_request_data))

    def test_create_single_airplane(self):
        """
        Ensure we can create a new Airplane.
        """
        url = reverse('airplane-list')
        data = self.single_obj_request_data
        expected = {
            **data,
            "per_minute": get_airplane_per_minute_consumption(data['airplane_id'], data['passenger_assumptions']),
            "max_minutes": airplane_max_minutes_fly_capability(data['airplane_id'], data['passenger_assumptions'])
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(response.data, expected)

    def test_limitation_of_airplanes(self):
        """
        Ensure Airplanes is more than 10, so we need to check it
        """
        expected_response = {'detail': 'Airplanes should be not more than 10'}
        url = reverse('airplane-multi-create')
        response = self.client.post(url, self.over_limit_request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(response.data, expected_response)

    def test_available_count_of_airplanes(self):
        """
        Ensure Airplanes is more than 10, so we need to check it
        """
        payload = self.over_limit_request_data.copy()
        payload.pop()
        url = reverse('airplane-multi-create')
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertLess(len(response.data), 11)
