from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TestModelInteraction(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')