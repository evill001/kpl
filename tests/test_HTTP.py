from django.test import TestCase, Client
from django.urls import reverse

class TestHTTPStatus(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_view_status(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)