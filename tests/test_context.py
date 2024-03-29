from django.test import TestCase, Client
from django.urls import reverse

class TestContext(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_view_context(self):
        response = self.client.get(reverse('login'))
        self.assertIn('form', response.context)