from django.test import TestCase, Client
from django.urls import reverse

class TestTemplate(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_view_template(self):
        response = self.client.get(reverse('main'))
        self.assertTemplateUsed(response, 'traur2/main.html')